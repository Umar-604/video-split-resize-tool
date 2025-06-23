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

def main():
    parser = argparse.ArgumentParser(description="Split and resize videos.")
    parser.add_argument('--file', type=str, help="Path to a single .mp4 file")
    parser.add_argument('--folder', type=str, help="Path to folder with .mp4 files")
    parser.add_argument('--output', type=str, default="output_clips", help="Output directory")
    args = parser.parse_args()

    if args.file:
        process_single_file(args.file, args.output)
    elif args.folder:
        process_folder(args.folder, args.output)
    else:
        print("Please provide --file or --folder")

if __name__ == '__main__':
    main()
