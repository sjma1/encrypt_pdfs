import os, PyPDF2

from send2trash import send2trash

def get_directory():
    while True:
        directory = input("Input directory: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')
        
def get_encryption():
    return input("Enter the encryption key: ")

def create_encrypted_pdfs(encryption_key, directory):
    for dir_name, subdir_list, file_list in os.walk(directory):
        for filename in file_list:
            if filename.endswith('.pdf'):
                pass