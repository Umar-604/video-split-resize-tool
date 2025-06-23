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
    
    os.makedirs(output_dir, exist_ok=True)

    for start in range(0, duration, segment_duration):
        end = min(start + segment_duration, duration)
        part_num = start // segment_duration + 1
        output_filename = f"{basename}_part{part_num:02d}.mp4"
        output_path = os.path.join(output_dir, output_filename)
