# Script to copy the contents of a file to clipboard

import pyperclip
import sys
import mimetypes


if __name__ == '__main__':

    # Get the name of file from command line
    try:
        name_of_file = sys.argv[1]
    except IndexError:
        print('Please provide a file name')
        sys.exit()
    
    # Check if the file is a valid text file
    if "text" not in mimetypes.guess_type(name_of_file)[0]:
        print('File type not supported')
        sys.exit(1)
    
    # Open the file and read the contents
    file = open(name_of_file, 'r')
    contents = file.read()
    file.close()

    # Copy the contents to clipboard
    pyperclip.copy(contents)
    print('Copied contents of ' + name_of_file + ' to clipboard.')
    pyperclip.waitForPaste(15)