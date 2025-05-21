from image_sorter import move_image_to_year
from video_sorter import move_video_to_year
import os

def process_folder(source_folder, dest_root):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            ext = file.lower()

            if ext.endswith((".jpeg",".jpg",".png",".heic")):
                move_image_to_year(file_path, dest_root)

            elif ext.endswith((".mp4",".MOV")):
                move_video_to_year(file_path, dest_root)

source_folder = r"C:\files\PyMediaSort\original Folder"
destination_root = r"C:\files\PyMediaSort\SortedPhotos"

process_folder(source_folder, destination_root)