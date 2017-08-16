import os, PyPDF2

import send2trash

def get_directory():
    while True:
        directory = input("Input directory: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')
        
def get_encryption():
    return input("Enter the encryption key: ")


def append_to_filename(filename):
    return filename.split('.pdf')[0] + '_encrypted.pdf'

def write_to_pdf(new_file, pdf_writer, pdf_reader):
    for page_number in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_number))
    pdf_writer.write(new_file)


def create_encrypted_pdfs(encryption_key, directory):
    for dir_name, subdir_list, file_list in os.walk(directory):
        for filename in file_list:
            if filename.endswith('.pdf'):
                                
                absolute_directory = os.path.abspath(dir_name)
                absolute_filename  = os.path.join(absolute_directory, filename)
                absolute_file      = open(absolute_filename, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(absolute_file)

                if not pdf_reader.isEncrypted:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    os.chdir(absolute_directory)
                    new_file = open(append_to_filename(filename), 'wb')
                    pdf_writer.encrypt(encryption_key)
                    write_to_pdf(new_file, pdf_writer, pdf_reader)
                    new_file.close()
                    absolute_file.close()
                    send2trash.send2trash(absolute_filename)