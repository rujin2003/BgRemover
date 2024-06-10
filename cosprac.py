import pandas as pd
import requests
from io import BytesIO
from rembg import remove
from PIL import Image
import os

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.RequestException as e:
        print(f"failed to download image from {url}: {e}")
        return None

def process_images(csv_file, output_dir, output_log):
    df = pd.read_csv(csv_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results = []
    for index, row in df.iterrows():
        image_url = row['ResearcherDirectoryItem__ResearcherImage-u0xee6-2 src']
        researcher_name = row['researcher-name'].replace(" ", "_")

        image = download_image(image_url)
        if image:
            try:
                image_no_bg = remove(image)
                output_path = os.path.join(output_dir, f"{researcher_name}_{index}.png")
                image_no_bg.save(output_path)
                print(f"procesed and saved image: {output_path}")
                results.append({
                    "index": index,
                    "researcher_name": researcher_name,
                    "image_url": image_url,
                    "status": "success",
                    "output_path": output_path
                })
            except Exception as e:
                print(f"Failed to process image for {researcher_name}: {e}")
                results.append({
                    "index": index,
                    "researcher_name": researcher_name,
                    "image_url": image_url,
                    "status": "processing_failed",
                    "output_path": None
                })
        else:
            results.append({
                "index": index,
                "researcher_name": researcher_name,
                "image_url": image_url,
                "status": "download_failed",
                "output_path": None
            })

    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_log, index=False)
    print(f"Results saved to {output_log}")

csv_file = '/Users/apple/Documents/python/research2.csv' # add your csv file path 
output_dir = '/Users/apple/Documents/python/finalimages'  #create a image directory
output_log = '/Users/apple/Documents/python/image_processing_log.csv' # creating a log file 

process_images(csv_file, output_dir, output_log)
