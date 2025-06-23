# 🎬 Video Split & Resize Tool

A simple Python script to **split large MP4 video files into smaller clips** and **resize** them to a specific resolution. Useful for processing long videos into segments suitable for training data, previews, or optimized playback.

---

## 🔧 Features

- ✅ Split MP4 videos into fixed-length segments (default: 20 seconds)
- ✅ Resize video clips to a custom resolution (default: 1280x768)
- ✅ Process a **single video file** or an **entire folder** of videos
- ✅ Uses `ffmpeg` for fast and efficient video processing

---

## 📦 Dependencies

- Python 3.6+
- [moviepy](https://github.com/Zulko/moviepy)
- ffmpeg (must be installed and available in your system's PATH)

### 📥 Install dependencies

```bash
pip install moviepy
````

Make sure `ffmpeg` is installed:

```bash
# On macOS
brew install ffmpeg

# On Ubuntu/Debian
sudo apt install ffmpeg

# On Windows
# Download from https://ffmpeg.org/download.html and add it to PATH
```

---

## 🚀 Usage

Run the script from your terminal:

### ▶️ To process a single video:

```bash
python process_videos.py --file path/to/video.mp4 --output path/to/output_dir
```

### 📁 To process all `.mp4` videos in a folder:

```bash
python process_videos.py --folder path/to/folder --output path/to/output_dir
```

---

## ⚙️ Optional Arguments

| Argument   | Description                          | Default        |
| ---------- | ------------------------------------ | -------------- |
| `--file`   | Path to a single `.mp4` file         | None           |
| `--folder` | Path to folder with `.mp4` files     | None           |
| `--output` | Output directory for processed clips | `output_clips` |

> 🔸 Either `--file` or `--folder` must be provided.

---

## 🛠 Customization

You can manually adjust the segment duration or resolution in the `split_and_resize` function:

```python
split_and_resize(video_path, output_dir, segment_duration=30, resolution=(1920, 1080))
```

---

## 📁 Output Structure

Clips are saved in this format:

```
<original_filename>_part01.mp4
<original_filename>_part02.mp4
<original_filename>_part03.mp4
...
```

All output is stored inside the directory specified by `--output`.

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## 👨‍💻 Author

Developed by **Umar Tariq**
Contributions and suggestions are welcome!

