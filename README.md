# TikTok Downloader 🎬

Un descargador de videos de TikTok potente y fácil de usar con almacenamiento de base de datos integrado que puede procesar múltiples URLs desde archivos de texto y organizar descargas de manera eficiente.

## Características ✨

- **Descarga en Lotes**: Descarga múltiples videos de TikTok desde una lista de URLs
- **Integración con Base de Datos**: Base de datos SQLite para almacenar metadatos de videos (título, creador, vistas, etc.)
- **Salida Organizada**: Organiza automáticamente videos, metadatos y registros
- **Seguimiento de Progreso**: Barras de progreso en tiempo real y salida colorizada
- **Manejo de Errores**: Continúa descargando incluso si algunos videos fallan
- **Extracción de Metadatos**: Guarda información de videos y miniaturas
- **Entrada Flexible**: Carga URLs desde cualquier archivo .txt en el directorio de datos
- **Registro Detallado**: Registros de descarga comprensivos con marcas de tiempo
- **Visor de Base de Datos**: Busca, filtra y analiza videos descargados
- **Estadísticas**: Ve estadísticas de descarga y análisis de creadores

## Estructura del Proyecto 📁

```
TikTok_Downloader/
├── TikTokVault/
│   ├── data/                    # Archivos de entrada (listas de URLs)
│   │   └── tiktok_urls.txt     # Archivo de URLs por defecto
│   ├── outputs/                 # Contenido descargado
│   │   ├── videos/             # Archivos de video (.mp4, .mov, etc.)
│   │   ├── logs/               # Registros de descarga (.json)
│   │   ├── metadata/           # Info de videos y miniaturas
│   │   └── tiktok_videos.db    # Base de datos SQLite
│   └── src/
│       ├── TikTokDL.py         # Script principal del descargador
│       ├── database.py         # Gestor de base de datos
│       └── db_viewer.py        # Interfaz del visor de base de datos
├── configs/
│   └── config.ini              # Configuraciones
├── requirements.txt            # Dependencias de Python
├── run_downloader.py          # Punto de entrada principal
└── README.md                  # Este archivo
```

## Instalación 🚀

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/YourUsername/TikTok_Downloader.git
   cd TikTok_Downloader
   ```

2. **Instalar dependencias de Python:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verificar instalación:**
   ```bash
   python run_downloader.py
   ```

## Uso 📖

### Descargar Videos

#### Método 1: Modo Interactivo (Recomendado)

1. **Agregar URLs de TikTok a un archivo:**
   - Crear o editar `TikTokVault/data/tiktok_urls.txt`
   - Agregar una URL de TikTok por línea:
   ```
   https://www.tiktok.com/@username/video/1234567890123456789
   https://www.tiktok.com/@username/video/9876543210987654321
   # Puedes agregar comentarios con #
   ```

2. **Ejecutar el descargador:**
   ```bash
   python run_downloader.py
   ```

3. **¡Selecciona tu archivo de URLs y observa la magia! ✨**

#### Método 2: Modo por Lotes

```bash
# Usar archivo por defecto (tiktok_urls.txt)
python run_downloader.py

# Usar archivo específico
python run_downloader.py mis_urls_personalizadas.txt
```

### Gestión de Base de Datos 🗄️

#### Visor Interactivo de Base de Datos
```bash
python run_downloader.py db
```

#### Operaciones de Base de Datos por Línea de Comandos
```bash
python run_downloader.py db stats

# Mostrar videos recientes (por defecto: 10)
python run_downloader.py db recent
python run_downloader.py db recent 20

# Buscar videos
python run_downloader.py db search "baile"
python run_downloader.py db search "gracioso" creator

# Mostrar todos los videos de un creador
python run_downloader.py db creator nombre_usuario

# Mostrar información detallada del video
python run_downloader.py db video ID_DEL_VIDEO
```

## Características de la Base de Datos 🗄️

La base de datos SQLite integrada almacena automáticamente metadatos completos para todos los videos descargados:

### Información Almacenada
- **Detalles del Video**: Título, descripción, duración, fecha de subida
- **Info del Creador**: Nombre de usuario, nombre para mostrar
- **Estadísticas de Engagement**: Vistas, likes, comentarios, compartidas
- **Info de Archivo**: Ruta del archivo, tamaño, calidad del formato
- **Info de Descarga**: Fecha de descarga, seguimiento de sesiones
- **Tags/Hashtags**: Extraídos de los metadatos del video

### Beneficios de la Base de Datos
- **Buscar y Filtrar**: Encuentra videos por título, creador o contenido
- **Análisis**: Ve estadísticas sobre descargas y creadores
- **Seguimiento de Historial**: Ve qué has descargado y cuándo
- **Prevención de Duplicados**: Evita volver a descargar el mismo video
- **Seguimiento de Lotes**: Monitorea las tasas de éxito de sesiones de descarga

### Comandos Disponibles
- Ver estadísticas y creadores top
- Buscar videos por varios criterios
- Navegar descargas recientes
- Analizar contenido de creadores
- Obtener información detallada de videos

## Formato de Archivo de URLs 📝

Crea archivos `.txt` en el directorio `TikTokVault/data/`:

```txt
# Mi Colección de TikTok
# Las líneas que empiezan con # son comentarios

