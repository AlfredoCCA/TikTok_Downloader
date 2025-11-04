"""
TikTok Downloader - Script Principal
Descarga videos de TikTok desde URLs listadas en archivos del directorio de datos
Guarda los videos descargados en el directorio de salidas con integración de base de datos
"""

# ============================================================================
# IMPORTACIONES DE LIBRERÍAS
# ============================================================================

# Librerías estándar de Python
import json  # Para manejar archivos JSON (logs y metadatos)
import logging  # Para crear logs detallados del sistema
import os  # Para operaciones del sistema operativo
import sys  # Para argumentos de línea de comandos y control del sistema
import uuid  # Para generar identificadores únicos de sesión
from datetime import datetime  # Para timestamps y manejo de fechas
from pathlib import Path  # Para manejo moderno de rutas de archivos

# Librerías externas instaladas via pip
import colorama  # Para colores en la terminal multiplataforma
import yt_dlp  # Motor principal para descargar videos de TikTok
from colorama import Back, Fore, Style  # Específicamente para colores de texto
from database import TikTokDatabase  # Nuestro módulo personalizado para base de datos
from tqdm import tqdm  # Para barras de progreso elegantes

# ============================================================================
# CONFIGURACIÓN INICIAL
# ============================================================================

# Inicializa colorama para que funcione en Windows, Linux y macOS
# autoreset=True hace que los colores se restablezcan automáticamente después de cada print
colorama.init(autoreset=True)

# ============================================================================
# CLASE PRINCIPAL: TikTokDownloader
# ============================================================================

