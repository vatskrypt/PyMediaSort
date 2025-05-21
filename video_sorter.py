import os
import shutil
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

def get_video_year(file_path):
    parser = createParser(file_path)
    if not parser:
        return None
    
    with parser:
        metadata = extractMetadata(parser)
        if metadata and metadata.has("creation_date"):
            creation_date=metadata.get("creation_date")
            return creation_date.strftime('%Y')
        return None

def move_video_to_year(video_path, dest_root):
    year = get_video_year(video_path)
    if not year:
        print(f"No creation dtae found for {video_path}. Skipping.")
        return
    
    year_folder= os.path.join(dest_root, year)
    os.makedirs(year_folder, exist_ok=True)

    filename = os.path.basename(video_path)
    dest_path = os.path.join(year_folder, filename)

    try:
        shutil.copy2(video_path,dest_path)
        print(f"copied '{filename}' to '{year_folder}'")
    except Exception as e:
        print(f"Failed to copy/move {video_path}: {e}")