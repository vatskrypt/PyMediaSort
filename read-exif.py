from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil

def move_image_to_year(image_path, dest_root):
    with Image.open(image_path) as image:
        exif_data = image._getexif()
    
    if exif_data is None:
        print(f"No EXIF data found for {image_path}. Skipping.")
        return

    date_taken = exif_data.get(36867)  # DateTimeOriginal

    if date_taken is None:
        print(f"No date taken found for {image_path}. Skipping.")
        return

    year = date_taken.split(":")[0]
    year_folder = os.path.join(dest_root, year)
    os.makedirs(year_folder, exist_ok=True)

    filename = os.path.basename(image_path)
    dest_path = os.path.join(year_folder, filename)

    shutil.move(image_path, dest_path)
    print(f"Moved '{filename}' to '{year_folder}'")
