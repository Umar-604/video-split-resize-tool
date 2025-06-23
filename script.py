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
        
        cmd = [
            'ffmpeg', '-y',
            '-ss', str(start),
            '-i', str(video_path),
            '-t', str(end - start),
            '-vf', f'scale={resolution[0]}:{resolution[1]}',
            '-c:a', 'copy',
            output_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def process_single_file(file_path, output_dir):
    print(f"Processing: {file_path}")
    split_and_resize(file_path, output_dir)

def process_folder(folder_path, output_dir):
    for file in os.listdir(folder_path):
        if file.lower().endswith('.mp4'):
            process_single_file(os.path.join(folder_path, file), output_dir)