class TikTokDownloader:
    """
    Clase principal que maneja toda la lógica de descarga de videos de TikTok.
    
    Responsabilidades:
    - Configurar directorios y rutas de archivos
    - Cargar URLs desde archivos de texto
    - Descargar videos usando yt-dlp
    - Integrar con base de datos SQLite
    - Generar logs y reportes de descarga
    - Proporcionar interfaz de usuario (CLI)
    """
    
    def __init__(self):
        """
        Constructor: Inicializa el descargador configurando todas las rutas necesarias
        y preparando el entorno de trabajo.
        
        Pasos que realiza:
        1. Define la estructura de directorios del proyecto
        2. Crea directorios faltantes automáticamente
        3. Inicializa la conexión con la base de datos
        4. Configura el sistema de logging
        """
        
        # ====================================================================
        # CONFIGURACIÓN DE RUTAS Y DIRECTORIOS
        # ====================================================================
        
        # Obtiene el directorio base (TikTokVault) navegando desde este archivo
        # __file__ = ruta actual del archivo TikTokDL.py
        # .parent = directorio src
        # .parent = directorio TikTokVault (nuestro directorio base)
        self.base_dir = Path(__file__).parent.parent  # TikTokVault directory
        
        # Define las rutas principales del proyecto
        self.data_dir = self.base_dir / "data"        # Archivos de entrada (URLs)
        self.outputs_dir = self.base_dir / "outputs"  # Todos los archivos de salida
        
        # ====================================================================
        # CREACIÓN AUTOMÁTICA DE DIRECTORIOS
        # ====================================================================
        
        # Crea los directorios principales si no existen
        # exist_ok=True evita errores si ya existen
        self.data_dir.mkdir(exist_ok=True)
        self.outputs_dir.mkdir(exist_ok=True)
        
        # Define y crea subdirectorios para organizar las salidas
        self.videos_dir = self.outputs_dir / "videos"      # Videos descargados (.mp4, .mov)
        self.logs_dir = self.outputs_dir / "logs"          # Archivos de log (.log, .json)
        self.metadata_dir = self.outputs_dir / "metadata"  # Metadatos (.info.json, thumbnails)
        
        # Crea todos los subdirectorios de salida de una vez
        for dir_path in [self.videos_dir, self.logs_dir, self.metadata_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # ====================================================================
        # INICIALIZACIÓN DE COMPONENTES PRINCIPALES
        # ====================================================================
        
        # Inicializa la conexión con la base de datos SQLite
        # Esto crea las tablas necesarias si no existen
        self.db = TikTokDatabase()
        
        # ====================================================================
        # CONFIGURACIÓN DEL SISTEMA DE LOGGING
        # ====================================================================
        
        # Configura el logging para escribir tanto a archivo como a consola
        logging.basicConfig(
            level=logging.INFO,  # Nivel mínimo de logs a mostrar
            format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de mensajes
            handlers=[
                # Handler 1: Escribe logs a un archivo en el directorio de logs
                logging.FileHandler(self.logs_dir / 'app.log'),
                # Handler 2: Muestra logs en la consola/terminal
                logging.StreamHandler()
            ]
        )
    
    # ========================================================================
    # MÉTODO: CARGAR URLs DESDE ARCHIVO
    # ========================================================================
    
    def load_urls_from_file(self, filename="tiktok_urls.txt"):
        """
        Carga y valida URLs de TikTok desde un archivo de texto en el directorio de datos.
        
        Parámetros:
            filename (str): Nombre del archivo a leer (por defecto: "tiktok_urls.txt")
        
        Retorna:
            list: Lista de URLs válidas de TikTok encontradas en el archivo
        
        Funcionalidad:
        1. Verifica que el archivo exista
        2. Lee línea por línea
        3. Filtra líneas vacías y comentarios (que empiecen con #)
        4. Valida que contengan 'tiktok.com'
        5. Muestra advertencias para URLs inválidas
        6. Retorna lista limpia de URLs válidas
        """
        
        # Construye la ruta completa del archivo
        file_path = self.data_dir / filename
        
        # ====================================================================
        # VERIFICACIÓN DE EXISTENCIA DEL ARCHIVO
        # ====================================================================
        
        # Si el archivo no existe, muestra error y guías útiles
        if not file_path.exists():
            print(f"{Fore.RED}❌ File {filename} not found in data directory!")
            print(f"{Fore.YELLOW}💡 Create a file at: {file_path}")
            print(f"{Fore.YELLOW}💡 Add TikTok URLs, one per line")
            return []  # Retorna lista vacía
        
        # ====================================================================
        # PROCESAMIENTO DEL ARCHIVO
        # ====================================================================
        
        urls = []  # Lista para almacenar URLs válidas
        
        try:
            # Abre el archivo con codificación UTF-8 para caracteres especiales
            with open(file_path, 'r', encoding='utf-8') as file:
                
                # Procesa cada línea con numeración para reportes de error
                for line_num, line in enumerate(file, 1):
                    
                    # Limpia espacios en blanco al inicio y final
                    line = line.strip()
                    
                    # ============================================================
                    # FILTRADO DE LÍNEAS
                    # ============================================================
                    
                    # Salta líneas vacías y comentarios (que empiecen con #)
                    if line and not line.startswith('#'):
                        
                        # Valida que sea una URL de TikTok
                        if 'tiktok.com' in line:
                            urls.append(line)  # Agrega URL válida a la lista
                        else:
                            # Muestra advertencia para URLs no válidas
                            print(f"{Fore.YELLOW}⚠️  Line {line_num}: Not a TikTok URL - {line}")
            
            # ================================================================
            # REPORTE DE RESULTADOS
            # ================================================================
            
            # Muestra resumen de URLs cargadas exitosamente
            print(f"{Fore.GREEN}📂 Loaded {len(urls)} URLs from {filename}")
            return urls
        
        # ====================================================================
        # MANEJO DE ERRORES
        # ====================================================================
        
        except Exception as e:
            # Captura cualquier error de lectura del archivo
            print(f"{Fore.RED}❌ Error reading file {filename}: {str(e)}")
            return []  # Retorna lista vacía en caso de error
    
    # ========================================================================
    # MÉTODO: CONFIGURACIÓN DE yt-dlp
    # ========================================================================
    
    def setup_ydl_options(self):
        """
        Configura las opciones para yt-dlp (YouTube-DL Plus), que es la librería
        que se encarga de descargar videos de TikTok y otras plataformas.
        
        Retorna:
            dict: Diccionario con configuraciones para yt-dlp
        
        Configuraciones incluidas:
        - Formato de nombres de archivo
        - Calidad de video preferida
        - Archivos adicionales a descargar (metadatos, thumbnails)
        - Comportamiento ante errores
        """
        
        return {
            # ================================================================
            # CONFIGURACIÓN DE NOMBRES DE ARCHIVO
            # ================================================================
            
            # Define el patrón para nombrar archivos descargados
            # %(uploader)s = Nombre del creador del video
            # %(title)s = Título del video
            # %(id)s = ID único del video en TikTok
            # %(ext)s = Extensión del archivo (mp4, mov, etc.)
            'outtmpl': str(self.videos_dir / '%(uploader)s_%(title)s_%(id)s.%(ext)s'),
            
            # ================================================================
            # CONFIGURACIÓN DE CALIDAD DE VIDEO
            # ================================================================
            
            # Selecciona la mejor calidad disponible hasta 720p
            # Si no hay 720p disponible, toma la mejor calidad disponible
            # Esto balancea calidad vs tamaño de archivo
            'format': 'best[height<=720]/best',
            
            # ================================================================
            # ARCHIVOS ADICIONALES A DESCARGAR
            # ================================================================
            
            # Guarda metadatos del video en formato JSON
            # Incluye información como título, descripción, vistas, likes, etc.
            'writeinfojson': True,
            
            # Descarga thumbnail/miniatura del video
            # Útil para vista previa y organización
            'writethumbnail': True,
            
            # No descarga subtítulos (TikTok generalmente no los tiene)
            'writesubtitles': False,
            
            # ================================================================
            # CONFIGURACIÓN DE COMPORTAMIENTO
            # ================================================================
            
            # Continúa descargando otros videos aunque uno falle
            # Evita que un error detenga todo el proceso
            'ignoreerrors': True,
            
            # Muestra advertencias (útil para debugging)
            'no_warnings': False,
            
            # No extrae solo información, descarga el archivo completo
            'extract_flat': False,
        }
    
    # ========================================================================
    # MÉTODO PRINCIPAL: DESCARGA DE VIDEOS
    # ========================================================================
    
    def download_videos(self, urls, source_file=None):
        """
        Método principal que descarga una lista de videos de TikTok con integración
        completa de base de datos y seguimiento de progreso.
        
        Parámetros:
            urls (list): Lista de URLs de TikTok a descargar
            source_file (str): Nombre del archivo de origen (opcional, para logs)
        
        Retorna:
            tuple: (lista_exitosos, lista_fallidos)
        
        Proceso completo:
        1. Validación inicial
        2. Creación de sesión de descarga
        3. Configuración de yt-dlp
        4. Loop de descarga con barra de progreso
        5. Integración con base de datos
        6. Manejo de errores
        7. Generación de logs
        """
        
        # ====================================================================
        # VALIDACIÓN INICIAL
        # ====================================================================
        
        # Verifica que hay URLs para procesar
        if not urls:
            print(f"{Fore.RED}❌ No URLs to download!")
            return [], []  # Retorna listas vacías

        # ====================================================================
        # INFORMACIÓN INICIAL AL USUARIO
        # ====================================================================
        
        # Muestra información sobre la sesión que va a iniciar
        print(f"{Fore.CYAN}🚀 Starting download of {len(urls)} videos...")
        print(f"{Fore.CYAN}📁 Videos will be saved to: {self.videos_dir}")
        print(f"{Fore.CYAN}🗄️  Metadata will be stored in database")

        # ====================================================================
        # INICIALIZACIÓN DE SESIÓN DE DESCARGA
        # ====================================================================
        
        # Crea un ID único para esta sesión de descarga
        # Permite rastrear estadísticas por sesión en la base de datos
        session_id = str(uuid.uuid4())
        
        # Registra el inicio de la sesión en la base de datos
        self.db.start_download_session(session_id, len(urls), source_file)

        # ====================================================================
        # INICIALIZACIÓN DE LISTAS DE RESULTADOS
        # ====================================================================
        
        # Listas para almacenar resultados separados
        successful_downloads = []  # Videos descargados exitosamente
        failed_downloads = []      # Videos que fallaron

        # ====================================================================
        # CONFIGURACIÓN DE yt-dlp
        # ====================================================================
        
        # Obtiene las opciones de configuración definidas anteriormente
        ydl_opts = self.setup_ydl_options()

        # ====================================================================
        # PROCESO PRINCIPAL DE DESCARGA
        # ====================================================================
        
        # Crea instancia de yt-dlp con las opciones configuradas
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            
            # Crea barra de progreso para mostrar avance visual
            # desc: texto descriptivo
            # unit: unidad de medida para la barra
            with tqdm(urls, desc="Downloading videos", unit="video") as pbar:
                
                # ============================================================
                # LOOP PRINCIPAL: PROCESA CADA URL
                # ============================================================
                
                for i, url in enumerate(pbar):
                    try:
                        # ====================================================
                        # ACTUALIZACIÓN DE PROGRESO VISUAL
                        # ====================================================
                        
                        # Actualiza el texto de la barra de progreso
                        pbar.set_description(f"Downloading video {i+1}/{len(urls)}")

                        # ====================================================
                        # PASO 1: EXTRACCIÓN DE INFORMACIÓN PREVIA
                        # ====================================================
                        
                        # Extrae información del video SIN descargarlo aún
                        # Esto permite mostrar información antes de la descarga
                        info = ydl.extract_info(url, download=False)
                        
                        # Obtiene datos básicos del video
                        title = info.get('title', 'Unknown')      # Título del video
                        uploader = info.get('uploader', 'Unknown') # Creador del video

                        # Actualiza la barra de progreso con información del video actual
                        pbar.set_postfix_str(f"'{title[:30]}...' by {uploader}")

                        # ====================================================
                        # PASO 2: DESCARGA REAL DEL VIDEO
                        # ====================================================
                        
                        # Descarga el video y obtiene información completa
                        # Esta llamada hace la descarga real del archivo
                        final_info = ydl.extract_info(url, download=True)
                        
                        # ====================================================
                        # PASO 3: REGISTRO EN BASE DE DATOS
                        # ====================================================
                        
                        # Guarda toda la información del video en la base de datos SQLite
                        self.db.add_video(final_info)

                        # ====================================================
                        # PASO 4: REGISTRO DE ÉXITO
                        # ====================================================
                        
                        # Crea registro detallado del video descargado exitosamente
                        successful_downloads.append({
                            'url': url,                                    # URL original
                            'title': title,                               # Título del video
                            'uploader': uploader,                         # Creador
                            'video_id': final_info.get('id', ''),        # ID único de TikTok
                            'timestamp': datetime.now().isoformat()      # Momento de descarga
                        })

                        # Muestra mensaje de éxito con colores
                        print(f"\n{Fore.GREEN}✅ Downloaded: {title} by {uploader}")

                    # ========================================================
                    # MANEJO DE ERRORES DURANTE LA DESCARGA
                    # ========================================================
                    
                    except Exception as e:
                        # Captura cualquier error durante el proceso de descarga
                        error_msg = str(e)
                        
                        # ================================================
                        # REGISTRO DE ERROR EN BASE DE DATOS
                        # ================================================
                        
                        # Registra la descarga fallida en la base de datos
                        self.db.add_failed_download(url, error_msg)
                        
                        # ================================================
                        # REGISTRO DE ERROR EN MEMORIA
                        # ================================================
                        
                        # Crea registro detallado del error
                        failed_downloads.append({
                            'url': url,                              # URL que falló
                            'error': error_msg,                      # Mensaje de error
                            'timestamp': datetime.now().isoformat() # Momento del error
                        })

                        # Muestra mensaje de error con colores
                        print(f"\n{Fore.RED}❌ Failed to download {url}")
                        print(f"{Fore.RED}   Error: {error_msg}")

        # ====================================================================
        # FINALIZACIÓN DE SESIÓN
        # ====================================================================
        
        # Registra el final de la sesión en la base de datos con estadísticas
        self.db.end_download_session(session_id, len(successful_downloads), len(failed_downloads))

        # ====================================================================
        # GENERACIÓN DE LOG DE DESCARGA
        # ====================================================================
        
        # Crea archivo de log detallado con todos los resultados
        self.save_download_log(successful_downloads, failed_downloads)

        # ====================================================================
        # RETORNO DE RESULTADOS
        # ====================================================================
        
        # Retorna ambas listas para que el código que llama pueda procesarlas
        return successful_downloads, failed_downloads
    
    # ========================================================================
    # MÉTODO: GUARDAR LOG DE DESCARGA
    # ========================================================================
    
    def save_download_log(self, successful, failed):
        """
        Guarda un log detallado de la sesión de descarga en formato JSON.
        Este archivo sirve como registro histórico y para debugging.
        
        Parámetros:
            successful (list): Lista de descargas exitosas
            failed (list): Lista de descargas fallidas
        
        Funcionalidad:
        1. Genera timestamp único para el archivo
        2. Calcula estadísticas de la sesión
        3. Estructura toda la información en formato JSON
        4. Guarda el archivo en el directorio de logs
        """
        
        # ====================================================================
        # GENERACIÓN DE NOMBRE DE ARCHIVO ÚNICO
        # ====================================================================
        
        # Crea timestamp en formato YYYYMMDD_HHMMSS para nombres únicos
        # Ejemplo: 20241027_143052
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Construye la ruta completa del archivo de log
        log_file = self.logs_dir / f"download_log_{timestamp}.json"
        
        # ====================================================================
        # ESTRUCTURACIÓN DE DATOS DEL LOG
        # ====================================================================
        
        # Crea diccionario con toda la información de la sesión
        log_data = {
            # Información temporal
            'timestamp': datetime.now().isoformat(),  # Momento exacto de creación del log
            
            # Estadísticas numéricas
            'total_urls': len(successful) + len(failed),     # Total de URLs procesadas
            'successful_downloads': len(successful),          # Cantidad de éxitos
            'failed_downloads': len(failed),                 # Cantidad de fallos
            
            # Cálculo de tasa de éxito
            # Usa operador ternario para evitar división por cero
            'success_rate': len(successful) / (len(successful) + len(failed)) * 100 if (successful or failed) else 0,
            
            # Datos detallados de cada descarga
            'successful': successful,  # Lista completa de descargas exitosas
            'failed': failed          # Lista completa de descargas fallidas
        }
        
        # ====================================================================
        # ESCRITURA DEL ARCHIVO
        # ====================================================================
        
        try:
            # Abre archivo para escritura con codificación UTF-8
            with open(log_file, 'w', encoding='utf-8') as f:
                # Guarda como JSON con formato legible
                # indent=2: indentación de 2 espacios para legibilidad
                # ensure_ascii=False: permite caracteres especiales (emojis, acentos)
                json.dump(log_data, f, indent=2, ensure_ascii=False)
            
            # Confirma que el log se guardó exitosamente
            print(f"{Fore.BLUE}📝 Download log saved to: {log_file}")
            
        except Exception as e:
            # Maneja errores de escritura del archivo
            print(f"{Fore.RED}❌ Failed to save log: {str(e)}")
    
    # ========================================================================
    # MÉTODO: MOSTRAR RESUMEN DE DESCARGA
    # ========================================================================
    
    def print_summary(self, successful, failed):
        """
        Muestra un resumen visual y detallado de los resultados de la descarga.
        Presenta estadísticas, listas de éxitos y fallos de manera organizada.
        
        Parámetros:
            successful (list): Lista de descargas exitosas
            failed (list): Lista de descargas fallidas
        
        Funcionalidad:
        1. Calcula estadísticas generales
        2. Muestra resumen con formato visual atractivo
        3. Lista videos descargados exitosamente (primeros 5)
        4. Lista errores de descarga (primeros 3)
        5. Usa colores para mejor legibilidad
        """
        
        # ====================================================================
        # CÁLCULO DE ESTADÍSTICAS
        # ====================================================================
        
        # Calcula totales y porcentajes
        total = len(successful) + len(failed)                          # Total de URLs procesadas
        success_rate = (len(successful) / total * 100) if total > 0 else 0  # Porcentaje de éxito
        
        # ====================================================================
        # ENCABEZADO DEL RESUMEN
        # ====================================================================
        
        # Crea separador visual llamativo
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}📊 DOWNLOAD SUMMARY")  # Título del resumen
        print(f"{Fore.CYAN}{'='*50}")
        
        # ====================================================================
        # ESTADÍSTICAS PRINCIPALES
        # ====================================================================
        
        # Muestra estadísticas numéricas con colores específicos
        print(f"{Fore.GREEN}✅ Successful: {len(successful)}/{total}")   # Éxitos en verde
        print(f"{Fore.RED}❌ Failed: {len(failed)}/{total}")            # Fallos en rojo
        print(f"{Fore.BLUE}📈 Success Rate: {success_rate:.1f}%")       # Porcentaje en azul
        
        # ====================================================================
        # LISTA DE DESCARGAS EXITOSAS
        # ====================================================================
        
        if successful:
            print(f"\n{Fore.GREEN}🎉 Successfully downloaded videos:")
            
            # Muestra los primeros 5 videos descargados
            for item in successful[:5]:
                # Trunca título largo a 50 caracteres para mejor formato
                truncated_title = item['title'][:50] + "..." if len(item['title']) > 50 else item['title']
                print(f"  • {truncated_title} by {item['uploader']}")
            
            # Si hay más de 5, indica cuántos más hay
            if len(successful) > 5:
                print(f"  ... and {len(successful) - 5} more")
        
        # ====================================================================
        # LISTA DE DESCARGAS FALLIDAS
        # ====================================================================
        
        if failed:
            print(f"\n{Fore.RED}💥 Failed downloads:")
            
            # Muestra los primeros 3 fallos para no saturar la pantalla
            for item in failed[:3]:
                print(f"  • {item['url']}")  # URL que falló
                
                # Trunca mensaje de error a 100 caracteres
                truncated_error = item['error'][:100] + "..." if len(item['error']) > 100 else item['error']
                print(f"    Error: {truncated_error}")
            
            # Si hay más de 3 fallos, indica cuántos más hay
            if len(failed) > 3:
                print(f"  ... and {len(failed) - 3} more failures")
    
    # ========================================================================
    # MÉTODO: LISTAR ARCHIVOS DISPONIBLES
    # ========================================================================
    
    def list_available_files(self):
        """
        Busca y lista todos los archivos .txt disponibles en el directorio de datos.
        Estos archivos contienen las URLs de TikTok a descargar.
        
        Retorna:
            list: Lista de objetos Path de archivos .txt encontrados
        
        Funcionalidad:
        1. Busca archivos .txt en el directorio de datos
        2. Los muestra numerados para selección del usuario
        3. Retorna la lista para uso posterior
        """
        
        # ====================================================================
        # BÚSQUEDA DE ARCHIVOS
        # ====================================================================
        
        # Busca todos los archivos .txt en el directorio de datos
        # glob("*.txt") encuentra archivos que terminen en .txt
        txt_files = list(self.data_dir.glob("*.txt"))
        
        # ====================================================================
        # PRESENTACIÓN DE ARCHIVOS ENCONTRADOS
        # ====================================================================
        
        if txt_files:
            # Si hay archivos, los muestra numerados
            print(f"{Fore.CYAN}📂 Available URL files in data directory:")
            
            # Enumera archivos empezando desde 1 (más intuitivo para usuarios)
            for i, file in enumerate(txt_files, 1):
                print(f"  {i}. {file.name}")  # Muestra solo el nombre, no la ruta completa
            
            return txt_files  # Retorna lista para uso posterior
        else:
            # Si no hay archivos, informa al usuario
            print(f"{Fore.YELLOW}📂 No .txt files found in data directory")
            return []  # Retorna lista vacía
    
    # ========================================================================
    # MÉTODO: MODO INTERACTIVO
    # ========================================================================
    
    def run_interactive(self):
        """
        Ejecuta el descargador en modo interactivo, donde el usuario puede
        seleccionar archivos de URLs mediante un menú visual.
        
        Funcionalidad:
        1. Muestra encabezado atractivo
        2. Lista archivos disponibles
        3. Permite al usuario seleccionar un archivo
        4. Valida la selección del usuario
        5. Ejecuta la descarga
        6. Muestra resumen de resultados
        
        Este modo es ideal para usuarios principiantes o uso ocasional.
        """
        
        # ====================================================================
        # ENCABEZADO DEL MODO INTERACTIVO
        # ====================================================================
        
        # Crea una interfaz visual atractiva
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}🎬 TikTok Downloader - Interactive Mode")
        print(f"{Fore.MAGENTA}{'='*60}")
        
        # ====================================================================
        # LISTADO DE ARCHIVOS DISPONIBLES
        # ====================================================================
        
        # Obtiene lista de archivos .txt disponibles
        available_files = self.list_available_files()
        
        # Si no hay archivos, informa al usuario y termina
        if not available_files:
            print(f"{Fore.YELLOW}💡 Create a .txt file in the data directory with TikTok URLs")
            return  # Sale del método
        
        # ====================================================================
        # SELECCIÓN INTERACTIVA DE ARCHIVO
        # ====================================================================
        
        # Loop infinito hasta que el usuario haga una selección válida o salga
        while True:
            try:
                # ============================================================
                # CAPTURA DE ENTRADA DEL USUARIO
                # ============================================================
                
                # Solicita al usuario que elija un archivo o salga
                choice = input(f"\n{Fore.CYAN}Enter file number (or 'q' to quit): ").strip()
                
                # ============================================================
                # MANEJO DE COMANDO DE SALIDA
                # ============================================================
                
                # Si el usuario escribe 'q', sale del programa
                if choice.lower() == 'q':
                    return  # Termina el método
                
                # ============================================================
                # VALIDACIÓN DE SELECCIÓN NUMÉRICA
                # ============================================================
                
                # Convierte la entrada a número (puede lanzar ValueError)
                file_index = int(choice) - 1  # Resta 1 porque la lista interna empieza en 0
                
                # Verifica que el índice esté dentro del rango válido
                if 0 <= file_index < len(available_files):
                    selected_file = available_files[file_index]  # Selecciona el archivo
                    break  # Sale del loop de selección
                else:
                    # Índice fuera de rango
                    print(f"{Fore.RED}❌ Invalid choice. Please try again.")
                    
            except ValueError:
                # La entrada no es un número válido
                print(f"{Fore.RED}❌ Please enter a valid number.")
        
        # ====================================================================
        # EJECUCIÓN DE LA DESCARGA
        # ====================================================================
        
        # Carga URLs del archivo seleccionado
        urls = self.load_urls_from_file(selected_file.name)
        
        # Si se encontraron URLs válidas, procede con la descarga
        if urls:
            # Ejecuta el proceso de descarga
            successful, failed = self.download_videos(urls, selected_file.name)
            
            # Muestra resumen detallado de resultados
            self.print_summary(successful, failed)
    
    # ========================================================================
    # MÉTODO: MODO BATCH (POR LOTES)
    # ========================================================================
    
    def run_batch(self, filename="tiktok_urls.txt"):
        """
        Ejecuta el descargador en modo batch (por lotes) con un archivo específico.
        Este modo es ideal para automatización y uso programático.
        
        Parámetros:
            filename (str): Nombre del archivo a procesar (por defecto: "tiktok_urls.txt")
        
        Funcionalidad:
        1. Muestra encabezado del modo batch
        2. Carga URLs del archivo especificado
        3. Ejecuta descarga automáticamente
        4. Muestra resumen de resultados
        5. Maneja errores si el archivo no existe o está vacío
        
        Este modo es ideal para:
        - Scripts automatizados
        - Procesamiento de archivos específicos
        - Integración con otros sistemas
        """
        
        # ====================================================================
        # ENCABEZADO DEL MODO BATCH
        # ====================================================================
        
        # Muestra interfaz para modo batch
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}🎬 TikTok Downloader - Batch Mode")
        print(f"{Fore.MAGENTA}{'='*60}")
        
        # ====================================================================
        # CARGA DE URLs DEL ARCHIVO ESPECIFICADO
        # ====================================================================
        
        # Intenta cargar URLs del archivo especificado
        urls = self.load_urls_from_file(filename)
        
        # ====================================================================
        # PROCESAMIENTO BASADO EN RESULTADOS
        # ====================================================================
        
        if urls:
            # ================================================================
            # CASO: URLS ENCONTRADAS - PROCESAR DESCARGA
            # ================================================================
            
            # Ejecuta descarga con el archivo como fuente para tracking
            successful, failed = self.download_videos(urls, filename)
            
            # Muestra resumen completo de resultados
            self.print_summary(successful, failed)
        else:
            # ================================================================
            # CASO: NO HAY URLS - MOSTRAR ERROR
            # ================================================================
            
            # Informa al usuario que no se encontraron URLs válidas
            print(f"{Fore.RED}❌ No URLs found or file doesn't exist")

