import os
import sys
from datetime import datetime, timedelta

# Check for command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 make_frames.py <video_filename>")
    sys.exit(1)

video_filename = sys.argv[1]

# Validate input file
if not os.path.isfile(video_filename):
    print(f"❌ File not found: {video_filename}")
    sys.exit(1)

# Create output folder
frames_dir = "frames"
os.makedirs(frames_dir, exist_ok=True)

# Extract frames using ffmpeg (1 frame per second)
ffmpeg_command = f'ffmpeg -i "{video_filename}" -vf fps=1 "{frames_dir}/frame_%05d.jpeg"'
os.system(ffmpeg_command)

# Extract base timestamp from filename
basename = os.path.splitext(os.path.basename(video_filename))[0]
try:
    start_time = datetime.strptime(basename, "%Y-%m-%d_%H_%M_%S")
except ValueError:
    print("❌ Filename must be in format YYYY-MM-DD_HH_MM_SS.mp4")
    sys.exit(1)

# Rename frames to match timestamp
frames = sorted(f for f in os.listdir(frames_dir) if f.startswith("frame_") and f.endswith(".jpeg"))

for i, frame in enumerate(frames):
    timestamp = start_time + timedelta(seconds=i)
    new_name = timestamp.strftime("%Y-%m-%d_%H_%M_%S.jpeg")
    os.rename(os.path.join(frames_dir, frame), os.path.join(frames_dir, new_name))

print("✅ Done! Frames saved in:", frames_dir)

