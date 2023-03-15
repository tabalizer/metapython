#MetaPython - Image Metadata Extractor<br>
This Python script extracts metadata from images, including date stamps, camera make and model, SHA256 hash value of the image, geolocation data, and other useful forensic data. The output is in a structured JSON format.<br>

Dependencies<br>
The script requires the following Python libraries:<br>

exifread: To read the EXIF data from images<br>
Pillow (PIL): To handle images<br>
You can install these libraries using pip:<br>

bash<br>
Copy code<br>
pip install exifread Pillow<br>

Usage<br>
Save the script as image_metadata_extractor.py<br>
Run the script using the following command:<br>

bash<br>
Copy code<br>
python image_metadata_extractor.py<br>
Enter the path to the image file when prompted:<br>
javascript<br>
Copy code<br>
Enter the path to the image: /path/to/image.jpg<br>
The script will output the extracted metadata in a structured JSON format:<br>
css<br>
Copy code<br>

Output Example<br>
Metadata:<br>
{<br>
  "File Name": "image.jpg",<br>
  "SHA256 Hash": "29f1b95c7eaa6d419515eb709d65db29b32c7b85a1d9de9fbf92b69c5521e949",<br>
  "Date Stamp": "2020:08:12 08:24:12",<br>
  "Date Digitized": "2020:08:12 08:24:12",<br>
  "Date Modified": "2020:08:12 08:24:12",<br>
  "Camera Make": "Canon",<br>
  "Camera Model": "Canon EOS 5D Mark III",<br>
  "Latitude": "48/1, 51/1, 3673/100",<br>
  "Latitude Ref": "N",<br>
  "Longitude": "2/1, 17/1, 5830/100",<br>
  "Longitude Ref": "E",<br>
  "Altitude": "100/1"<br>
}<br>

The output contains the file name, SHA256 hash, date stamps, camera make and model, and geolocation data (if available).
