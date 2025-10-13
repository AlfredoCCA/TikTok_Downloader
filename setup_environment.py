#!/usr/bin/env python3
"""
Setup Script for TikTok Downloader
Configures the environment for first-time users
"""

import os
import shutil
from pathlib import Path


def setup_environment():
    """Set up the development environment"""
    print("🚀 Setting up TikTok Downloader environment...")

    base_dir = Path(__file__).parent
    data_dir = base_dir / "TikTokVault" / "data"

    # Check if tiktok_urls.txt already exists
    urls_file = data_dir / "tiktok_urls.txt"
    example_file = data_dir / "tiktok_urls.example.txt"

    if not urls_file.exists() and example_file.exists():
        print("📋 Creating your personal URLs file from example...")
        shutil.copy(example_file, urls_file)
        print(f"✅ Created: {urls_file}")
        print(f"📝 Edit {urls_file} to add your TikTok URLs")
    elif urls_file.exists():
        print(f"📋 URLs file already exists: {urls_file}")
    else:
        print(f"❌ Example file not found: {example_file}")
        return False

    # Create .gitkeep files if they don't exist
    output_dirs = [
        "TikTokVault/outputs/videos",
        "TikTokVault/outputs/logs",
        "TikTokVault/outputs/metadata",
    ]

    for dir_path in output_dirs:
        full_path = base_dir / dir_path
        gitkeep_file = full_path / ".gitkeep"

        if not gitkeep_file.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            gitkeep_file.write_text(f"# Keep {dir_path} directory structure")
            print(f"✅ Created: {gitkeep_file}")

    print("\n🎉 Environment setup complete!")
    print("\n📋 Next steps:")
    print(f"1. Edit {urls_file} and add your TikTok URLs")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Run the downloader: python run_downloader.py")
    print("\n🔒 Your personal URLs file will not be committed to git!")

    return True


if __name__ == "__main__":
    try:
        setup_environment()
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        exit(1)
