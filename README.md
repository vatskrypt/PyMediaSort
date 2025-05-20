# PyMediaSort

**PyMediaSort** is a Python tool that scans your photo library, reads the original date taken (from EXIF metadata), and sorts the files into folders by year — perfect for backup or archival purposes.

---

## Features

- Reads EXIF metadata to extract "Date Taken"
- Automatically creates folders like `2021/`, `2022/`, etc.
- Moves (or optionally copies(wip)) files to the correct folder
- Supports common image formats (JPEG, PNG)
- Windows GUI in progress (built with Tkinter)
- Planned support for video files (WIP)

---

## Planned Features / Vision

- Fully-featured Google Photos alternative, fully local (no cloud)
- Designed to run on a home server (headless or minimal UI)
- Companion mobile apps for Android/iOS with modern native UIs
- Advanced tagging and grouping (faces, locations, scenes, etc.)
- Smart categorization (e.g., beach, mountain, party)
- AI-based image captioning (e.g., “a cat sitting on a couch”)
- Geo-visualization: plot photos with GPS data on an interactive map (e.g., Google Maps or Folium)

---

## 🚀 How to Use

1. Make sure you have Python 3 installed.
2. Install dependencies:

```bash
pip install Pillow
```
