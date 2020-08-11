from tkinter import *
from tkinter.filedialog import askopenfilename


def open_file_dialog():
    path = askopenfilename()
    return path



def dialog_query_file():
    root = Tk()
    b1 = Button(root, text='Open', command=open_file_dialog)
    b1.pack()
    root.mainloop()
