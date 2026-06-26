"""
JPG to PNG Converter Agent
---------------------------
A simple tool that converts JPG/JPEG images into PNG format.

How to use it:
    python jpg_to_png_converter.py photo.jpg       <- convert one file
    python jpg_to_png_converter.py my_folder        <- convert every JPG in a folder

You need the Pillow library installed first:
    pip install Pillow
"""

import sys
import os
from PIL import Image


def convert_image(jpg_path):
    """Convert a single JPG file to PNG and save it right next to the original."""
    if not jpg_path.lower().endswith((".jpg", ".jpeg")):
        print(f"Skipping {jpg_path} (not a JPG file)")
        return

    try:
        img = Image.open(jpg_path)
        png_path = os.path.splitext(jpg_path)[0] + ".png"
        img.save(png_path, "PNG")
        print(f"Converted: {jpg_path} -> {png_path}")
    except Exception as error:
        print(f"Could not convert {jpg_path}: {error}")


def convert_folder(folder_path):
    """Convert every JPG file found inside a folder."""
    found_any = False
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg")):
            found_any = True
            convert_image(os.path.join(folder_path, filename))
    if not found_any:
        print("No JPG files found in that folder.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python jpg_to_png_converter.py <file_or_folder>")
        return

    target = sys.argv[1]

    if os.path.isdir(target):
        convert_folder(target)
    elif os.path.isfile(target):
        convert_image(target)
    else:
        print("That file or folder doesn't exist. Check the path and try again.")


if __name__ == "__main__":
    main()
