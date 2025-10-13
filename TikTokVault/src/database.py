"""
TikTok Video Database Manager
Handles database operations for storing video metadata
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import logging

class TikTokDatabase:
    def __init__(self, db_path: Path = None):
        """
        Initialize database connection
        
        Args:
            db_path: Path to SQLite database file. If None, creates in outputs directory
        """
        if db_path is None:
            # Default to outputs directory
            self.db_path = Path(__file__).parent.parent / "outputs" / "tiktok_videos.db"
        else:
            self.db_path = db_path
        
        # Ensure directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self.init_database()
    
    def init_database(self):
        """Create database tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create videos table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos (
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
                    download_date TEXT NOT NULL,
                    file_path TEXT,
                    thumbnail_path TEXT,
                    file_size INTEGER,
                    format_quality TEXT,
                    tags TEXT,  -- JSON string of tags/hashtags
                    metadata_json TEXT,  -- Full metadata as JSON
                    download_status TEXT DEFAULT 'completed',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create download_sessions table to track batch downloads
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS download_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT UNIQUE NOT NULL,
                    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    end_time TIMESTAMP,
                    total_urls INTEGER,
                    successful_downloads INTEGER,
                    failed_downloads INTEGER,
                    success_rate REAL,
                    source_file TEXT,
                    notes TEXT
                )
            ''')
            
            # Create indexes for better performance
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_video_id ON videos(video_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_creator_username ON videos(creator_username)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_download_date ON videos(download_date)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_session_id ON download_sessions(session_id)')
            
            conn.commit()
    
    def add_video(self, video_data: Dict) -> bool:
        """
        Add a video record to the database
        
        Args:
            video_data: Dictionary containing video information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Extract and prepare data
                video_id = video_data.get('id', '')
                url = video_data.get('webpage_url', video_data.get('url', ''))
                title = video_data.get('title', '')
                description = video_data.get('description', '')
                creator_username = video_data.get('uploader', video_data.get('uploader_id', ''))
                creator_display_name = video_data.get('uploader', '')
                duration = video_data.get('duration', 0)
                view_count = video_data.get('view_count', 0)
                like_count = video_data.get('like_count', 0)
                comment_count = video_data.get('comment_count', 0)
                share_count = video_data.get('repost_count', 0)
                upload_date = video_data.get('upload_date', '')
                download_date = datetime.now().isoformat()
                
                # File information
                file_path = video_data.get('_filename', '')
                thumbnail_path = video_data.get('thumbnail', '')
                file_size = video_data.get('filesize', 0) or video_data.get('filesize_approx', 0)
                format_quality = video_data.get('format', '')
                
                # Tags/hashtags
                tags = video_data.get('tags', [])
                tags_json = json.dumps(tags) if tags else None
                
                # Full metadata as JSON (excluding binary data)
                metadata_copy = dict(video_data)
                # Remove potentially large or binary fields
                for key in ['formats', 'thumbnails', 'automatic_captions', 'subtitles']:
                    metadata_copy.pop(key, None)
                metadata_json = json.dumps(metadata_copy, default=str)
                
                # Insert or update video record
                cursor.execute('''
                    INSERT OR REPLACE INTO videos (
                        video_id, url, title, description, creator_username, 
                        creator_display_name, duration, view_count, like_count, 
                        comment_count, share_count, upload_date, download_date,
                        file_path, thumbnail_path, file_size, format_quality,
                        tags, metadata_json, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    video_id, url, title, description, creator_username,
                    creator_display_name, duration, view_count, like_count,
                    comment_count, share_count, upload_date, download_date,
                    file_path, thumbnail_path, file_size, format_quality,
                    tags_json, metadata_json, datetime.now().isoformat()
                ))
                
                conn.commit()
                return True
                
        except Exception as e:
            logging.error(f"Error adding video to database: {str(e)}")
            return False
    
    def add_failed_download(self, url: str, error: str) -> bool:
        """
        Add a failed download record
        
        Args:
            url: The URL that failed to download
            error: Error message
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO videos (
                        video_id, url, download_date, download_status, metadata_json
                    ) VALUES (?, ?, ?, ?, ?)
                ''', (
                    'failed_' + str(hash(url))[:10], url, 
                    datetime.now().isoformat(), 'failed',
                    json.dumps({'error': error, 'url': url})
                ))
                
                conn.commit()
                return True
                
        except Exception as e:
            logging.error(f"Error adding failed download to database: {str(e)}")
            return False
    
    def start_download_session(self, session_id: str, total_urls: int, source_file: str = None) -> bool:
        """
        Start a new download session
        
        Args:
            session_id: Unique identifier for this session
            total_urls: Total number of URLs to download
            source_file: Source file name
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO download_sessions (
                        session_id, total_urls, source_file
                    ) VALUES (?, ?, ?)
                ''', (session_id, total_urls, source_file))
                
                conn.commit()
                return True
                
        except Exception as e:
            logging.error(f"Error starting download session: {str(e)}")
            return False
    
    def end_download_session(self, session_id: str, successful: int, failed: int) -> bool:
        """
        End a download session with results
        
        Args:
            session_id: Session identifier
            successful: Number of successful downloads
            failed: Number of failed downloads
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                total = successful + failed
                success_rate = (successful / total * 100) if total > 0 else 0
                
                cursor.execute('''
                    UPDATE download_sessions SET 
                        end_time = CURRENT_TIMESTAMP,
                        successful_downloads = ?,
                        failed_downloads = ?,
                        success_rate = ?
                    WHERE session_id = ?
                ''', (successful, failed, success_rate, session_id))
                
                conn.commit()
                return True
                
        except Exception as e:
            logging.error(f"Error ending download session: {str(e)}")
            return False
    
    def get_video_by_id(self, video_id: str) -> Optional[Dict]:
        """
        Get video information by video ID
        
        Args:
            video_id: TikTok video ID
            
        Returns:
            Dict or None: Video information or None if not found
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('SELECT * FROM videos WHERE video_id = ?', (video_id,))
                row = cursor.fetchone()
                
                return dict(row) if row else None
                
        except Exception as e:
            logging.error(f"Error getting video by ID: {str(e)}")
            return None
    
    def get_videos_by_creator(self, creator_username: str) -> List[Dict]:
        """
        Get all videos by a specific creator
        
        Args:
            creator_username: Creator's username
            
        Returns:
            List[Dict]: List of video records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT * FROM videos 
                    WHERE creator_username = ? AND download_status = 'completed'
                    ORDER BY download_date DESC
                ''', (creator_username,))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            logging.error(f"Error getting videos by creator: {str(e)}")
            return []
    
    def get_recent_videos(self, limit: int = 50) -> List[Dict]:
        """
        Get recently downloaded videos
        
        Args:
            limit: Maximum number of videos to return
            
        Returns:
            List[Dict]: List of recent video records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT * FROM videos 
                    WHERE download_status = 'completed'
                    ORDER BY download_date DESC 
                    LIMIT ?
                ''', (limit,))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            logging.error(f"Error getting recent videos: {str(e)}")
            return []
    
    def get_statistics(self) -> Dict:
        """
        Get database statistics
        
        Returns:
            Dict: Statistics about stored videos
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                stats = {}
                
                # Total videos
                cursor.execute('SELECT COUNT(*) FROM videos WHERE download_status = "completed"')
                stats['total_videos'] = cursor.fetchone()[0]
                
                # Failed downloads
                cursor.execute('SELECT COUNT(*) FROM videos WHERE download_status = "failed"')
                stats['failed_downloads'] = cursor.fetchone()[0]
                
                # Unique creators
                cursor.execute('SELECT COUNT(DISTINCT creator_username) FROM videos WHERE download_status = "completed"')
                stats['unique_creators'] = cursor.fetchone()[0]
                
                # Total file size
                cursor.execute('SELECT SUM(file_size) FROM videos WHERE download_status = "completed"')
                total_size = cursor.fetchone()[0] or 0
                stats['total_file_size'] = total_size
                stats['total_file_size_mb'] = round(total_size / (1024 * 1024), 2)
                
                # Date range
                cursor.execute('''
                    SELECT MIN(download_date), MAX(download_date) 
                    FROM videos WHERE download_status = "completed"
                ''')
                date_range = cursor.fetchone()
                stats['first_download'] = date_range[0]
                stats['last_download'] = date_range[1]
                
                # Top creators
                cursor.execute('''
                    SELECT creator_username, COUNT(*) as video_count
                    FROM videos 
                    WHERE download_status = "completed" AND creator_username IS NOT NULL
                    GROUP BY creator_username
                    ORDER BY video_count DESC
                    LIMIT 10
                ''')
                stats['top_creators'] = [{'username': row[0], 'video_count': row[1]} 
                                       for row in cursor.fetchall()]
                
                return stats
                
        except Exception as e:
            logging.error(f"Error getting statistics: {str(e)}")
            return {}
    
    def search_videos(self, query: str, field: str = 'all') -> List[Dict]:
        """
        Search videos by title, creator, or description
        
        Args:
            query: Search query
            field: Field to search in ('all', 'title', 'creator', 'description')
            
        Returns:
            List[Dict]: Matching video records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = f'%{query}%'
                
                if field == 'title':
                    cursor.execute('''
                        SELECT * FROM videos 
                        WHERE title LIKE ? AND download_status = 'completed'
                        ORDER BY download_date DESC
                    ''', (query,))
                elif field == 'creator':
                    cursor.execute('''
                        SELECT * FROM videos 
                        WHERE creator_username LIKE ? AND download_status = 'completed'
                        ORDER BY download_date DESC
                    ''', (query,))
                elif field == 'description':
                    cursor.execute('''
                        SELECT * FROM videos 
                        WHERE description LIKE ? AND download_status = 'completed'
                        ORDER BY download_date DESC
                    ''', (query,))
                else:  # search all fields
                    cursor.execute('''
                        SELECT * FROM videos 
                        WHERE (title LIKE ? OR creator_username LIKE ? OR description LIKE ?)
                        AND download_status = 'completed'
                        ORDER BY download_date DESC
                    ''', (query, query, query))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            logging.error(f"Error searching videos: {str(e)}")
            return []
    
    def close(self):
        """Close database connection (not needed with context managers but good practice)"""
        # Using context managers (with statements) automatically handles connections
        pass