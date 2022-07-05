from tkinter import  *
from tkinter import colorchooser
a=Tk()
color = colorchooser.askcolor()
label =Label (text ="your chosen color ", bg=color).pack()



#button =Button(text="choose color", command ="mcolor" ,width=30).pack()
a.mainloop()
