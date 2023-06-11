from tkinter import *
from tkinter import filedialog as fd
import hashlib
root=Tk()
root.geometry("250x190")
root.configure(background="lemon chiffon")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title=" Open Text File", filetypes=(("Text Files", ".txt"),))
    print(text_file)
    read_file = open(text_file,'r')
    paragraph=read_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    md5_file = open("md5.*txt",'w')
    md5_file.write(file_hexd)
    print(file_hexd)
    
    md5_file.close
    
    
def apply_sha256():
    print("SHA function")
    text_file = fd.askopenfilename(title=" Open Text File", filetypes=(("Text Files", ".txt"),))
    print(text_file)
    read_file = open(text_file,'r')
    paragraph=read_file.read()
    file_result = hashlib.sha256(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    sha256_file = open("sha256.*txt",'w')
    sha256_file.write(file_hexd)
    print(file_hexd)
    
    sha256_file.close