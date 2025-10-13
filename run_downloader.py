#!/usr/bin/env python3

"""
TikTok Downloader - Main entry point
Run this script to start downloading TikTok videos or view database
"""

import os
import sys
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "TikTokVault" / "src"
sys.path.insert(0, str(src_path))


def show_help():
    """Show help information"""
    print("🎬 TikTok Downloader - Usage:")
    print("\nDOWNLOAD VIDEOS:")
    print("  python run_downloader.py                    # Interactive mode")
    print("  python run_downloader.py <filename>         # Download from specific file")
    print("\nVIEW DATABASE:")
    print("  python run_downloader.py db                 # Interactive database viewer")
    print("  python run_downloader.py db stats           # Show statistics")
    print("  python run_downloader.py db recent [N]      # Show N recent videos")
    print("  python run_downloader.py db search <query>  # Search videos")
    print("  python run_downloader.py db creator <name>  # Show creator's videos")
    print("  python run_downloader.py db video <id>      # Show video details")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
            show_help()
        elif len(sys.argv) > 1 and sys.argv[1] == "db":
            # Database viewer mode
            from db_viewer import main as db_main

            # Remove 'db' from args and pass the rest
            sys.argv = [sys.argv[0]] + sys.argv[2:]
            db_main()
        else:
            # Download mode
            from TikTokDL import main

            main()
    except ImportError as e:
        print(f"❌ Error importing modules: {e}")
        print(
            "Make sure all dependencies are installed: pip install -r requirements.txt"
        )
    except Exception as e:
        print(f"💥 Error: {e}")
