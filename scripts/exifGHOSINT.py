# pip install Pillow
# python exifGHOSINT.py /path/to/your/image.jpg

from PIL import Image
from PIL.ExifTags import TAGS
import sys

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = {}
        info = image._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
            return exif_data
        else:
            return "No EXIF data found."
    except IOError:
        return "Error opening file."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python exif_extractor.py <image_path>")
    else:
        image_path = sys.argv[1]
        exif_data = get_exif_data(image_path)
        print(exif_data)