# ============================================================================
# FUNCIÓN PRINCIPAL Y PUNTO DE ENTRADA
# ============================================================================

def main():
    """
    Función principal que actúa como punto de entrada del programa.
    Determina el modo de ejecución basado en argumentos de línea de comandos.
    
    Lógica de decisión:
    - Si hay argumentos: Modo batch con archivo específico
    - Si no hay argumentos: Modo interactivo
    
    Funcionalidad:
    1. Crea instancia del descargador
    2. Analiza argumentos de línea de comandos
    3. Ejecuta el modo apropiado
    """
    
    # ========================================================================
    # INICIALIZACIÓN DEL DESCARGADOR
    # ========================================================================
    
    # Crea una instancia de la clase TikTokDownloader
    # Esto ejecuta __init__() que configura directorios, base de datos, etc.
    downloader = TikTokDownloader()
    
    # ========================================================================
    # ANÁLISIS DE ARGUMENTOS DE LÍNEA DE COMANDOS
    # ========================================================================
    
    # sys.argv contiene los argumentos pasados al script
    # sys.argv[0] = nombre del script
    # sys.argv[1] = primer argumento (si existe)
    # len(sys.argv) > 1 significa que hay al menos un argumento
    
    if len(sys.argv) > 1:
        # ====================================================================
        # MODO BATCH: ARCHIVO ESPECÍFICO
        # ====================================================================
        
        # Obtiene el nombre del archivo del primer argumento
        filename = sys.argv[1]
        
        # Ejecuta descarga en modo batch con el archivo especificado
        # Ejemplo: python TikTokDL.py mi_lista.txt
        downloader.run_batch(filename)
    else:
        # ====================================================================
        # MODO INTERACTIVO: SIN ARGUMENTOS
        # ====================================================================
        
        # Si no hay argumentos, ejecuta modo interactivo
        # El usuario podrá seleccionar archivos desde un menú
        # Ejemplo: python TikTokDL.py
        downloader.run_interactive()

