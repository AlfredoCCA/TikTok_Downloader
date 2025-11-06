#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para descargar videos con yt-dlp
Sin interacción del usuario - solo cambiar la URL y ejecutar
"""

import yt_dlp
import os

# ===============================
# CONFIGURACIÓN (CAMBIAR AQUÍ)
# ===============================

# URL del video a descargar
URL_VIDEO = "https://www.tiktok.com/@usuario/video/1234567890"

# Carpeta donde guardar el video
CARPETA_DESCARGA = "videos_descargados"

# ===============================
# PROCESO DE DESCARGA
# ===============================

def descargar_video():
    """Descarga el video de forma automática"""
    
    # Crear carpeta si no existe
    if not os.path.exists(CARPETA_DESCARGA):
        os.makedirs(CARPETA_DESCARGA)
    
    # Configuración de descarga
    opciones = {
        'outtmpl': f'{CARPETA_DESCARGA}/%(title)s.%(ext)s',  # Nombre del archivo
        'format': 'best',  # Mejor calidad disponible
    }
    
    try:
        # Realizar descarga
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([URL_VIDEO])
        
        print("✅ ¡Descarga completa!")
        return True
        
    except Exception as e:
        print(f"❌ Error en la descarga: {str(e)}")
        return False

# Ejecutar descarga
if __name__ == "__main__":
    descargar_video()