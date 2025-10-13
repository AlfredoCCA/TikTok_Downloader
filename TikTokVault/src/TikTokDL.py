"""
TikTok Downloader - Main Script
Downloads TikTok videos from URLs listed in data directory files
Saves downloaded videos to outputs directory
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import yt_dlp
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style

# Initialize colorama for cross-platform colored output
colorama.init(autoreset=True)

class TikTokDownloader:
    def __init__(self):
        # Set up paths
        self.base_dir = Path(__file__).parent.parent  # TikTokVault directory
        self.data_dir = self.base_dir / "data"
        self.outputs_dir = self.base_dir / "outputs"
        
        # Create directories if they don't exist
        self.data_dir.mkdir(exist_ok=True)
        self.outputs_dir.mkdir(exist_ok=True)
        
        # Create subdirectories for organization
        self.videos_dir = self.outputs_dir / "videos"
        self.logs_dir = self.outputs_dir / "logs"
        self.metadata_dir = self.outputs_dir / "metadata"
        
        for dir_path in [self.videos_dir, self.logs_dir, self.metadata_dir]:
            dir_path.mkdir(exist_ok=True)
    
    def load_urls_from_file(self, filename="tiktok_urls.txt"):
        """Load TikTok URLs from a file in the data directory"""
        file_path = self.data_dir / filename
        
        if not file_path.exists():
            print(f"{Fore.RED}❌ File {filename} not found in data directory!")
            print(f"{Fore.YELLOW}💡 Create a file at: {file_path}")
            print(f"{Fore.YELLOW}💡 Add TikTok URLs, one per line")
            return []
        
        urls = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        if 'tiktok.com' in line:
                            urls.append(line)
                        else:
                            print(f"{Fore.YELLOW}⚠️  Line {line_num}: Not a TikTok URL - {line}")
            
            print(f"{Fore.GREEN}📂 Loaded {len(urls)} URLs from {filename}")
            return urls
        
        except Exception as e:
            print(f"{Fore.RED}❌ Error reading file {filename}: {str(e)}")
            return []
    
    def setup_ydl_options(self):
        """Configure yt-dlp download options"""
        return {
            'outtmpl': str(self.videos_dir / '%(uploader)s_%(title)s_%(id)s.%(ext)s'),
            'format': 'best[height<=720]/best',  # Best quality up to 720p
            'writeinfojson': True,  # Save metadata
            'writethumbnail': True,  # Save thumbnail
            'writesubtitles': False,  # TikTok doesn't usually have subtitles
            'ignoreerrors': True,  # Continue on errors
            'no_warnings': False,
            'extract_flat': False,
        }
    
    def download_videos(self, urls):
        """Download TikTok videos from list of URLs"""
        if not urls:
            print(f"{Fore.RED}❌ No URLs to download!")
            return [], []
        
        print(f"{Fore.CYAN}🚀 Starting download of {len(urls)} videos...")
        print(f"{Fore.CYAN}📁 Videos will be saved to: {self.videos_dir}")
        
        successful_downloads = []
        failed_downloads = []
        download_log = []
        
        # Setup yt-dlp
        ydl_opts = self.setup_ydl_options()
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Progress bar for overall progress
            with tqdm(urls, desc="Downloading videos", unit="video") as pbar:
                for i, url in enumerate(pbar):
                    try:
                        pbar.set_description(f"Downloading video {i+1}/{len(urls)}")
                        
                        # Extract info first to get metadata
                        info = ydl.extract_info(url, download=False)
                        title = info.get('title', 'Unknown')
                        uploader = info.get('uploader', 'Unknown')
                        
                        pbar.set_postfix_str(f"'{title[:30]}...' by {uploader}")
                        
                        # Download the video
                        ydl.download([url])
                        
                        successful_downloads.append({
                            'url': url,
                            'title': title,
                            'uploader': uploader,
                            'timestamp': datetime.now().isoformat()
                        })
                        
                        print(f"\n{Fore.GREEN}✅ Downloaded: {title} by {uploader}")
                        
                    except Exception as e:
                        error_msg = str(e)
                        failed_downloads.append({
                            'url': url,
                            'error': error_msg,
                            'timestamp': datetime.now().isoformat()
                        })
                        
                        print(f"\n{Fore.RED}❌ Failed to download {url}")
                        print(f"{Fore.RED}   Error: {error_msg}")
        
        # Save download log
        self.save_download_log(successful_downloads, failed_downloads)
        
        return successful_downloads, failed_downloads
    
    def save_download_log(self, successful, failed):
        """Save download results to a log file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.logs_dir / f"download_log_{timestamp}.json"
        
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_urls': len(successful) + len(failed),
            'successful_downloads': len(successful),
            'failed_downloads': len(failed),
            'success_rate': len(successful) / (len(successful) + len(failed)) * 100 if (successful or failed) else 0,
            'successful': successful,
            'failed': failed
        }
        
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
            print(f"{Fore.BLUE}📝 Download log saved to: {log_file}")
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to save log: {str(e)}")
    
    def print_summary(self, successful, failed):
        """Print download summary"""
        total = len(successful) + len(failed)
        success_rate = (len(successful) / total * 100) if total > 0 else 0
        
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}📊 DOWNLOAD SUMMARY")
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.GREEN}✅ Successful: {len(successful)}/{total}")
        print(f"{Fore.RED}❌ Failed: {len(failed)}/{total}")
        print(f"{Fore.BLUE}📈 Success Rate: {success_rate:.1f}%")
        
        if successful:
            print(f"\n{Fore.GREEN}🎉 Successfully downloaded videos:")
            for item in successful[:5]:  # Show first 5
                print(f"  • {item['title'][:50]}... by {item['uploader']}")
            if len(successful) > 5:
                print(f"  ... and {len(successful) - 5} more")
        
        if failed:
            print(f"\n{Fore.RED}💥 Failed downloads:")
            for item in failed[:3]:  # Show first 3 failures
                print(f"  • {item['url']}")
                print(f"    Error: {item['error'][:100]}...")
            if len(failed) > 3:
                print(f"  ... and {len(failed) - 3} more failures")
    
    def list_available_files(self):
        """List available URL files in data directory"""
        txt_files = list(self.data_dir.glob("*.txt"))
        if txt_files:
            print(f"{Fore.CYAN}📂 Available URL files in data directory:")
            for i, file in enumerate(txt_files, 1):
                print(f"  {i}. {file.name}")
            return txt_files
        else:
            print(f"{Fore.YELLOW}📂 No .txt files found in data directory")
            return []
    
    def run_interactive(self):
        """Run in interactive mode"""
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}🎬 TikTok Downloader - Interactive Mode")
        print(f"{Fore.MAGENTA}{'='*60}")
        
        # List available files
        available_files = self.list_available_files()
        
        if not available_files:
            print(f"{Fore.YELLOW}💡 Create a .txt file in the data directory with TikTok URLs")
            return
        
        # Let user choose file
        while True:
            try:
                choice = input(f"\n{Fore.CYAN}Enter file number (or 'q' to quit): ").strip()
                if choice.lower() == 'q':
                    return
                
                file_index = int(choice) - 1
                if 0 <= file_index < len(available_files):
                    selected_file = available_files[file_index]
                    break
                else:
                    print(f"{Fore.RED}❌ Invalid choice. Please try again.")
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number.")
        
        # Load URLs and download
        urls = self.load_urls_from_file(selected_file.name)
        if urls:
            successful, failed = self.download_videos(urls)
            self.print_summary(successful, failed)
    
    def run_batch(self, filename="tiktok_urls.txt"):
        """Run in batch mode with specific file"""
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}🎬 TikTok Downloader - Batch Mode")
        print(f"{Fore.MAGENTA}{'='*60}")
        
        urls = self.load_urls_from_file(filename)
        if urls:
            successful, failed = self.download_videos(urls)
            self.print_summary(successful, failed)
        else:
            print(f"{Fore.RED}❌ No URLs found or file doesn't exist")

def main():
    """Main entry point"""
    downloader = TikTokDownloader()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        # Batch mode with specific file
        filename = sys.argv[1]
        downloader.run_batch(filename)
    else:
        # Interactive mode
        downloader.run_interactive()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Download interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}💥 Unexpected error: {str(e)}")
        sys.exit(1)