# ============================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# ============================================================================

# Este bloque solo se ejecuta cuando el archivo se ejecuta directamente,
# no cuando se importa como módulo
if __name__ == "__main__":
    """
    Punto de entrada principal del programa con manejo robusto de errores.
    
    Maneja tres tipos de situaciones:
    1. Ejecución normal: Llama a main()
    2. Interrupción del usuario (Ctrl+C): Salida limpia
    3. Errores inesperados: Muestra error y sale con código de error
    """
    
    try:
        # ====================================================================
        # EJECUCIÓN NORMAL DEL PROGRAMA
        # ====================================================================
        
        # Ejecuta la función principal
        main()
        
    except KeyboardInterrupt:
        # ====================================================================
        # MANEJO DE INTERRUPCIÓN DEL USUARIO (Ctrl+C)
        # ====================================================================
        
        # El usuario presionó Ctrl+C para detener el programa
        print(f"\n{Fore.YELLOW}⚠️  Download interrupted by user")
        sys.exit(0)  # Sale con código 0 (salida limpia)
        
    except Exception as e:
        # ====================================================================
        # MANEJO DE ERRORES INESPERADOS
        # ====================================================================
        
        # Captura cualquier error no manejado en el programa
        print(f"\n{Fore.RED}💥 Unexpected error: {str(e)}")
        sys.exit(1)  # Sale con código 1 (error)
        sys.exit(1)  # Línea duplicada - debería eliminarse en limpieza de código
