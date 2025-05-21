import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_year(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
    except Exception as e:
        print(f"error opening image {image_path}: {e}")
        return None
    
    if not exif_data:
        print(f"No EXIF data found for {image_path}. Skipping.")
        return None
    
    date_taken = exif_data.get(36867) # 36867 is DateTimeOriginal
    # if not date_taken:
    #     date_taken = exif_data.get(306) # fallback datetime last modified
    if not date_taken:
        return None
    
    return date_taken.split(":")[0] #returns YYYY

def move_image_to_year(image_path, dest_root):
    year = get_image_year(image_path)
    if not year:
        print(f"No date found for {image_path}.Skipping.")
        return
    
    year_folder = os.path.join(dest_root, year)
    os.makedirs(year_folder, exist_ok=True)

    filename = os.path.basename(image_path)
    dest_path = os.path.join(year_folder, filename)

    try:
        shutil.copy2(image_path, dest_path)
        print(f"Copied '{filename}' to '{year_folder}'")
    except Exception as e:
        print(f"Error copying {image_path}: {e}")