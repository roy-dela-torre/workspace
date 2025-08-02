import os
from PIL import Image

# Directory containing PNG files
input_dir = r"C:\Users\roy\OneDrive\Documents\Workspace\projects\dibara_masonry\recent_project\optimize"

for filename in os.listdir(input_dir):
    if filename.lower().endswith('.png'):
        png_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        jpg_path = os.path.join(input_dir, jpg_filename)
        with Image.open(png_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_path, 'JPEG')