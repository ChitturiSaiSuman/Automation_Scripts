# Script to copy the contents of a file to clipboard

import pyperclip
import sys
import mimetypes
import os


if __name__ == '__main__':

    # Get the name of file from command line
    try:
        name_of_file = sys.argv[1]
    except IndexError:
        print('Please provide a file name')
        sys.exit()

    # Check if file exists
    if not os.path.exists(name_of_file):
        print('File does not exists')
        sys.exit()

    # Check if provided argument is a folder
    if os.path.isdir(name_of_file):
        print(name_of_file + ' is a directory')
        print('Please provide a file name')
        sys.exit()

    # Check if provided argument is a CP file
    # Examples: STDIN, STDOUT, STDEXPOUT, STDERR
    if "." in name_of_file:
        # Check if the file is a valid text file
        if "text" not in mimetypes.guess_type(name_of_file)[0]:
            print('File type not supported')
            sys.exit(1)
    
    # Control reached here signifies two cases
    # Case 1: File is a text file
    # Case 2: File is a CP file

    
    # Open the file and read the contents
    file = open(name_of_file, 'r')
    contents = file.read()
    file.close()

    # Copy the contents to clipboard
    pyperclip.copy(contents)
    print('Copied contents of ' + name_of_file + ' to clipboard.')
    pyperclip.waitForPaste(15)