"""
Rotates a list of pdf files from an input direcotry by 90 degrees clockwise 
and saves into output directory

Usage
python3 rotate_pdf.py -d path_to_rotate_pdf_folder
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
import argparse
import os, sys

def rotate_images(path_in, path_out):
    for x in os.listdir(path_in):
        if x.endswith('.pdf'):
            pdf_input = open(os.path.join(path_in , x), 'rb')
            pdf_reader = PdfFileReader(pdf_input)
            pdf_writer = PdfFileWriter()
            for pagenum in range(pdf_reader.numPages):
                page = pdf_reader.getPage(pagenum)
                page.rotateClockwise(90)
                pdf_writer.addPage(page)
        pdf_out = open( os.path.join(path_out, x), 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", required=True, help="path to the PDF files")
    args = parser.parse_args()

    # Input directory
    _src = args.directory

    # Rotate pdfs
    sp = sys.platform.lower()
    if sp in {"linux", "linux2"}:
        rotate_images(os.path.join(_src))
    elif sp in {"darwin", "win32"}:
        print("Not Linux platform")
