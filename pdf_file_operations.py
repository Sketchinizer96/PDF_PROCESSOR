import os
import PyPDF2
from os import path
import re
import time
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import warnings

from PyPDF2.utils import PdfReadWarning


def file_open():
    y = 0
    while y != 1:
        print('Please mention the complete path of the PDF to fetch the file ')
        fp_path = input(f'Path:\t')
        pattern = re.compile('^[A-Z][:]{1}\\\(.*)')
        match = pattern.match(fp_path)
        if match:
            y = 1
        else:
            print('Please enter the correct path')
            time.sleep(3)
    k = 0
    while k != 1:
        file_name = input(f'Please enter the File Name to be opened:\t')
        file_path = fr'{fp_path}'f'\\{file_name}'
        file_exist = path.exists(fr'{file_path}')
        if file_exist:
            k = 1
        else:
            print('Entered file doesnot exist. Please check and try again')
            time.sleep(3)
    return file_path

    # num = int(input('Please enter the number of files to be merged:'))

    # for i in range(0, num):
    #   globals()['input%s' % i] = file_open()


def pdf_merge():
    merger = PdfFileMerger(strict=False)
    print('Please provide details of First file')
    file_1 = file_open()
    merger.append(PdfFileReader(file_1, 'rb'))
    print('Please provide details of Second file')
    file_2 = file_open()
    merger.append(PdfFileReader(file_2, 'rb'))
    merged_file = merger.write('Merged_file.pdf')
    return merged_file


# pdf_merge()

def encrypt_pdf():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=PdfReadWarning)
    file_1 = file_open()
    pdfFileObj = open(file_1, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

    output_pdf = PdfFileWriter()
    output_pdf.appendPagesFromReader(pdfReader)
    k: int = 0
    while k != 1:
        password = input(f'Please enter the password for encryption :\t')
        pass_len = len(password)
        if pass_len >= 6 <= 10:
            output_pdf.encrypt(f'{password}')
            k = 1
        else:
            print('Please enter a password between 8 to 10 characters ')
    file_name_encrypt = input("Please enter the file name for encryption : ")
    with open(f"{file_name_encrypt}", "wb") as out_file:
        output_pdf.write(out_file)
        print("File has been Encrypted ")
    return out_file


# encrypt_pdf()

# def decrypt_pdf():
#   file_1 = file_open()
#  pdfFileObj = open(file_1, 'rb')
# reader = PyPDF2.PdfFileReader(pdfFileObj)
# password = input('Please enter the password to decrypt : ')
# if reader.isEncrypted:
#    try:
#       out_file = reader.decrypt(password)
#   except NotImplementedError:
#      command = f"qpdf --password='{password}' --decrypt {file_1};"
#      os.system(command)
# return reader

exit_id: str = 'No'
while 'Yes' != exit_id:
    print("-" * 100)
    print("*" * 10 + " PDF Processing Operations " + "*" * 10)
    print(
        f' 1 : Create A Merged PDF  \n 2 : Encrypt PDF ')
    print("-" * 100)
    data_input = input(f'Please enter the Choice : \t')
    if data_input == '1':
        pdf_merge()
    elif data_input == '2':
        encrypt_pdf()
    else:
        print('No options selected')
    exit_id = input('Do you want  to End this (Yes/No):  ')
print(f'PDF Processing is exiting........ ')
