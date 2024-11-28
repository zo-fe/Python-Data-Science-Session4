import os
import re
from collections import defaultdict

# Directory containing annotation files
annotations_dir = "/Users/lorenzoferrantin/Python-Data-Science-Session4/annotations"

# Regex for validating file naming convention
file_pattern = re.compile(
    r"^(\d{8})_(\d{6})_SN(\d+)_QUICKVIEW_VISUAL_(\d+_\d+_\d+)_(.+)\.txt$"
)

# Initialize variables
file_count = 0
valid_files = []
annotations_per_month = defaultdict(int)
annotations_per_satellite = defaultdict(int)
unique_regions = set()

# 1. Count total files and validate naming convention
for file_name in os.listdir(annotations_dir):
    file_count += 1
    match = file_pattern.match(file_name)
    if match:
        valid_files.append(file_name)

        # Extract parts from the filename
        date, time, satellite, version, region = match.groups()

        # Update per-month and satellite counts
        year_month = date[:6]  # Extract YYYYMM
        annotations_per_month[year_month] += 1
        annotations_per_satellite[satellite] += 1

        # Collect unique regions
        unique_regions.add(region)

# 2. Output results of file counting and validation
print(f"Total files: {file_count}")
print(f"Valid files: {len(valid_files)}")
print(f"Invalid files: {file_count - len(valid_files)}")

# 3. Find the month with the most annotations
if annotations_per_month:
    most_annotations_month = max(annotations_per_month, key=annotations_per_month.get)
    print(f"Month with most annotations: {most_annotations_month} ({annotations_per_month[most_annotations_month]})")
else:
    print("No annotations per month found.")

# 4. Print files from most recent to oldest
valid_files.sort(reverse=True, key=lambda x: file_pattern.match(x).groups()[:2])
print("Files from most recent to oldest:")
for file_name in valid_files:
    print(file_name)

# 5. Satellite analysis
if valid_files:
    most_recent_file = valid_files[0]
    most_recent_satellite = file_pattern.match(most_recent_file).group(3)
    print(f"Unique satellites: {len(annotations_per_satellite)}")
    print(f"Annotations per satellite: {annotations_per_satellite}")
    print(f"Satellite in most recent annotation: {most_recent_satellite}")
else:
    print("No valid files to analyze.")

# 6. Unique region analysis
print(f"Unique regions: {len(unique_regions)}")