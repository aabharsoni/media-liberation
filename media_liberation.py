import os
import shutil
from PIL import Image

# Supported media extensions
IMAGE_EXT = ['.jpg', '.jpeg', '.png']
VIDEO_EXT = ['.mp4', '.mov', '.avi']
AUDIO_EXT = ['.mp3', '.wav']

def create_folders(base_path):
    """Create Images, Videos, and Audio folders if they don't exist"""
    folders = ['Images', 'Videos', 'Audio']
    for folder in folders:
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.mkdir(path)

def organize_files(base_path):
    """Move files into respective folders and rename them"""
    create_folders(base_path)
    count = {'Images': 1, 'Videos': 1, 'Audio': 1}

    for file in os.listdir(base_path):
        full_path = os.path.join(base_path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXT:
                new_name = f"image_{count['Images']:03d}{ext}"
                shutil.move(full_path, os.path.join(base_path, 'Images', new_name))
                count['Images'] += 1
            elif ext in VIDEO_EXT:
                new_name = f"video_{count['Videos']:03d}{ext}"
                shutil.move(full_path, os.path.join(base_path, 'Videos', new_name))
                count['Videos'] += 1
            elif ext in AUDIO_EXT:
                new_name = f"audio_{count['Audio']:03d}{ext}"
                shutil.move(full_path, os.path.join(base_path, 'Audio', new_name))
                count['Audio'] += 1

def compress_images(base_path):
    """Compress images to reduce size"""
    img_folder = os.path.join(base_path, 'Images')
    if not os.path.exists(img_folder):
        print("No images found to compress.")
        return
    for img in os.listdir(img_folder):
        img_path = os.path.join(img_folder, img)
        with Image.open(img_path) as im:
            im.save(img_path, optimize=True, quality=60)
    print("Images compressed successfully!")

def main():
    path = input("Enter the folder path to organize: ").strip()
    if not os.path.exists(path):
        print("Invalid Path!")
        return
    organize_files(path)
    choice = input("Do you want to compress images? (y/n): ").lower()
    if choice == 'y':
        compress_images(path)
    print("Media organized successfully!")

if __name__ == "__main__":
    main()
