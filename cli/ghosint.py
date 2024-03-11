from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import subprocess
import argparse
import requests
import tqdm
import sys

def display_logo():
    print(r"""          
  ________  ___ ___ ________    _________.___ __________________
 /  _____/ /   |   \\_____  \  /   _____/|   |\      \__    ___/
/   \  ___/    ~    \/   |   \ \_____  \ |   |/   |   \|    |   
\    \_\  \    Y    /    |    \/        \|   /    |    \    |   
 \______  /\___|_  /\_______  /_______  /|___\____|__  /____|   
        \/       \/         \/        \/             \/         
    """)

def main_menu():
    print("Welcome to GHOSINT")
    print("Below is a list of tools available. Please select one by entering its number:")

    tool_descriptions = [
        "Exif",
        "Email",
        "Phone",
        "Address",
        "Username",
        "Dark Web",
        "Domain/IP",
        "Mac Address",
        "Social Media",
        "Public Records",
        "Google Dorking",
        "Transportation",
        "Business Records",
        "Internet Archives",


        # Add descriptions for all tools, up to 30
    ]

    for i in range(1, len(tool_descriptions) + 1):
        print(f"{i}. {tool_descriptions[i-1]}")


    try:
        choice = int(input("Enter the number of the tool you want to use: "))
        if choice == 1:
            tool_1_function()
        elif choice == 5:  # This is where we handle the option for tool 5
            tool_5_function()
        elif 1 < choice <= len(tool_descriptions):
            print(f"You selected Tool {choice} - {tool_descriptions[choice-1]}")
            # Placeholder for other tool function calls
            # You would add similar conditions here for other tools, for example:
            # if choice == 2: tool_2_function()
        else:
            print("Invalid choice, please select a valid number.")
    except ValueError:
        print("Please enter a valid number.")


def get_exif_data(image_path):
    """
    Extracts EXIF data from an image file.

    :param image_path: Path to the image file
    :return: A dictionary of EXIF data if available, otherwise an error message
    """
    try:
        image = Image.open(image_path)
        info = image._getexif()
        if not info:
            return "No EXIF data found in the image."

        exif_data = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {GPSTAGS.get(t, t): value[t] for t in value}
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
        return exif_data
    except IOError:
        return f"Error opening file at '{image_path}'. Check if the file exists and the path is correct."

def print_specific_exif_data(exif_data):
    """
    Prints specified fields of EXIF data.

    :param exif_data: Dictionary containing EXIF data
    """
    desired_fields = [
        "Make", "Model", "Orientation", "DateTimeOriginal", "DateTimeDigitized",
        "ShutterSpeedValue", "ApertureValue", "BrightnessValue", "ExposureBiasValue",
        "MeteringMode", "Flash", "FocalLength", "ColorSpace", "PixelXDimension",
        "PixelYDimension", "GPSInfo",
    ]

    print("EXIF Data:")
    for field in desired_fields:
        print(f"{field}: {exif_data.get(field, 'Not available')}")

def tool_1_function():
    """
    The main function to extract and print EXIF data for an image.
    """
    print("EXIF Data Extraction Tool")
    image_path = input("Enter the path to your image: ")
    result = get_exif_data(image_path)

    # Check if the result is a dictionary (indicating successful extraction) or an error message.
    if isinstance(result, dict):
        print_specific_exif_data(result)
    else:
        print(result)  # Prints the error message from get_exif_data

def tool_5_function():
    print("https://whatsmyname.app/")
    print("test")



if __name__ == "__main__":
    display_logo()
    main_menu()
