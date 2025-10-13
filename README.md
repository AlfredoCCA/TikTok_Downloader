# TikTok Downloader 🎬

A powerful and easy-to-use TikTok video downloader that can process multiple URLs from text files and organize downloads efficiently.

## Features ✨

- **Batch Download**: Download multiple TikTok videos from a list of URLs
- **Organized Output**: Automatically organizes videos, metadata, and logs
- **Progress Tracking**: Real-time progress bars and colored output
- **Error Handling**: Continues downloading even if some videos fail
- **Metadata Extraction**: Saves video information and thumbnails
- **Flexible Input**: Load URLs from any .txt file in the data directory
- **Detailed Logging**: Comprehensive download logs with timestamps

## Project Structure 📁

```
TikTok_Downloader/
├── TikTokVault/
│   ├── data/                    # Input files (URL lists)
│   │   └── tiktok_urls.txt     # Default URL file
│   ├── outputs/                 # Downloaded content
│   │   ├── videos/             # Video files (.mp4, .mov, etc.)
│   │   ├── logs/               # Download logs (.json)
│   │   └── metadata/           # Video info & thumbnails
│   └── src/
│       └── TikTokDL.py         # Main downloader script
├── configs/
│   └── config.ini              # Configuration settings
├── requirements.txt            # Python dependencies
├── run_downloader.py          # Quick run script
└── README.md                  # This file
```

## Installation 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/TikTok_Downloader.git
   cd TikTok_Downloader
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python run_downloader.py
   ```

## Usage 📖

### Method 1: Interactive Mode (Recommended for beginners)

1. **Add TikTok URLs to a file:**
   - Create or edit `TikTokVault/data/tiktok_urls.txt`
   - Add one TikTok URL per line:
   ```
   https://www.tiktok.com/@username/video/1234567890123456789
   https://www.tiktok.com/@username/video/9876543210987654321
   # You can add comments with #
   ```

2. **Run the downloader:**
   ```bash
   python run_downloader.py
   ```

3. **Select your URL file and watch the magic happen! ✨**

### Method 2: Batch Mode (For advanced users)

```bash
# Use default file (tiktok_urls.txt)
python run_downloader.py

# Use specific file
python run_downloader.py my_custom_urls.txt
```

### Method 3: Direct Script Execution

```bash
cd TikTokVault/src
python TikTokDL.py
```

## URL File Format 📝

Create `.txt` files in the `TikTokVault/data/` directory:

```txt
# My TikTok Collection
# Lines starting with # are comments

https://www.tiktok.com/@user1/video/1234567890123456789
https://www.tiktok.com/@user2/video/9876543210987654321

# You can organize URLs with comments
# Funny videos:
https://www.tiktok.com/@comedian/video/1111111111111111111

# Tutorial videos:
https://www.tiktok.com/@teacher/video/2222222222222222222
```

## Configuration ⚙️

Edit `configs/config.ini` to customize:

- **Video Quality**: Set maximum download quality
- **File Organization**: Choose naming patterns
- **Download Behavior**: Set retries, delays, error handling
- **Output Options**: Enable/disable thumbnails, metadata

## Output Files 📂

After downloading, you'll find:

### Videos Directory (`TikTokVault/outputs/videos/`)
- **Video files**: `username_video-title_video-id.mp4`
- **Thumbnails**: `username_video-title_video-id.jpg`

### Logs Directory (`TikTokVault/outputs/logs/`)
- **Download logs**: `download_log_YYYYMMDD_HHMMSS.json`
- Contains success/failure statistics and detailed results

### Metadata Directory (`TikTokVault/outputs/metadata/`)
- **Video info**: `.info.json` files with complete video metadata
- **Descriptions**: Video titles, descriptions, upload dates

## Example Output 🎯

```
🚀 Starting download of 5 videos...
📁 Videos will be saved to: TikTokVault/outputs/videos

Downloading videos: 60%|██████    | 3/5 [00:45<00:30, 15.2s/video]
✅ Downloaded: Amazing Dance Video by @dancer123

==================================================
📊 DOWNLOAD SUMMARY
==================================================
✅ Successful: 4/5
❌ Failed: 1/5  
📈 Success Rate: 80.0%

🎉 Successfully downloaded videos:
  • Amazing Dance Video... by @dancer123
  • Cooking Tutorial... by @chef_master
  • Cat Compilation... by @funny_pets
  • DIY Project... by @crafty_creator
```

## Troubleshooting 🔧

### Common Issues:

1. **"No module named 'yt_dlp'"**
   ```bash
   pip install -r requirements.txt
   ```

2. **"No URLs found"**
   - Check that your `.txt` file is in `TikTokVault/data/`
   - Ensure URLs contain 'tiktok.com'
   - Remove empty lines or fix formatting

3. **Downloads failing**
   - Some TikTok videos may be private or deleted
   - Check your internet connection
   - Try updating yt-dlp: `pip install --upgrade yt-dlp`

4. **Permission errors**
   - Run as administrator (Windows) or use `sudo` (Linux/Mac)
   - Check folder permissions

### Getting Help:

- Check the log files in `TikTokVault/outputs/logs/`
- Enable detailed logging by editing the script
- Create an issue on GitHub with error details

## Contributing 🤝

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## Legal Notice ⚖️

- **Respect Copyright**: Only download videos you have permission to download
- **Personal Use**: This tool is intended for personal use and educational purposes
- **Terms of Service**: Comply with TikTok's Terms of Service
- **Fair Use**: Respect content creators' rights

## Dependencies 📦

- `yt-dlp`: Core video downloading functionality
- `tqdm`: Progress bars
- `colorama`: Cross-platform colored output
- `requests`: HTTP requests
- `pathlib`: File system operations

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 👏

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The amazing video downloader library
- TikTok content creators - For the amazing content
- Python community - For the excellent tools and libraries

---

**Happy Downloading! 🎉**

*Made with ❤️ for the TikTok community*
