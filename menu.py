from tkinter import *
from tkinter.filedialog import askopenfilename

def dialog_query_file():
    root = Tk()
    root.withdraw()
    root.update()
    
    file_path = askopenfilename()
    root.destroy() 
    return file_path
