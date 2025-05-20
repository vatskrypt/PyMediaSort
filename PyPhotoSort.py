import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

def move_image_to_year(image_path, dest_root):
    try:
        with Image.open(image_path) as image:
            exif_data = image._getexif()
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return

    if not exif_data:
        print(f"No EXIF data found for {image_path}. Skipping.")
        return

    date_taken = exif_data.get(36867)  # 36867 is DateTimeOriginal

    if not date_taken:
        print(f"No 'Date Taken' found for {image_path}. Skipping.")
        return

    year = date_taken.split(":")[0]
    year_folder = os.path.join(dest_root, year)
    os.makedirs(year_folder, exist_ok=True)

    filename = os.path.basename(image_path)
    dest_path = os.path.join(year_folder, filename)

    try:
        shutil.move(image_path, dest_path)
        print(f"Moved '{filename}' to '{year_folder}'")
    except Exception as e:
        print(f"Failed to move {image_path}: {e}")

def process_folder(source_folder, dest_root):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(root, file)
                move_image_to_year(file_path, dest_root)

# Example usage
source_folder = r"C:\files\Phone\DCIM\Camera"
destination_root = r"C:\files\Phone\DCIM\CamByYear"

process_folder(source_folder, destination_root)
