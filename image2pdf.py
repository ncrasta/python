"""
Converts image files to pdf
usage:
python3 image2pdf.py -d path_to_file_folder
"""
import os
import argparse
from PIL import Image

def convert_image_pdf(path_name):
    for idx, filename in enumerate(os.listdir(path_name)):
        name, ext = os.path.splitext(filename)
        if ext in ['.jpg', '.PNG', '.jpeg']:
            image = Image.open( os.path.join(path_name,filename) )
            img = image.convert('RGB')
            img.save(os.path.join(path_name, name + '.pdf'))
            os.remove(os.path.join(path_name, filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", required=True, help="path to the PDF files")
    args = parser.parse_args()

    # INPUT DIRECTORY
    src = args.directory

    # CONVERT ALL IMAGES TO PDFs
    convert_image_pdf(os.path.join(src))
