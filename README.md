# Image Processing Script

This Python project downloads images from URLs provided in a CSV file, removes their backgrounds, and saves the processed images to a specified directory. The project also logs the results of the processing into a CSV file.

## Description

This script processes a list of researcher images by:
1. Downloading each image from a given URL.
2. Removing the background from each image.
3. Saving the processed images to a specified directory.
4. Logging the status of each image processing task to a CSV file.

## Features

- Download images from URLs.
- Remove the background from images using `rembg`.
- Save the processed images to a specified directory.
- Log the processing results.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/image-processing-script.git
    cd image-processing-script
    ```

2. Install the required Python packages:

    ```bash
    pip install pandas requests pillow rembg
    ```

## Usage

1. Prepare a CSV file with the following columns:
   - `ResearcherDirectoryItem__ResearcherImage-u0xee6-2 src`: The column containing the URLs of the images to be processed.
   - `researcher-name`: The column containing the names of the researchers.

2. Update the script with the paths to your CSV file, output directory, and output log file:

    ```python
    csv_file = '/path/to/your/research.csv'  # Path to your CSV file
    output_dir = '/path/to/your/output/directory'  # Directory to save processed images
    output_log = '/path/to/your/output/log.csv'  # Path to save the log file
    ```

3. Run the script:

    ```bash
    python process_images.py
    ```

## Example

```python
csv_file = '/Users/apple/Documents/python/research2.csv'
output_dir = '/Users/apple/Documents/python/finalimages'
output_log = '/Users/apple/Documents/python/image_processing_log.csv'

process_images(csv_file, output_dir, output_log)
