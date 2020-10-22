import os
import argparse

def rename_files(path_name):
    for idx, filename in enumerate(os.listdir(path_name)):
        name, ext = os.path.splitext(filename)
        print(idx)
        if filename.endswith('.pdf'):
                os.rename(os.path.join(path_name, filename), os.path.join(path_name, str(idx)+'.pdf') )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", required=True, help="path to the PDF files")
    args = parser.parse_args()

    # INPUT DIRECTORY
    _src = args.directory

    # RENAME FILES
    rename_files(_src)
