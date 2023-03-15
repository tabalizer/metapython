#MetaPython - Image Metadata Extractor
This Python script extracts metadata from images, including date stamps, camera make and model, SHA256 hash value of the image, geolocation data, and other useful forensic data. The output is in a structured JSON format.

Dependencies
The script requires the following Python libraries:

exifread: To read the EXIF data from images
Pillow (PIL): To handle images
You can install these libraries using pip:

bash
Copy code
pip install exifread Pillow
Usage
Save the script as image_metadata_extractor.py.
Run the script using the following command:
bash
Copy code
python image_metadata_extractor.py
Enter the path to the image file when prompted:
javascript
Copy code
Enter the path to the image: /path/to/image.jpg
The script will output the extracted metadata in a structured JSON format:
css
Copy code
Metadata:
{
  "File Name": "image.jpg",
  "SHA256 Hash": "29f1b95c7eaa6d419515eb709d65db29b32c7b85a1d9de9fbf92b69c5521e949",
  "Date Stamp": "2020:08:12 08:24:12",
  "Date Digitized": "2020:08:12 08:24:12",
  "Date Modified": "2020:08:12 08:24:12",
  "Camera Make": "Canon",
  "Camera Model": "Canon EOS 5D Mark III",
  "Latitude": "48/1, 51/1, 3673/100",
  "Latitude Ref": "N",
  "Longitude": "2/1, 17/1, 5830/100",
  "Longitude Ref": "E",
  "Altitude": "100/1"
}
The output contains the file name, SHA256 hash, date stamps, camera make and model, and geolocation data (if available).