https://www.tiktok.com/@usuario1/video/1234567890123456789
https://www.tiktok.com/@usuario2/video/9876543210987654321

# Puedes organizar URLs con comentarios
# Videos graciosos:
https://www.tiktok.com/@comediante/video/1111111111111111111

# Videos tutoriales:
https://www.tiktok.com/@maestro/video/2222222222222222222
```

## Configuración ⚙️

Edita `configs/config.ini` para personalizar:

- **Calidad de Video**: Establece la calidad máxima de descarga
- **Organización de Archivos**: Elige patrones de nomenclatura
- **Comportamiento de Descarga**: Establece reintentos, retrasos, manejo de errores
- **Opciones de Salida**: Habilita/deshabilita miniaturas, metadatos

## Archivos de Salida 📂

Después de descargar, encontrarás:

### Directorio de Videos (`TikTokVault/outputs/videos/`)
- **Archivos de video**: `usuario_titulo-video_id-video.mp4`
- **Miniaturas**: `usuario_titulo-video_id-video.jpg`

### Directorio de Registros (`TikTokVault/outputs/logs/`)
- **Registros de descarga**: `download_log_AAAAMMDD_HHMMSS.json`
- Contiene estadísticas de éxito/fallo y resultados detallados

### Directorio de Metadatos (`TikTokVault/outputs/metadata/`)
- **Info de video**: archivos `.info.json` con metadatos completos del video
- **Descripciones**: Títulos de videos, descripciones, fechas de subida

## Ejemplos 🎯

### Ejemplo de Descarga
```
🚀 Iniciando descarga de 5 videos...
📁 Los videos se guardarán en: TikTokVault/outputs/videos
🗄️ Los metadatos se almacenarán en la base de datos

Descargando videos: 60%|██████    | 3/5 [00:45<00:30, 15.2s/video]
✅ Descargado: Video de Baile Increíble por @bailarin123

==================================================
📊 RESUMEN DE DESCARGA
==================================================
✅ Exitosos: 4/5
❌ Fallidos: 1/5  
📈 Tasa de Éxito: 80.0%

🎉 Videos descargados exitosamente:
  • Video de Baile Increíble... por @bailarin123
  • Tutorial de Cocina... por @chef_maestro
  • Compilación de Gatos... por @mascotas_graciosas
  • Proyecto DIY... por @creador_manualidades
```

### Ejemplos de Base de Datos

**Ver Estadísticas:**
```bash
python run_downloader.py db stats
```
Salida:
```
📊 ESTADÍSTICAS DE BASE DE DATOS
📹 Total de Videos: 25
👤 Creadores Únicos: 8  
💾 Tamaño Total: 487.3 MB
🏆 MEJORES CREADORES:
  1. maestro_cocina: 6 videos
  2. bailarin123: 4 videos
```

**Buscar videos de cocina:**
```bash
python run_downloader.py db search "receta"
```

**Ver todos los videos de un creador:**
```bash
python run_downloader.py db creator maestro_cocina
```

## Solución de Problemas 🔧

### Problemas Comunes:

1. **"No module named 'yt_dlp'"**
   ```bash
   pip install -r requirements.txt
   ```

2. **"No se encontraron URLs"**
   - Verifica que tu archivo `.txt` esté en `TikTokVault/data/`
   - Asegúrate de que las URLs contengan 'tiktok.com'
   - Elimina líneas vacías o corrige el formato

3. **Descargas fallando**
   - Algunos videos de TikTok pueden ser privados o estar eliminados
   - Verifica tu conexión a internet
   - Intenta actualizar yt-dlp: `pip install --upgrade yt-dlp`

4. **Errores de permisos**
   - Ejecuta como administrador (Windows) o usa `sudo` (Linux/Mac)
   - Verifica los permisos de las carpetas

### Obtener Ayuda:

- Revisa los archivos de registro en `TikTokVault/outputs/logs/`
- Habilita registro detallado editando el script
- Crea un issue en GitHub con detalles del error

## Contribuir 🤝

1. Hace fork del repositorio
2. Crea una rama de funcionalidad: `git checkout -b nombre-funcionalidad`
3. Commit tus cambios: `git commit -am 'Agregar alguna funcionalidad'`
4. Push a la rama: `git push origin nombre-funcionalidad`
5. Envía un pull request

## Aviso Legal ⚖️

- **Respeta los Derechos de Autor**: Solo descarga videos para los que tengas permiso
- **Uso Personal**: Esta herramienta está destinada para uso personal y educativo
- **Términos de Servicio**: Cumple con los Términos de Servicio de TikTok
- **Uso Justo**: Respeta los derechos de los creadores de contenido

## Dependencias 📦

- `yt-dlp`: Funcionalidad principal de descarga de videos
- `tqdm`: Barras de progreso
- `colorama`: Salida colorizada multiplataforma
- `requests`: Peticiones HTTP
- `pathlib`: Operaciones del sistema de archivos

## Licencia 📄

Este proyecto está licenciado bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para detalles.

## Agradecimientos 👏

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - La increíble librería descargadora de videos
- Creadores de contenido de TikTok - Por el contenido increíble
- Comunidad de Python - Por las excelentes herramientas y librerías

---

**¡Felices Descargas! 🎉**

*Hecho con ❤️ para la comunidad de TikTok*
