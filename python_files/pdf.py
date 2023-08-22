'''
created by Anuj Mishra 21/08/2023
# this par of code use only if you want to run only this file and have the downloadided json file for the study material
# Load the JSON data
'''
# import neccessory libraries
from fpdf import FPDF
import json
import requests
from PIL import Image
import os
from urllib.parse import urlparse
import shutil
import lang

'''
Uncomment below if you have direct json format for the study material reffer json file 
directory that is having AI geberated json files
'''

# with open('Pythagoras theorem.json', 'r', encoding='utf-8') as json_file:
#     data_hindi = json.load(json_file)
def makepdf(data,pdf_name):
    # # Create a directory to store downloaded images
    image_dir = "images"
    os.makedirs(image_dir, exist_ok=True)
    # Create a PDF document
    pdf = FPDF()
    pdf.add_page()
    # Set font and size for headings and content
    pdf.set_font("Arial", "B", 16)
    pdf.multi_cell(0, 10, data["Title"], 0, "C")
    pdf.set_font("Arial", "B", 14)

    '''Add headings, content, and images from JSON
    Now we will add the images and all the content into the pdf this may take time in downloading the images
    '''
    for section, content in data.items():
        if section != "Title":
            pdf.set_font("Arial", "B", 14)
            pdf.ln(10)
            pdf.cell(0, 10, section, 0, 1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, content["point"])
            if "img" in content and content["img"]:
                response = requests.get(content["img"])
                parsed_url = urlparse(content["img"])
                img_filename = os.path.basename(parsed_url.path)  # Extract filename from URL
                
                img_path = os.path.join(image_dir, img_filename)
                
                with open(img_path, "wb") as img_file:
                    img_file.write(response.content)
                try:   
                    img = Image.open(img_path)

                    # Convert image to RGB if it's not in RGB format
                    if img.mode != "RGB":
                        img = img.convert("RGB")

                    img_width = 180  # Adjust as needed"Arial"
                    img_height = (img_width / img.width) * img.height
                    pdf.image(img_path, x=15, y=pdf.get_y(), w=img_width, h=img_height)
                    pdf.ln(img_height)
                    # Close the PIL Image object to release the file handle
                    img.close()
                    # Delete the image file after it's been used
                    os.unlink(img_path)
                except:
                    img

    '''
    this code is for integrated the langchain for translation but unfortunately due to encoding issues not done yet due to lack of time
    although i have tried with number of prompts but othe language text contains some encodings that not supports the 'latin-1 encoding
    like hindi and others

    language = input("Enter the language of the pdf please write 'e' if it is English")
    data_hindi = lang.lgchain(json.dumps(data),language)
    print(data_hindi)
    data_hindi = data_hindi.encode('utf-8')
    data_hindi = json.loads(data_hindi)
    if data:
        pdf.set_font("Arial", "B", 16)
        pdf.multi_cell(0, 10, data["Title"], 0, "C")
        pdf.set_font("Arial", "B", 14)
    # Add headings, content, and images from JSON
    for section, content in data.items():
        if section != "Title":
            pdf.set_font("Arial", "B", 14)
            pdf.ln(10)
            pdf.cell(0, 10, section, 0, 1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, content["point"])
    '''
    # Save the PDF
    pdf.output(f"{pdf_name}.pdf")
    # Delete the image directory and its contents
    shutil.rmtree(image_dir)

# call the function
# makepdf(data_hindi,"photosynthesis")
