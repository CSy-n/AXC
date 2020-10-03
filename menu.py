from tkinter.filedialog import askopenfilename as open_file_name
from tkinter.filedialog import askdirectory as open_directory_name
from tkinter import Tk


# Reference: https://pythonspot.com/tk-file-dialogs/

def dialog_query_file(initial_directory="."):
    root = Tk()
    root.withdraw()
    root.update()

    file_path = open_file_name(initialdir=initial_directory,title= "Select file",
                                   filetypes = (("All files","*.*"),("jpeg files","*.jpg")))
    root.destroy() 
    return file_path


def dialog_query_directory():
   root = Tk()
   root.withdraw()
   root.update()

   file_path = open_directory_name()
   root.destroy() 
   return file_path

                               
