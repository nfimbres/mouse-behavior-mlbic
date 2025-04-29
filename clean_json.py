import json
import sys
import os
from datetime import datetime

def convert_entry(entry):
    # Get the filename
    filename = entry.get("meta", {}).get("file", "")
    image_path = f"{filename}"

    # Extract timestamp from filename
    base_name = os.path.splitext(filename)[0]  # Remove ".jpeg"
    try:
        dt = datetime.strptime(base_name, "%Y-%m-%d_%H_%M_%S")
        timestamp = int(dt.timestamp())
    except ValueError:
        timestamp = None  # If format doesn't match, skip timestamp

    # Get labels from 'accept'
    labels = entry.get("accept", [])

    return {
        "image": image_path,
        "labels": labels,
        "timestamp": timestamp
    }

def main(input_path, output_path):
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            if not line.strip():
                continue  # Skip empty lines
            entry = json.loads(line)
            new_entry = convert_entry(entry)
            outfile.write(json.dumps(new_entry) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_jsonl.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    main(input_path, output_path)

