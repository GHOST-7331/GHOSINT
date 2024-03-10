# pip install Pillow
# python exifGHOSINT.py /path/to/your/image.jpg

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys

def get_exif_data(image_path):
    """Extracts EXIF data from an image and returns it as a dictionary."""
    try:
        image = Image.open(image_path)  # Attempt to open the image
        exif_data = {}
        info = image._getexif()  # Try to extract EXIF data
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)  # Decode the tag
                if decoded == "GPSInfo":
                    # Special handling for GPS data, if present
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]
                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
            return exif_data
        else:
            return None  # Indicate no EXIF data was found
    except IOError:
        print("Error opening file:", image_path)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <image_path>")
    else:
        image_path = sys.argv[1]
        exif_data = get_exif_data(image_path)
        if exif_data:
            # If EXIF data was found, print it to the console
            for tag, value in exif_data.items():
                print(f"{tag}: {value}")
        else:
            print("No EXIF data found.")

