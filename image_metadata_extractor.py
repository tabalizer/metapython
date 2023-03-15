import exifread
import hashlib
from PIL import Image
import json
import os

def get_exif_data(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    return tags

def get_sha256_hash(image_path):
    with open(image_path, 'rb') as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()

def extract_metadata(image_path):
    exif_data = get_exif_data(image_path)
    metadata = {
        "File Name": os.path.basename(image_path),
        "SHA256 Hash": get_sha256_hash(image_path),
    }

    tag_map = {
        "EXIF DateTimeOriginal": "Date Stamp",
        "EXIF DateTimeDigitized": "Date Digitized",
        "Image DateTime": "Date Modified",
        "Image Make": "Camera Make",
        "Image Model": "Camera Model",
        "GPS GPSLatitude": "Latitude",
        "GPS GPSLatitudeRef": "Latitude Ref",
        "GPS GPSLongitude": "Longitude",
        "GPS GPSLongitudeRef": "Longitude Ref",
        "GPS GPSAltitude": "Altitude",
    }

    for tag, value in exif_data.items():
        if tag in tag_map:
            metadata[tag_map[tag]] = str(value)

    return metadata

def main():
    image_path = input("Enter the path to the image: ")
    metadata = extract_metadata(image_path)
    output = json.dumps(metadata, indent=2)
    print("\nMetadata:")
    print(output)

if __name__ == "__main__":
    main()
