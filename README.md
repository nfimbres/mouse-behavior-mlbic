# Mouse Behavior Annotation Pipeline

[![Prodigy Annotation](https://img.shields.io/badge/Tool-Prodigy-orange)]()  
[![Video Analysis](https://img.shields.io/badge/Video--Frame-Processing-blue)]()  
[![Machine Learning Ready](https://img.shields.io/badge/ML-Ready-green)]()

---

## Overview

This project enables the analysis of mouse behavior by processing video files into frame images, facilitating manual multi-label annotation using Prodigy, and preparing the data for training machine learning models.  
It supports a workflow for both local and server-based environments.

The pipeline includes frame extraction, annotation, data cleaning, dataset management, and prediction on new video samples.

---

## Features

- Frame-by-frame video processing.
- Multi-label image annotation using Prodigy.
- Clean and structured data output for model training.
- Google Colab compatibility for training and inference.
- Server-based (CPSC) deployment and configuration instructions.

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/mouse-behavior-mlbic.git
   cd mouse-behavior-mlbic
   ```

2. Ensure Python 3.10 is installed.

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install and configure Prodigy from https://prodi.gy/

---

## Usage

### 1. Frame Extraction

Rename the video to match the timestamp of the first frame:
```
YYYY-MM-DD_HH_MM_SS.mp4
```

Extract frames:
```
python make_frames.py --input_path path/to/video.mp4 --output_folder path/to/frames/
```

### 2. Annotation with Prodigy

Start annotation:
```
prodigy image.multchoice [dataset_name] [frame_folder_path] "ON HOUSE (N), ON HOUSE (S), IN HOUSE (N), IN HOUSE (S), IN FOOD HOPPER, ON FOOD HOPPER" -F mult_choice.py
```

Export annotations:
```
prodigy db-out [dataset_name] > annotations-unclean.jsonl
```

### 3. Clean Annotations

Clean the exported annotations:
```
python3 clean_json.py annotations-unclean.jsonl annotations-clean.jsonl
```

Zip the frame folder:
```
zip -r frames.zip path/to/frames/
```

### 4. Upload to Google Colab

Upload `frames.zip` and `annotations-clean.jsonl` to the notebook when prompted.

---

## Prodigy CPSC Server Configuration

Navigate to the Prodigy install directory:
```
cd /home/faculty/pchandra/.local/lib/python3.10/site-packages/
```

Set environment variables:
```
export PRODIGY_CONFIG_OVERRIDES='{"host": "10.128.0.3", "port": 6225}'
export PYTHONPATH="/home/students/nfimbres"
```

Run Prodigy:
```
python3 -m prodigy image.multchoice [dataset] /home/students/nfimbres/mouse-behavior-mlbic/frames/[frame folder] "ON HOUSE (N), ON HOUSE (S), IN HOUSE (N), IN HOUSE (S), IN FOOD HOPPER, ON FOOD HOPPER" -F /home/students/nfimbres/prodigy_recipes/mult_choice.py
```

Export and clean JSONL:
```
python3 -m prodigy db-out [dataset] > /home/students/nfimbres/mouse-behavior-mlbic/json_output/[annotations].jsonl
python3 /home/students/nfimbres/prodigy_recipes/clean_json.py original.jsonl clean.jsonl
```

List existing datasets:
```
sqlite3 /home/students/nfimbres/prodigy_data/prodigy.db "SELECT name FROM dataset;"
```

Create dataset manually in Python:
```python
from prodigy.components.db import connect

db = connect()
dataset_id = "[dataset]"
db.add_dataset(dataset_id)

print(f"✅ Created dataset: {dataset_id}")
```

---

## Examples

Extracting frames:
```
python make_frames.py --input_path videos/mouse_day1.mp4 --output_folder frames/day1
```

Running annotation:
```
prodigy image.multchoice mouse_day1 frames/day1 "ON HOUSE (N), ON HOUSE (S), IN HOUSE (N), ..." -F mult_choice.py
```

---

## Troubleshooting

- Ensure the video file is properly renamed using the timestamp format.
- Prodigy must be licensed and properly installed.
- Confirm all label names are properly quoted in command line.
- JSONL files must be cleaned before use in machine learning pipelines.

---

## Contributors

**Nathan Fimbres**  
University of Mary Washington  
Fredericksburg, Virginia, USA  
nfimbres@mail.umw.edu

---

## License

This project is intended for academic research and use. Contact the contributors for reuse permissions or licensing inquiries.
