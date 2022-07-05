from tkinter import *
root =Tk()
root.geometry("1200x800+50+50")

#sidebar frame
sideBar= LabelFrame(root,pady=3, padx=3,height=300,width=300,bg="#fff")
sideBar.place(x=0,y=5)
sideBar.pack_propagate(0)

b = Button(sideBar,text = "do not click here",font=100).place(anchor="W")
b = Button(sideBar,text = "do not click here",font=100).place(anchor="W")
b = Button(sideBar,text = "do not click here",font=100).place(anchor='W')
b = Button(sideBar,text = "do not click here",font=100).place(anchor='W')
b = Button(sideBar,text = "do not click here",font=100).place(anchor='W')
b = Button(sideBar,text = "do not click here",font=100).place(anchor='W')


root.mainloop()
