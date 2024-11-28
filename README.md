# Python-Data-Science-Session4

## Overview

This repository contains a Python script and sample data files for processing and analyzing satellite annotation files. The script is designed to validate file naming conventions, analyze file content, and generate meaningful insights.

## Contents

- `exercise_zip_file.py`: The main Python script for processing annotation files.
- `annotations/`: A folder containing sample satellite annotation files. These files follow the naming convention and format described below.

## File Naming Convention

The script processes annotation files with the following naming format:
{DATE}_{TIME}SN{SATELLITE_NUMBER}QUICKVIEW_VISUAL{VERSION}{UNIQUE_REGION}.txt


Where:
- **DATE**: A string in the format `YYYYMMDD`, e.g., `20240101`.
- **TIME**: A string in the format `HHMMSS`, e.g., `192856`.
- **SATELLITE_NUMBER**: An integer representing the satellite number, e.g., `24`.
- **VERSION**: A pipeline version string in the format `x_x_x`, e.g., `1_1_10`.
- **UNIQUE_REGION**: A unique region identifier, e.g., `SATL-2KM-10N_552_4164`.

## Features

The script performs the following tasks:
1. Counts the total number of files in the folder.
2. Validates file names against the specified naming convention.
3. Analyzes annotations per month and identifies the month with the most annotations.
4. Sorts files from the most recent to the oldest.
5. Identifies unique satellites and calculates annotations per satellite.
6. Counts unique regions.

## How to Use

### Requirements

- Python 3.8 or later
- Required libraries: `os`, `re`, `collections`, `pathlib`

### Steps

1. Clone the repository:
   git clone https://github.com/zo-fe/Python-Data-Science-Session4.git
   cd Python-Data-Science-Session4
2. Ensure the annotations folder contains your annotation files
3. Run the script:
   python exercise_zip_file.py
