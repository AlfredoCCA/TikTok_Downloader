"""
TikTok Database Viewer
Command-line interface for viewing and searching TikTok video database
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import colorama
from colorama import Back, Fore, Style
from database import TikTokDatabase

# Initialize colorama for cross-platform colored output
colorama.init(autoreset=True)


class TikTokDBViewer:
    def __init__(self):
        self.db = TikTokDatabase()

    def print_header(self, title):
        """Print a formatted header"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}{title}")
        print(f"{Fore.CYAN}{'='*60}")

    def format_file_size(self, size_bytes):
        """Convert bytes to human readable format"""
        if size_bytes == 0 or size_bytes is None:
            return "N/A"

        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"

    def format_duration(self, duration_seconds):
        """Convert seconds to minutes:seconds format"""
        if duration_seconds is None or duration_seconds == 0:
            return "N/A"

        minutes = int(duration_seconds // 60)
        seconds = int(duration_seconds % 60)
        return f"{minutes}:{seconds:02d}"

    def show_statistics(self):
        """Display database statistics"""
        self.print_header("📊 DATABASE STATISTICS")

        stats = self.db.get_statistics()

        if not stats:
            print(f"{Fore.RED}❌ Error retrieving statistics")
            return

        print(f"{Fore.GREEN}📹 Total Videos: {stats.get('total_videos', 0)}")
        print(f"{Fore.RED}❌ Failed Downloads: {stats.get('failed_downloads', 0)}")
        print(f"{Fore.BLUE}👤 Unique Creators: {stats.get('unique_creators', 0)}")
        print(
            f"{Fore.MAGENTA}💾 Total Size: {self.format_file_size(stats.get('total_file_size', 0))} ({stats.get('total_file_size_mb', 0)} MB)"
        )

        if stats.get("first_download"):
            print(
                f"{Fore.YELLOW}📅 First Download: {stats.get('first_download', 'N/A')}"
            )
            print(f"{Fore.YELLOW}📅 Last Download: {stats.get('last_download', 'N/A')}")

        # Top creators
        top_creators = stats.get("top_creators", [])
        if top_creators:
            print(f"\n{Fore.CYAN}🏆 TOP CREATORS:")
            for i, creator in enumerate(top_creators[:5], 1):
                print(f"  {i}. {creator['username']}: {creator['video_count']} videos")

    def show_recent_videos(self, limit=10):
        """Display recent videos"""
        self.print_header(f"🕒 RECENT VIDEOS (Last {limit})")

        videos = self.db.get_recent_videos(limit)

        if not videos:
            print(f"{Fore.YELLOW}No videos found in database")
            return

        for i, video in enumerate(videos, 1):
            title = video.get("title", "N/A")[:50] + (
                "..." if len(video.get("title", "")) > 50 else ""
            )
            creator = video.get("creator_username", "N/A")
            duration = self.format_duration(video.get("duration"))
            size = self.format_file_size(video.get("file_size"))
            download_date = video.get("download_date", "N/A")[
                :19
            ]  # Remove milliseconds

            print(f"\n{Fore.GREEN}{i}. {title}")
            print(f"   👤 Creator: {creator}")
            print(f"   ⏱️  Duration: {duration}")
            print(f"   💾 Size: {size}")
            print(f"   📅 Downloaded: {download_date}")

    def search_videos(self, query, field="all"):
        """Search videos in database"""
        self.print_header(f"🔍 SEARCH RESULTS: '{query}' in {field}")

        videos = self.db.search_videos(query, field)

        if not videos:
            print(f"{Fore.YELLOW}No videos found matching '{query}'")
            return

        print(f"{Fore.GREEN}Found {len(videos)} video(s):")

        for i, video in enumerate(videos[:20], 1):  # Limit to first 20 results
            title = video.get("title", "N/A")[:60] + (
                "..." if len(video.get("title", "")) > 60 else ""
            )
            creator = video.get("creator_username", "N/A")
            views = video.get("view_count", 0)
            likes = video.get("like_count", 0)
            download_date = video.get("download_date", "N/A")[:19]

            print(f"\n{Fore.CYAN}{i}. {title}")
            print(f"   👤 {creator} | 👁️ {views:,} views | ❤️ {likes:,} likes")
            print(f"   📅 Downloaded: {download_date}")

        if len(videos) > 20:
            print(f"\n{Fore.YELLOW}... and {len(videos) - 20} more results")

    def show_creator_videos(self, creator):
        """Show all videos by a specific creator"""
        self.print_header(f"👤 VIDEOS BY @{creator}")

        videos = self.db.get_videos_by_creator(creator)

        if not videos:
            print(f"{Fore.YELLOW}No videos found for creator '{creator}'")
            return

        print(f"{Fore.GREEN}Found {len(videos)} video(s) by @{creator}:")

        total_views = sum(video.get("view_count", 0) for video in videos)
        total_likes = sum(video.get("like_count", 0) for video in videos)

        print(f"{Fore.BLUE}📊 Total: {total_views:,} views, {total_likes:,} likes")

        for i, video in enumerate(videos, 1):
            title = video.get("title", "N/A")[:60] + (
                "..." if len(video.get("title", "")) > 60 else ""
            )
            views = video.get("view_count", 0)
            likes = video.get("like_count", 0)
            duration = self.format_duration(video.get("duration"))
            download_date = video.get("download_date", "N/A")[:19]

            print(f"\n{Fore.CYAN}{i}. {title}")
            print(f"   👁️ {views:,} views | ❤️ {likes:,} likes | ⏱️ {duration}")
            print(f"   📅 Downloaded: {download_date}")

    def show_video_details(self, video_id):
        """Show detailed information about a specific video"""
        video = self.db.get_video_by_id(video_id)

        if not video:
            print(f"{Fore.RED}❌ Video with ID '{video_id}' not found")
            return

        self.print_header(f"📹 VIDEO DETAILS: {video_id}")

        print(f"{Fore.GREEN}Title: {video.get('title', 'N/A')}")
        print(
            f"{Fore.BLUE}Creator: @{video.get('creator_username', 'N/A')} ({video.get('creator_display_name', 'N/A')})"
        )
        print(f"{Fore.CYAN}URL: {video.get('url', 'N/A')}")
        print(f"{Fore.YELLOW}Duration: {self.format_duration(video.get('duration'))}")
        print(
            f"{Fore.MAGENTA}File Size: {self.format_file_size(video.get('file_size'))}"
        )

        print(f"\n{Fore.CYAN}📊 ENGAGEMENT:")
        print(f"   👁️ Views: {video.get('view_count', 0):,}")
        print(f"   ❤️ Likes: {video.get('like_count', 0):,}")
        print(f"   💬 Comments: {video.get('comment_count', 0):,}")
        print(f"   🔄 Shares: {video.get('share_count', 0):,}")

        print(f"\n{Fore.CYAN}📅 DATES:")
        print(f"   📤 Uploaded: {video.get('upload_date', 'N/A')}")
        print(f"   📥 Downloaded: {video.get('download_date', 'N/A')}")

        if video.get("description"):
            desc = video.get("description", "")[:200] + (
                "..." if len(video.get("description", "")) > 200 else ""
            )
            print(f"\n{Fore.CYAN}📝 DESCRIPTION:")
            print(f"   {desc}")

        if video.get("file_path"):
            print(f"\n{Fore.CYAN}📁 FILE PATH:")
            print(f"   {video.get('file_path')}")

    def interactive_menu(self):
        """Run interactive menu"""
        while True:
            self.print_header("🎬 TIKTOK DATABASE VIEWER")

            print(f"{Fore.YELLOW}1. Show Statistics")
            print(f"{Fore.YELLOW}2. Show Recent Videos")
            print(f"{Fore.YELLOW}3. Search Videos")
            print(f"{Fore.YELLOW}4. Show Creator's Videos")
            print(f"{Fore.YELLOW}5. Show Video Details")
            print(f"{Fore.YELLOW}6. Exit")

            choice = input(f"\n{Fore.CYAN}Choose an option (1-6): ").strip()

            if choice == "1":
                self.show_statistics()

            elif choice == "2":
                try:
                    limit = input(
                        f"{Fore.CYAN}Number of videos to show (default 10): "
                    ).strip()
                    limit = int(limit) if limit else 10
                    self.show_recent_videos(limit)
                except ValueError:
                    print(f"{Fore.RED}❌ Please enter a valid number")

            elif choice == "3":
                query = input(f"{Fore.CYAN}Search query: ").strip()
                if query:
                    field = (
                        input(
                            f"{Fore.CYAN}Search in (all/title/creator/description) [all]: "
                        ).strip()
                        or "all"
                    )
                    self.search_videos(query, field)
                else:
                    print(f"{Fore.RED}❌ Please enter a search query")

            elif choice == "4":
                creator = input(f"{Fore.CYAN}Creator username (without @): ").strip()
                if creator:
                    self.show_creator_videos(creator)
                else:
                    print(f"{Fore.RED}❌ Please enter a creator username")

            elif choice == "5":
                video_id = input(f"{Fore.CYAN}Video ID: ").strip()
                if video_id:
                    self.show_video_details(video_id)
                else:
                    print(f"{Fore.RED}❌ Please enter a video ID")

            elif choice == "6":
                print(f"{Fore.GREEN}👋 Goodbye!")
                break

            else:
                print(f"{Fore.RED}❌ Invalid choice. Please try again.")

            input(f"\n{Fore.CYAN}Press Enter to continue...")


def main():
    """Main entry point"""
    viewer = TikTokDBViewer()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "stats":
            viewer.show_statistics()
        elif command == "recent":
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            viewer.show_recent_videos(limit)
        elif command == "search":
            if len(sys.argv) < 3:
                print(f"{Fore.RED}❌ Please provide a search query")
                return
            query = sys.argv[2]
            field = sys.argv[3] if len(sys.argv) > 3 else "all"
            viewer.search_videos(query, field)
        elif command == "creator":
            if len(sys.argv) < 3:
                print(f"{Fore.RED}❌ Please provide a creator username")
                return
            creator = sys.argv[2]
            viewer.show_creator_videos(creator)
        elif command == "video":
            if len(sys.argv) < 3:
                print(f"{Fore.RED}❌ Please provide a video ID")
                return
            video_id = sys.argv[2]
            viewer.show_video_details(video_id)
        else:
            print(f"{Fore.RED}❌ Unknown command: {command}")
            print(
                f"{Fore.YELLOW}Available commands: stats, recent, search, creator, video"
            )
    else:
        # Interactive mode
        viewer.interactive_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}💥 Error: {str(e)}")
        sys.exit(1)
