from tkinter import *
from tkinter import filedialog as fd
a= Tk()

def mfileopen():
    file1= fd.askopenfile()
    label= Label(text=file1).pack()
    file2 =file1.name
    file = open(file2)
    label2 =Label(text = file.read()).pack


button= Button(text ="open file",width =30,command=mfileopen).pack()
a.mainloop()
