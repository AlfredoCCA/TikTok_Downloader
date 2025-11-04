# Importar bibliotecas
import yt_dlp

# URL del video 
url = "https://www.tiktok.com/@usuario/video/1234567890"

# Descarga el video
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([url])

print("✅ ¡Descarga completa!")

