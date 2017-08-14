#Seong Ma


import functions 

'''
This program will allow a user to input a directory
and a password, and will then walk through the directory
and its subdirectories and encrypt all found pdf files 
with the password, encrypted files will contain the same
filename but with _encrypted appended. The original files
will be sent to the recycle bin.
'''

if __name__ == '__main__':
    directory = functions.get_directory()
    
    