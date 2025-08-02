import os
from PIL import Image

# Folder containing images to optimize
IMAGE_DIR = r"C:\Users\roy\OneDrive\Documents\windowworksnc"
MAX_SIZE_KB = 300
MAX_SIZE_BYTES = MAX_SIZE_KB * 1024

def optimize_image(image_path):
    try:
        with Image.open(image_path) as img:
            img_format = img.format
            quality = 95
            step = 5
            temp_path = image_path + ".opt"
            # Try reducing quality first
            while True:
                img.save(temp_path, format=img_format, quality=quality, optimize=True)
                if os.path.getsize(temp_path) <= MAX_SIZE_BYTES or quality <= 10:
                    break
                quality -= step
            # If still too large, resize image
            if os.path.getsize(temp_path) > MAX_SIZE_BYTES:
                with Image.open(image_path) as img_resize:
                    width, height = img_resize.size
                    while os.path.getsize(temp_path) > MAX_SIZE_BYTES and width > 100 and height > 100:
                        width = int(width * 0.9)
                        height = int(height * 0.9)
                        img_resized = img_resize.resize((width, height), Image.LANCZOS)
                        img_resized.save(temp_path, format=img_format, quality=quality, optimize=True)
            os.replace(temp_path, image_path)
            print(f"Optimized: {image_path} ({os.path.getsize(image_path)//1024} KB)")
    except Exception as e:
        print(f"Failed to optimize {image_path}: {e}")

def is_image_file(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png'))

def optimize_images_in_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if is_image_file(file):
                image_path = os.path.join(root, file)
                if os.path.getsize(image_path) > MAX_SIZE_BYTES:
                    optimize_image(image_path)

if __name__ == "__main__":
    optimize_images_in_folder(IMAGE_DIR)