# process_videos.py
import os
import argparse
import subprocess
from pathlib import Path
from moviepy.editor import VideoFileClip

def split_and_resize(video_path, output_dir, segment_duration=20, resolution=(1280, 768)):
    video = VideoFileClip(str(video_path))
    duration = int(video.duration)
    basename = Path(video_path).stem
