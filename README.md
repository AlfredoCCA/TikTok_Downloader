# TikTok Downloader 🎬

<div align="center">

[![Version](https://img.shields.io/badge/Version-1.5.0-blue?style=for-the-badge)](https://github.com/AlfredoCCA/TikTok_Downloader/releases)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-red?style=for-the-badge&logo=gnu&logoColor=white)](COPYING)
[![Database](https://img.shields.io/badge/Database-SQLite-orange?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

[![GitHub Stars](https://img.shields.io/github/stars/AlfredoCCA/TikTok_Downloader?style=social)](https://github.com/AlfredoCCA/TikTok_Downloader/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/AlfredoCCA/TikTok_Downloader?style=social)](https://github.com/AlfredoCCA/TikTok_Downloader/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/AlfredoCCA/TikTok_Downloader?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/AlfredoCCA/TikTok_Downloader?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader/pulls)

[![Downloads](https://img.shields.io/github/downloads/AlfredoCCA/TikTok_Downloader/total?style=flat-square&color=brightgreen)](https://github.com/AlfredoCCA/TikTok_Downloader/releases)
[![Last Commit](https://img.shields.io/github/last-commit/AlfredoCCA/TikTok_Downloader?style=flat-square&color=blue)](https://github.com/AlfredoCCA/TikTok_Downloader/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/AlfredoCCA/TikTok_Downloader?style=flat-square&color=orange)](https://github.com/AlfredoCCA/TikTok_Downloader)
[![Code Size](https://img.shields.io/github/languages/code-size/AlfredoCCA/TikTok_Downloader?style=flat-square&color=lightblue)](https://github.com/AlfredoCCA/TikTok_Downloader)

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-green?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader/commits/main)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Powered by yt-dlp](https://img.shields.io/badge/Powered%20by-yt--dlp-red?style=flat-square&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![Data Storage](https://img.shields.io/badge/Data%20Storage-SQLite-orange?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![CLI Interface](https://img.shields.io/badge/Interface-CLI-purple?style=flat-square&logo=terminal&logoColor=white)](https://github.com/AlfredoCCA/TikTok_Downloader)

</div>

---

Un descargador profesional de videos de TikTok con sistema avanzado de base de datos SQLite que proporciona gestión completa de metadatos, búsqueda inteligente, y análisis detallado de contenido descargado.

## 📚 Tabla de Contenido

<details>
<summary>🔍 Expandir Navegación</summary>

- [🎯 Características](#características-)
- [📁 Estructura del Proyecto](#estructura-del-proyecto-)
- [🚀 Instalación y Configuración](#instalación-y-configuración-)
- [📖 Uso Detallado](#uso-detallado-)
- [🗄️ Sistema de Base de Datos](#sistema-de-base-de-datos-️)
- [📝 Formato de Archivo de URLs](#formato-de-archivo-de-urls-)
- [⚙️ Configuración Avanzada](#configuración-avanzada-️)
- [📂 Archivos de Salida](#archivos-de-salida-)
- [🔒 Gestión de Archivos y Privacidad](#-gestión-de-archivos-y-privacidad)
- [🎯 Ejemplos Prácticos](#ejemplos-prácticos-)
- [🔧 Solución de Problemas](#solución-de-problemas-)
- [🤝 Contribuir al Proyecto](#contribuir-al-proyecto-)
- [⚖️ Aviso Legal](#aviso-legal-️)
- [🔧 Características Técnicas](#características-técnicas-)
- [📄 Licencia](#licencia-)
- [👏 Agradecimientos](#agradecimientos-)

</details>

---

## ⚡ Instalación Rápida

<div align="center">

[![Install with pip](https://img.shields.io/badge/Install%20with-pip-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pip/)
[![Git Clone](https://img.shields.io/badge/Git-Clone-orange?style=for-the-badge&logo=git&logoColor=white)](https://github.com/AlfredoCCA/TikTok_Downloader.git)
[![Download ZIP](https://img.shields.io/badge/Download-ZIP-green?style=for-the-badge&logo=download&logoColor=white)](https://github.com/AlfredoCCA/TikTok_Downloader/archive/refs/heads/main.zip)

</div>

```bash
# 1. Clonar repositorio
git clone https://github.com/AlfredoCCA/TikTok_Downloader.git
cd TikTok_Downloader

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar entorno
python setup_environment.py

# 4. ¡Usar!
python run_downloader.py
```

**[📖 Ver Guía Completa de Instalación](#instalación-y-configuración-)**

---

## Características ✨

### 📥 Descarga Avanzada
- **Descarga en Lotes**: Procesa múltiples URLs desde archivos de texto
- **Control de Calidad**: Configuración flexible de calidad de video (hasta 1080p)
- **Gestión de Archivos**: Organización automática con metadatos y miniaturas
- **Manejo de Errores Robusto**: Continúa descargando aunque algunos videos fallen
- **Prevención de Duplicados**: Evita descargar el mismo video múltiples veces
- **Configuración Personalizable**: Configuración avanzada a través de archivos INI

### 🗄️ Sistema de Base de Datos Completo
- **Base de Datos SQLite**: Almacenamiento persistente de metadatos de videos
- **Seguimiento de Sesiones**: Historial completo de descargas por sesión
- **Búsqueda Inteligente**: Busca por título, creador, descripción o contenido
- **Análisis de Creadores**: Estadísticas detalladas por creador de contenido
- **Métricas de Engagement**: Tracking de vistas, likes, comentarios y shares
- **Exportación de Datos**: Información estructurada para análisis posterior

### 🎯 Interfaz de Usuario
- **Modo Interactivo**: Interfaz de menú intuitiva para navegación
- **Comandos CLI**: Acceso directo a funciones específicas vía línea de comandos
- **Salida Colorizada**: Interfaz visual mejorada con códigos de color
- **Barras de Progreso**: Seguimiento en tiempo real del progreso de descarga
- **Configuración Automática**: Script de configuración para nuevos usuarios

## Estructura del Proyecto 📁

```
TikTok_Downloader/
├── configs/                          # Archivos de configuración
│   ├── config.ini                   # Configuración general del downloader
│   └── database_config.ini          # Configuración específica de base de datos
├── TikTokVault/                      # Directorio principal del proyecto
│   ├── data/                        # Archivos de entrada (listas de URLs)
│   │   ├── tiktok_urls.example.txt  # Archivo de ejemplo con URLs ficticias
│   │   └── tiktok_urls.txt          # Tu archivo personal de URLs (no versionado)
│   ├── outputs/                     # Todo el contenido descargado
│   │   ├── videos/                  # Videos descargados (.mp4, .mov, etc.)
│   │   ├── logs/                    # Registros de descarga (.json, .log)
│   │   ├── metadata/                # Información detallada de videos (.json)
│   │   └── tiktok_videos.db         # Base de datos SQLite principal
│   └── src/                         # Código fuente del proyecto
│       ├── TikTokDL.py             # Motor principal de descarga
│       ├── database.py             # Gestor de base de datos SQLite
│       └── db_viewer.py            # Interfaz de consulta de base de datos
├── run_downloader.py                # Punto de entrada principal unificado
├── setup_environment.py            # Script de configuración automática
├── requirements.txt                 # Dependencias de Python
├── DATABASE_FEATURES.md            # Documentación detallada de la base de datos
└── README.md                       # Esta documentación
```

## Instalación y Configuración 🚀

### 1. Clonar el Repositorio
```bash
git clone https://github.com/AlfredoCCA/TikTok_Downloader.git
cd TikTok_Downloader
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración Automática
```bash
python setup_environment.py
```
Este script:
- Crea tu archivo personal `tiktok_urls.txt` desde el ejemplo
- Configura la estructura de directorios necesaria
- Prepara el entorno para primer uso

### 5. Verificar Instalación
```bash
python run_downloader.py --help
```

## Uso Detallado 📖

### 🎬 Descarga de Videos

#### Preparación de URLs
1. **Edita tu archivo de URLs**:
   ```bash
   # El archivo ya existe después de ejecutar setup_environment.py
   notepad TikTokVault\data\tiktok_urls.txt    # Windows
   nano TikTokVault/data/tiktok_urls.txt       # Linux/Mac
   ```

2. **Formato del archivo de URLs**:
   ```txt
   # Mi Lista Personal de TikTok
   # Líneas que empiezan con # son comentarios
   
   https://www.tiktok.com/@username/video/1234567890123456789
   https://www.tiktok.com/@username/video/9876543210987654321
   
   # Organiza por categorías:
   # Videos de baile:
   https://www.tiktok.com/@dancer/video/1111111111111111111
   
   # Videos educativos:
   https://www.tiktok.com/@teacher/video/2222222222222222222
   ```

#### Métodos de Descarga

**Modo Interactivo (Recomendado para principiantes)**:
```bash
python run_downloader.py
```
- Interfaz de menú intuitiva
- Selección de archivos de URLs
- Guía paso a paso

**Modo Directo (Para usuarios avanzados)**:
```bash
# Usar archivo por defecto
python run_downloader.py

# Usar archivo específico
python run_downloader.py mi_lista_personalizada.txt

# Obtener ayuda
python run_downloader.py --help
```

### 🗄️ Gestión de Base de Datos

#### Visor Interactivo
```bash
python run_downloader.py db
```
Características del visor interactivo:
- Navegación por menús
- Búsqueda en tiempo real
- Filtros dinámicos
- Estadísticas visuales

#### Comandos Directos de Base de Datos

**Estadísticas Generales**:
```bash
python run_downloader.py db stats
```

**Videos Recientes**:
```bash
python run_downloader.py db recent           # Últimos 10 videos
python run_downloader.py db recent 25       # Últimos 25 videos
```

**Búsqueda de Videos**:
```bash
python run_downloader.py db search "baile"           # Buscar en título/descripción
python run_downloader.py db search "receta" creator  # Buscar solo en creadores
```

**Análisis por Creador**:
```bash
python run_downloader.py db creator username123
```

**Detalles de Video Específico**:
```bash
python run_downloader.py db video 7418920193847251205
```

## Sistema de Base de Datos 🗄️

### Arquitectura de Datos
El proyecto utiliza SQLite para proporcionar un sistema robusto de gestión de metadatos sin necesidad de configuración adicional de servidor.

#### Tabla `videos` - Información Principal
- **Identificación**: ID único de video, URL original
- **Contenido**: Título, descripción, duración, fecha de subida
- **Creador**: Username, nombre completo del creador
- **Métricas**: Vistas, likes, comentarios, shares
- **Archivos**: Rutas de video, thumbnail, tamaño de archivo
- **Metadatos**: Tags, calidad, datos JSON completos
- **Fechas**: Timestamp de descarga y procesamiento

#### Tabla `download_sessions` - Seguimiento de Sesiones
- **Sesión**: ID único, archivo fuente, timestamp
- **Resultados**: Videos exitosos vs fallidos
- **Estadísticas**: Tiempo total, tasa de éxito
- **Configuración**: Settings usados durante la descarga

### Capacidades de Búsqueda Avanzada

#### Tipos de Búsqueda Disponibles:
1. **Búsqueda Global**: En título, descripción y tags
2. **Por Creador**: Todos los videos de un usuario específico
3. **Por Fecha**: Videos de un período determinado
4. **Por Engagement**: Filtrar por número de vistas/likes
5. **Por Duración**: Videos cortos vs largos

#### Funciones de Análisis:
- **Estadísticas de Creadores**: Videos más populares por usuario
- **Tendencias de Contenido**: Análisis de tags y temas populares
- **Métricas de Engagement**: Promedios de vistas, likes, comentarios
- **Historial de Descargas**: Seguimiento temporal de actividad

### Comandos de Base de Datos Avanzados

```bash
# Estadísticas detalladas con top creadores
python run_downloader.py db stats

# Buscar videos por engagement mínimo (próximamente)
python run_downloader.py db search --min-views 100000

# Exportar datos a CSV (próximamente)
python run_downloader.py db export --format csv

# Análisis de sesiones de descarga
python run_downloader.py db sessions
```

## Formato de Archivo de URLs 📝

### Estructura Recomendada
Crea archivos `.txt` bien organizados en el directorio `TikTokVault/data/`:

```txt
# Mi Colección Personal de TikTok - Octubre 2024
# Líneas que empiezan con # son comentarios y se ignoran

# ===============================================
# VIDEOS EDUCATIVOS
# ===============================================
https://www.tiktok.com/@cooking_master/video/1234567890123456789
https://www.tiktok.com/@tech_tutorials/video/2345678901234567890
https://www.tiktok.com/@language_learning/video/3456789012345678901

# ===============================================
# CONTENIDO DE ENTRETENIMIENTO
# ===============================================
# Videos de baile y música:
https://www.tiktok.com/@dance_queen/video/4567890123456789012
https://www.tiktok.com/@musician_viral/video/5678901234567890123

# Comedia y memes:
https://www.tiktok.com/@comedy_central/video/6789012345678901234
https://www.tiktok.com/@meme_lord/video/7890123456789012345

# ===============================================
# CONTENIDO PROFESIONAL
# ===============================================
https://www.tiktok.com/@business_tips/video/8901234567890123456
https://www.tiktok.com/@career_advice/video/9012345678901234567
```

### Mejores Prácticas
- **Organización**: Usa comentarios para categorizar contenido
- **Validación**: Solo URLs que contengan 'tiktok.com' serán procesadas
- **Separación**: Una URL por línea, sin líneas vacías innecesarias
- **Documentación**: Incluye fechas y propósito de la colección

## Configuración Avanzada ⚙️

### Archivos de Configuración

#### `configs/config.ini` - Configuración Principal
```ini
[DOWNLOAD]
max_quality = 720p              # Calidad máxima: 480p, 720p, 1080p, best
download_thumbnails = true      # Descargar miniaturas
download_metadata = true        # Guardar metadatos JSON
organize_by_uploader = false    # Crear carpetas por creador

[OUTPUT]
filename_template = %(uploader)s_%(title)s_%(id)s.%(ext)s
date_subdirectories = false     # Organizar por fechas

[BEHAVIOR]
continue_on_error = true        # Continuar si un video falla
max_retries = 3                 # Intentos por video
download_delay = 1              # Pausa entre descargas (segundos)
```

#### `configs/database_config.ini` - Configuración de Base de Datos
```ini
[database]
database_file = tiktok_videos.db
enable_database = true
max_search_results = 50
default_recent_count = 10

[performance]
concurrent_downloads = 1        # Descargas simultáneas
retry_count = 3
timeout = 30

[logging]
log_level = INFO
log_to_file = true
log_retention_days = 30
```

### Personalización de Salida

#### Templates de Nombres de Archivo
Variables disponibles para `filename_template`:
- `%(uploader)s` - Nombre del creador
- `%(title)s` - Título del video
- `%(id)s` - ID único del video
- `%(ext)s` - Extensión del archivo
- `%(upload_date)s` - Fecha de subida
- `%(duration)s` - Duración del video

#### Ejemplos de Templates:
```ini
# Por defecto
filename_template = %(uploader)s_%(title)s_%(id)s.%(ext)s

# Organizado por fecha
filename_template = %(upload_date)s_%(uploader)s_%(title)s.%(ext)s

# Solo ID (para nombres cortos)
filename_template = %(id)s.%(ext)s

# Con duración
filename_template = %(uploader)s_%(duration)ss_%(title)s.%(ext)s
```

## Archivos de Salida 📂

### Estructura de Archivos Generados

#### Directorio de Videos (`TikTokVault/outputs/videos/`)
```
TikTokVault/outputs/videos/
├── cooking_master_Receta de pasta italiana en 60 segundos_7418920193847251205.mp4
├── cooking_master_Receta de pasta italiana en 60 segundos_7418920193847251205.jpg
├── dance_queen_Tutorial de baile viral #fyp_7419820193847251206.mp4
├── dance_queen_Tutorial de baile viral #fyp_7419820193847251206.jpg
└── comedy_king_Reacción épica a meme de gatos_7420820193847251207.mp4
```

**Convención de Nombres**:
- `{creador}_{titulo}_{video_id}.{extension}`
- Caracteres especiales reemplazados por guiones bajos
- Nombres truncados si son muy largos

#### Directorio de Metadatos (`TikTokVault/outputs/metadata/`)
```
TikTokVault/outputs/metadata/
├── cooking_master_Receta de pasta italiana_7418920193847251205.info.json
├── dance_queen_Tutorial de baile viral_7419820193847251206.info.json
└── comedy_king_Reacción épica_7420820193847251207.info.json
```

**Contenido de Metadatos JSON**:
```json
{
  "id": "7418920193847251205",
  "title": "Receta de pasta italiana en 60 segundos",
  "description": "Aprende a hacer pasta deliciosa...",
  "uploader": "cooking_master",
  "uploader_id": "cooking_master",
  "upload_date": "20241025",
  "duration": 58,
  "view_count": 156789,
  "like_count": 12456,
  "comment_count": 234,
  "share_count": 89,
  "tags": ["receta", "pasta", "cocina", "italiano"],
  "webpage_url": "https://www.tiktok.com/@cooking_master/video/7418920193847251205"
}
```

#### Directorio de Logs (`TikTokVault/outputs/logs/`)
```
TikTokVault/outputs/logs/
├── app.log                                      # Log general de aplicación
├── download_log_20241027_143052.json          # Sesión de descarga específica
└── download_log_20241027_151234.json          # Otra sesión
```

**Ejemplo de Log de Sesión**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "start_time": "2024-10-27T14:30:52",
  "end_time": "2024-10-27T14:35:18",
  "source_file": "tiktok_urls.txt",
  "total_urls": 8,
  "successful_downloads": 6,
  "failed_downloads": 2,
  "success_rate": 75.0,
  "total_size_mb": 156.7,
  "failed_videos": [
    {
      "url": "https://www.tiktok.com/@private_user/video/1234567890",
      "error": "Video is private",
      "timestamp": "2024-10-27T14:32:15"
    }
  ]
}
```

#### Base de Datos (`TikTokVault/outputs/tiktok_videos.db`)
- **Formato**: SQLite 3 compatible con cualquier cliente SQLite
- **Tamaño**: Típicamente 1-5 MB por cada 100 videos
- **Backup**: Se recomienda hacer copias periódicas

## 🔒 Gestión de Archivos y Privacidad

### Archivos Privados (No Versionados)
Estos archivos contienen tu información personal y **NUNCA** se suben al repositorio:

```
TikTokVault/
├── data/
│   └── tiktok_urls.txt              # ❌ Tu lista personal de URLs
├── outputs/
│   ├── videos/                      # ❌ Videos descargados
│   │   ├── *.mp4, *.mov            # ❌ Archivos de video
│   │   └── *.jpg, *.png            # ❌ Miniaturas
│   ├── logs/                        # ❌ Registros personales
│   │   ├── app.log                 # ❌ Log de aplicación
│   │   └── download_log_*.json     # ❌ Logs de sesiones
│   ├── metadata/                    # ❌ Metadatos de videos
│   │   └── *.info.json             # ❌ Información de videos
│   └── tiktok_videos.db            # ❌ Tu base de datos personal
```

### Archivos del Proyecto (Versionados)
Estos archivos forman parte del código y **SÍ** se incluyen en el repositorio:

```
TikTok_Downloader/
├── configs/                         # ✅ Configuraciones por defecto
│   ├── config.ini                  # ✅ Configuración ejemplo
│   └── database_config.ini         # ✅ Configuración de BD
├── TikTokVault/
│   ├── data/
│   │   ├── tiktok_urls.example.txt # ✅ Archivo de ejemplo
│   │   └── .gitkeep                # ✅ Mantiene estructura
│   ├── outputs/
│   │   ├── videos/.gitkeep         # ✅ Mantiene estructura
│   │   ├── logs/.gitkeep           # ✅ Mantiene estructura
│   │   └── metadata/.gitkeep       # ✅ Mantiene estructura
│   └── src/                        # ✅ Código fuente
│       ├── TikTokDL.py            # ✅ Motor principal
│       ├── database.py            # ✅ Gestor de BD
│       └── db_viewer.py           # ✅ Visor de BD
├── run_downloader.py               # ✅ Punto de entrada
├── setup_environment.py           # ✅ Script de configuración
├── requirements.txt                # ✅ Dependencias
├── README.md                       # ✅ Documentación
├── DATABASE_FEATURES.md            # ✅ Docs de BD
└── COPYING                         # ✅ Licencia
```

### Configuración Inicial Segura
```bash
# 1. Ejecutar script de configuración automática
python setup_environment.py

# 2. El script creará automáticamente:
#    - TikTokVault/data/tiktok_urls.txt (desde el ejemplo)
#    - Estructura de directorios necesaria
#    - Archivos .gitkeep para mantener estructura

# 3. Editar tu archivo personal de URLs
notepad TikTokVault\data\tiktok_urls.txt    # Windows
nano TikTokVault/data/tiktok_urls.txt       # Linux/Mac

# 4. Tus URLs reales NUNCA se subirán al repositorio
```

### Protección de Privacidad
- **`.gitignore`** configurado para excluir todos los archivos personales
- **Separación clara** entre código y datos personales
- **Ejemplo incluido** para guiar sin exponer información real
- **Documentación** sobre qué archivos son seguros de compartir

## Ejemplos Prácticos 🎯

### Sesión de Descarga Típica
```bash
🚀 Iniciando TikTok Downloader...
� Directorio de salida: TikTokVault/outputs/videos
🗄️ Base de datos: TikTokVault/outputs/tiktok_videos.db

📋 Archivo seleccionado: tiktok_urls.txt (8 URLs encontradas)

Descargando videos: 75%|███████▌  | 6/8 [02:15<00:45, 12.3s/video]
✅ @chef_master: "Receta de pasta italiana en 60 segundos"
✅ @dance_queen: "Tutorial de baile viral #fyp"
⚠️  @tech_guru: Video privado - omitido
✅ @comedy_king: "Reacción épica a meme de gatos"

==================================================
📊 RESUMEN DE SESIÓN DE DESCARGA
==================================================
🎬 Total procesados: 8 videos
✅ Exitosos: 6 videos (75.0%)
❌ Fallidos: 2 videos
� Tamaño descargado: 156.7 MB
⏱️  Tiempo total: 3m 42s

📈 ESTADÍSTICAS ACTUALIZADAS:
🗄️ Videos en base de datos: 23 (+6 nuevos)
👤 Creadores únicos: 12
📊 Tasa de éxito histórica: 82.6%
```

### Ejemplos de Consultas de Base de Datos

#### Estadísticas Generales
```bash
$ python run_downloader.py db stats

📊 ESTADÍSTICAS DE BASE DE DATOS
================================
🎬 Total de Videos: 47
👤 Creadores Únicos: 15
💾 Tamaño Total: 892.4 MB
📅 Primer Video: 2024-10-15
📅 Último Video: 2024-10-27

🏆 TOP 5 CREADORES:
1. @cooking_master    12 videos  (187.3 MB)
2. @dance_tutorials    8 videos  (142.1 MB)
3. @comedy_central     6 videos   (95.7 MB)
4. @tech_reviews       5 videos  (134.8 MB)
5. @life_hacks         4 videos   (78.2 MB)

📈 ENGAGEMENT PROMEDIO:
👀 Vistas: 245,673
❤️  Likes: 18,542
💬 Comentarios: 1,234
🔄 Shares: 892
```

#### Búsqueda de Contenido
```bash
$ python run_downloader.py db search "receta"

🔍 RESULTADOS DE BÚSQUEDA: "receta"
===================================
📹 Encontrados: 4 videos

1. 📱 Receta de pizza en 5 minutos
   👤 @cooking_master | 👀 156,789 | ❤️ 12,456
   📅 2024-10-25 | ⏱️ 0:58 | 💾 15.2 MB

2. 📱 Receta secreta de brownies
   👤 @sweet_baker | 👀 89,123 | ❤️ 7,890
   📅 2024-10-22 | ⏱️ 1:24 | 💾 18.7 MB

3. 📱 Receta saludable de smoothie verde
   👤 @healthy_life | 👀 45,678 | ❤️ 3,456
   📅 2024-10-20 | ⏱️ 0:45 | 💾 12.1 MB
```

#### Análisis por Creador
```bash
$ python run_downloader.py db creator cooking_master

👤 PERFIL DEL CREADOR: @cooking_master
=====================================
📹 Total de Videos: 12
📊 Engagement Total: 1,847,392 vistas
💾 Tamaño Total: 187.3 MB
📅 Primer Video: 2024-10-16
📅 Último Video: 2024-10-26

🔥 VIDEO MÁS POPULAR:
"Pasta italiana en 60 segundos"
👀 234,567 vistas | ❤️ 18,934 likes

📈 ESTADÍSTICAS:
Promedio de vistas: 153,949
Promedio de likes: 11,234
Duración promedio: 1:08
```

## Solución de Problemas 🔧

### Problemas de Instalación

#### Error: "No module named 'yt_dlp'"
```bash
# Solución: Instalar dependencias
pip install -r requirements.txt

# Si persiste, actualizar pip
python -m pip install --upgrade pip
pip install --upgrade yt-dlp
```

#### Error: "Python no reconocido"
```bash
# Windows: Asegúrate de que Python esté en PATH
# O usa:
py -3 run_downloader.py

# Linux/Mac: Usar python3
python3 run_downloader.py
```

### Problemas de Descarga

#### "No se encontraron URLs válidas"
```bash
# Verificar:
1. El archivo existe en TikTokVault/data/
2. Las URLs contienen 'tiktok.com'
3. El formato del archivo es correcto
4. No hay líneas vacías entre URLs

# Ejemplo de formato correcto:
https://www.tiktok.com/@user/video/1234567890123456789
https://www.tiktok.com/@user/video/9876543210987654321
```

#### "Descargas constantemente fallando"
```bash
# Causas comunes:
1. Videos privados o eliminados
2. Restricciones geográficas
3. Conexión de internet inestable
4. yt-dlp desactualizado

# Soluciones:
pip install --upgrade yt-dlp
python run_downloader.py --help  # Verificar funcionamiento básico
```

#### "Error de permisos en Windows"
```bash
# Ejecutar como administrador
# O cambiar permisos de la carpeta
icacls "f:\Code\TikTok_Downloader" /grant Users:(OI)(CI)F
```

### Problemas de Base de Datos

#### "Database is locked"
```bash
# Cerrar todas las instancias del programa
# Eliminar archivo de lock si existe
del TikTokVault\outputs\tiktok_videos.db-wal
del TikTokVault\outputs\tiktok_videos.db-shm
```

#### "Datos corruptos en base de datos"
```bash
# Hacer backup y recrear
copy TikTokVault\outputs\tiktok_videos.db TikTokVault\outputs\backup.db
del TikTokVault\outputs\tiktok_videos.db
python run_downloader.py  # Recreará la base de datos
```

### Problemas de Espacio

#### "Disco lleno"
```bash
# Verificar espacio disponible
dir TikTokVault\outputs\videos

# Limpiar archivos antiguos
python run_downloader.py db stats  # Ver tamaño total
# Eliminar videos manualmente si es necesario
```

### Diagnóstico y Logs

#### Habilitar Logging Detallado
```bash
# Editar configs/database_config.ini
[logging]
log_level = DEBUG
log_to_file = true

# Los logs se guardan en:
TikTokVault/outputs/logs/app.log
```

#### Archivos de Log Útiles
```bash
# Log de aplicación
type TikTokVault\outputs\logs\app.log

# Logs de descarga (JSON)
type TikTokVault\outputs\logs\download_log_*.json
```

### Obtener Ayuda

#### Información del Sistema
```bash
python --version
pip list | findstr "yt-dlp\|tqdm\|colorama"
python run_downloader.py --help
```

#### Reportar Problemas
Al reportar un problema, incluye:
1. Versión de Python
2. Sistema operativo
3. Comando ejecutado
4. Mensaje de error completo
5. Archivo de log relevante

## Contribuir al Proyecto 🤝

### Guía de Contribución

#### 1. Configuración del Entorno de Desarrollo
```bash
# Fork y clonar el repositorio
git clone https://github.com/tu-usuario/TikTok_Downloader.git
cd TikTok_Downloader

# Crear rama de desarrollo
git checkout -b feature/nueva-funcionalidad

# Configurar entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias de desarrollo
pip install -r requirements.txt
pip install pytest black flake8  # Herramientas de desarrollo
```

#### 2. Estándares de Código
```bash
# Formateo de código
black TikTokVault/src/

# Verificación de estilo
flake8 TikTokVault/src/

# Ejecutar tests (cuando estén disponibles)
pytest tests/
```

#### 3. Áreas de Contribución Prioritarias

**🌟 Funcionalidades de Alta Prioridad**:
- 🌐 **Interfaz Web**: Dashboard con Flask/FastAPI
- 📊 **Analytics Avanzados**: Gráficas y estadísticas visuales
- 📱 **API REST**: Endpoints para integración externa
- 🔄 **Sincronización**: Backup automático a servicios de nube
- 🔍 **Búsqueda Avanzada**: Filtros complejos y facetados

**📈 Mejoras de Rendimiento**:
- ⚡ **Descarga Paralela**: Implementación segura de concurrencia
- 🗜️ **Compresión**: Optimización de almacenamiento
- 📦 **Caching**: Sistema de cache inteligente
- 🔄 **Streaming**: Descarga progresiva para videos grandes

**🎨 Experiencia de Usuario**:
- 🖥️ **GUI**: Interfaz gráfica con tkinter/PyQt
- 📋 **Gestión de Listas**: CRUD para colecciones de URLs
- 🏷️ **Etiquetado**: Sistema de tags automático y manual
- 📊 **Reportes**: Exportación a PDF/Excel

#### 4. Proceso de Pull Request
```bash
# Asegurar que todo funciona correctamente
python run_downloader.py --help
python run_downloader.py db stats

# Verificar estilo de código
black --check TikTokVault/src/
flake8 TikTokVault/src/

# Commit con mensaje descriptivo siguiendo convenciones
git add .
git commit -m "feat: agregar funcionalidad de exportación CSV

- Implementa comando 'db export --format csv'
- Incluye filtros por fecha y creador
- Añade documentación y tests
- Fixes #123"

# Push y crear PR
git push origin feature/nueva-funcionalidad
```

### Roadmap de Desarrollo 🗺️

#### 🎯 Versión 2.0 (Q1 2025)
- [ ] **Interfaz Web Básica** - Dashboard con estadísticas principales
- [ ] **API REST** - Endpoints para operaciones CRUD
- [ ] **Exportación de Datos** - CSV, JSON, Excel con filtros
- [ ] **Filtros Avanzados** - Búsqueda por múltiples criterios
- [ ] **Sistema de Backup** - Respaldo automático de base de datos

#### 🚀 Versión 2.5 (Q2 2025)
- [ ] **Analytics Dashboard** - Gráficas interactivas con Chart.js
- [ ] **Integración Cloud** - Google Drive, Dropbox, OneDrive
- [ ] **Notificaciones** - Push notifications y email alerts
- [ ] **Audio Extraction** - Extracción de bandas sonoras
- [ ] **Content Recognition** - Detección automática de categorías

#### 🌟 Versión 3.0 (Q3 2025)
- [ ] **Machine Learning** - Recomendaciones basadas en historial
- [ ] **Trend Analysis** - Análisis de tendencias y viralidad
- [ ] **Social Integration** - Conexión con otras redes sociales
- [ ] **Mobile App** - App companion para Android/iOS
- [ ] **Multi-user Support** - Colaboración y perfiles múltiples

### Contribuciones Específicas Buscadas

#### 🛠️ Desarrolladores Backend
- Optimización de consultas SQL
- Implementación de API REST
- Sistema de autenticación y autorización
- Microservicios y containerización

#### 🎨 Desarrolladores Frontend
- Interfaz web responsiva
- Dashboard de analytics interactivo
- UX/UI design para herramientas CLI
- Mobile-first design

#### 📊 Data Scientists
- Algoritmos de análisis de tendencias
- Modelos de recomendación
- Análisis de engagement
- Predicción de viralidad

#### 🧪 QA y Testing
- Test suites automatizados
- Testing de integración
- Performance testing
- Security testing

### Recursos para Contribuidores

#### Documentación Técnica
- [DATABASE_FEATURES.md](DATABASE_FEATURES.md) - Arquitectura de base de datos
- [API_DOCUMENTATION.md](docs/api.md) - Especificación de API (próximamente)
- [ARCHITECTURE.md](docs/architecture.md) - Arquitectura del sistema (próximamente)

#### Enlaces Útiles
- [Issues Abiertos](https://github.com/AlfredoCCA/TikTok_Downloader/issues)
- [Discusiones](https://github.com/AlfredoCCA/TikTok_Downloader/discussions)
- [Project Board](https://github.com/AlfredoCCA/TikTok_Downloader/projects)
- [Wiki](https://github.com/AlfredoCCA/TikTok_Downloader/wiki)

## Aviso Legal ⚖️

### Responsabilidad Legal y Ética

#### ⚖️ Cumplimiento Legal
- **Derechos de Autor**: Solo descarga contenido con permiso del creador
- **Términos de Servicio**: Cumple con los ToS de TikTok en todo momento
- **Uso Justo**: Respeta las leyes de uso justo de tu jurisdicción
- **Privacidad**: No recolectes información personal sin consentimiento
- **GPL v3**: Este software está bajo GPL v3, no MIT como otras herramientas

#### 🎯 Uso Recomendado
```txt
✅ USOS APROPIADOS:
- Backup personal de contenido propio
- Investigación académica con permiso
- Archivo de contenido con consentimiento del creador
- Análisis de datos con fines educativos
- Modificación y redistribución bajo GPL v3

❌ USOS INAPROPIADOS:
- Descarga masiva sin permiso
- Redistribución comercial sin cumplir GPL v3
- Violación de derechos de autor
- Scraping agresivo que impacte la plataforma
- Integración en software propietario sin GPL v3
```

#### 🛡️ Limitaciones de Responsabilidad
- **Uso Personal**: Esta herramienta está destinada para uso personal y educativo
- **Sin Garantías**: Software proporcionado "tal como está" según GPL v3
- **Responsabilidad del Usuario**: Los usuarios son responsables del uso ético de la herramienta
- **Cumplimiento Legal**: Usuarios deben cumplir con las leyes locales y ToS de plataformas
- **Copyleft**: Modificaciones deben mantenerse bajo GPL v3 o compatible

## Características Técnicas �

### Arquitectura del Sistema
- **Lenguaje**: Python 3.8+
- **Base de Datos**: SQLite 3 (sin servidor requerido)
- **Descarga**: yt-dlp (fork mantenido de youtube-dl)
- **Interfaz**: CLI con soporte de colores multiplataforma
- **Configuración**: Archivos INI con validación

### Dependencias Principales
```python
# Core - Descarga y procesamiento
yt-dlp>=2023.10.13          # Motor de descarga principal
requests>=2.31.0            # Peticiones HTTP
urllib3>=2.0.0              # Conexiones web

# UI y Progreso
tqdm>=4.65.0                # Barras de progreso
colorama>=0.4.6             # Colores multiplataforma

# Manejo de Datos
python-dateutil>=2.8.2     # Parsing de fechas
pathlib2>=2.3.7            # Manejo de rutas

# Configuración
configparser>=5.3.0        # Lectura de archivos INI
python-dotenv>=1.0.0       # Variables de entorno

# Opcional - Características avanzadas
ffmpeg-python>=0.2.0       # Procesamiento de video
Pillow>=10.0.0             # Manipulación de imágenes
```

### Estructura de Base de Datos

#### Schema Principal
```sql
-- Tabla de videos principales
CREATE TABLE videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT UNIQUE NOT NULL,
    url TEXT NOT NULL,
    title TEXT,
    description TEXT,
    creator_username TEXT,
    creator_display_name TEXT,
    duration INTEGER,
    view_count INTEGER,
    like_count INTEGER,
    comment_count INTEGER,
    share_count INTEGER,
    upload_date TEXT,
    download_date TEXT DEFAULT CURRENT_TIMESTAMP,
    file_path TEXT,
    thumbnail_path TEXT,
    file_size INTEGER,
    video_quality TEXT,
    session_id TEXT,
    metadata_json TEXT
);

-- Tabla de sesiones de descarga
CREATE TABLE download_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT UNIQUE NOT NULL,
    source_file TEXT,
    start_time TEXT,
    end_time TEXT,
    total_urls INTEGER,
    successful_downloads INTEGER,
    failed_downloads INTEGER,
    total_size INTEGER
);
```

### Funcionalidades Avanzadas

#### Sistema de Sesiones
- Cada ejecución genera un UUID único de sesión
- Tracking completo de estadísticas por sesión
- Análisis histórico de tasas de éxito

#### Prevención de Duplicados
- Verificación por ID único de TikTok
- Base de datos como fuente de verdad
- Omisión automática de videos ya descargados

#### Manejo de Errores Robusto
- Continuación automática en fallos individuales
- Logging detallado de errores
- Reintentos configurables

#### Optimización de Rendimiento
- Descarga secuencial para evitar rate limiting
- Configuración de delays personalizables
- Compresión automática de metadatos JSON

## Licencia 📄

**GNU General Public License v3** - Este proyecto está bajo la licencia GPL v3. Ver [COPYING](COPYING) para detalles completos.

#### Derechos Otorgados por GPL v3
- ✅ **Uso Personal**: Sin restricciones para uso personal
- ✅ **Modificación**: Libre modificación del código fuente
- ✅ **Distribución**: Distribución libre con código fuente incluido
- ✅ **Uso Comercial**: Permitido bajo las condiciones de GPL v3
- ✅ **Convivencia**: Compatibilidad con otras licencias GPL

#### Obligaciones bajo GPL v3
- 📄 **Incluir Licencia**: Incluir texto completo de GPL v3 en distribuciones
- 🔓 **Código Fuente**: Proporcionar código fuente en distribuciones
- 🔗 **Copyleft**: Obras derivadas deben usar GPL v3 o compatible
- 📝 **Cambios Documentados**: Marcar claramente las modificaciones realizadas
- ⚖️ **Mismos Términos**: Redistribuir bajo los mismos términos de GPL v3

## Agradecimientos 👏

#### Proyectos Fundamentales
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Motor de descarga extraordinario y mantenido activamente
- **[tqdm](https://github.com/tqdm/tqdm)** - Barras de progreso elegantes y informativas
- **[colorama](https://github.com/tartley/colorama)** - Colores multiplataforma para mejor UX
- **[SQLite](https://www.sqlite.org/)** - Base de datos robusta, liviana y sin configuración
- **[Python](https://www.python.org/)** - Lenguaje de programación poderoso y versátil

#### Comunidades que Inspiran
- **Creadores de TikTok** - Por el contenido increíble y la creatividad sin límites
- **Comunidad Python** - Por las herramientas excepcionales y el apoyo constante
- **Open Source Community** - Por hacer posible el desarrollo colaborativo
- **Contributors & Users** - Por el feedback valioso, testing y mejoras continuas

#### Menciones Especiales
- **Desarrolladores de yt-dlp** - Por mantener viva y actualizada la funcionalidad de descarga
- **SQLite Team** - Por crear una base de datos que simplemente funciona
- **GitHub** - Por proporcionar la plataforma que hace posible la colaboración
- **Stack Overflow** - Por resolver incontables dudas técnicas de la comunidad

---

## Estado del Proyecto 📊

### Badges Técnicas

[![yt-dlp](https://img.shields.io/badge/yt--dlp-2023.10.13+-red?style=flat-square&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![tqdm](https://img.shields.io/badge/tqdm-4.65.0+-blue?style=flat-square)](https://github.com/tqdm/tqdm)
[![colorama](https://img.shields.io/badge/colorama-0.4.6+-yellow?style=flat-square)](https://github.com/tartley/colorama)
[![requests](https://img.shields.io/badge/requests-2.31.0+-green?style=flat-square)](https://docs.python-requests.org/)

[![CLI Tool](https://img.shields.io/badge/Type-CLI%20Tool-purple?style=flat-square&logo=terminal)](https://github.com/AlfredoCCA/TikTok_Downloader)
[![Batch Processing](https://img.shields.io/badge/Feature-Batch%20Processing-orange?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader)
[![Metadata](https://img.shields.io/badge/Feature-Metadata%20Extraction-lightblue?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader)
[![Analytics](https://img.shields.io/badge/Feature-Analytics%20Dashboard-cyan?style=flat-square)](https://github.com/AlfredoCCA/TikTok_Downloader)

### Estadísticas de Desarrollo
- **Líneas de Código**: ~2,000+ líneas
- **Archivos**: 15+ archivos fuente  
- **Funcionalidades**: 25+ características implementadas
- **Comandos CLI**: 10+ comandos disponibles
- **Tipos de Archivo**: 8+ formatos soportados

### Métricas de Calidad
- **Cobertura de Documentación**: 95%+
- **Ejemplos Incluidos**: 20+ ejemplos prácticos
- **Configuraciones**: 15+ opciones configurables
- **Comandos de Ayuda**: 100% documentados
- **Error Handling**: Robusto y detallado

---

## Enlaces de Referencia Rápida 🔗

### 📚 Documentación
- [Características de Base de Datos](DATABASE_FEATURES.md)
- [Script de Configuración](setup_environment.py)
- [Archivo de Configuración Principal](configs/config.ini)
- [Configuración de Base de Datos](configs/database_config.ini)

### 🐛 Soporte y Ayuda
- [Reportar un Bug](https://github.com/AlfredoCCA/TikTok_Downloader/issues/new?template=bug_report.md)
- [Solicitar una Función](https://github.com/AlfredoCCA/TikTok_Downloader/issues/new?template=feature_request.md)
- [Hacer una Pregunta](https://github.com/AlfredoCCA/TikTok_Downloader/discussions)
- [Ver Issues Abiertos](https://github.com/AlfredoCCA/TikTok_Downloader/issues)

### 🤝 Participación
- [Guía de Contribución](CONTRIBUTING.md) (próximamente)
- [Código de Conducta](CODE_OF_CONDUCT.md) (próximamente)
- [Discussions](https://github.com/AlfredoCCA/TikTok_Downloader/discussions)
- [Project Board](https://github.com/AlfredoCCA/TikTok_Downloader/projects)

### 📖 Recursos Adicionales
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python Documentation](https://docs.python.org/3/)
- [TikTok Terms of Service](https://www.tiktok.com/legal/terms-of-service)

---

## 🎉 ¡Gracias por Usar TikTok Downloader!

**Desarrollado con ❤️ para la comunidad de TikTok**

*Este proyecto se mantiene activamente y está abierto a contribuciones de la comunidad. ¡Esperamos tus ideas y mejoras!*

### Información del Proyecto
- **Última Actualización**: Octubre 27, 2024
- **Versión**: 1.5.0  
- **Autor**: [AlfredoCCA](https://github.com/AlfredoCCA)
- **Repositorio**: [TikTok_Downloader](https://github.com/AlfredoCCA/TikTok_Downloader)

**¡Felices Descargas! 🎬✨**
