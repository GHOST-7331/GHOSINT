# pip install Pillow exifread piexif
# python exifGHOSINT.py /path/to/your/image.jpg

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = {}
        info = image._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]
                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
            return exif_data
        else:
            return None
    except IOError as e:
        return f"Error opening file: {e}"

def print_specific_exif_data(exif_data):
    # Define the desired metadata fields to display
    desired_fields = [
        "Make",
        "Model",
        "Orientation",
        "DateTimeOriginal",
        "DateTimeDigitized",
        "ShutterSpeedValue",
        "ApertureValue",
        "BrightnessValue",
        "ExposureBiasValue",
        "MeteringMode",
        "Flash",
        "FocalLength",
        "ColorSpace",
        "PixelXDimension",
        "PixelYDimension",
        "GPSInfo",
    ]

    if exif_data:
        for field in desired_fields:
            if field in exif_data:
                print(f"{field}: {exif_data[field]}")
            else:
                print(f"{field}: Not available")
    else:
        print("No EXIF data found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 exif_extractor.py <image_path>")
    else:
        image_path = sys.argv[1]
        exif_data = get_exif_data(image_path)
        print_specific_exif_data(exif_data)
