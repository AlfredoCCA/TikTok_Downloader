#!/usr/bin/env python3
"""
TikTok Downloader - Quick Run Script
Usage: python run_downloader.py [filename.txt]
"""

import sys
import os
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "TikTokVault" / "src"
sys.path.insert(0, str(src_path))

# Import and run the downloader
try:
    from TikTokDL import main
    main()
except ImportError as e:
    print(f"❌ Error importing TikTokDL: {e}")
    print("Make sure all dependencies are installed: pip install -r requirements.txt")
except Exception as e:
    print(f"💥 Error: {e}")