from tkinter import *
import math 
a =Tk()
a.title("Calclutor")
a.geometry("370x440+100+100")
n="arial",16,"bold"
a.configure(bg="#000")
#declaring my entry
entry =Entry(a, width=52,bd=5 , relief=SUNKEN)
entry.place(x=20,y=30)
#functions declaration
#function to the entry and insect it according
def entry_output(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) +str(number))
def but_add():
    global f_num
    global math
    math="addition"
    f_num = int(entry.get())
    entry.delete(0,END)
def but_sub():
    global f_num
    global math
    math="subtraction"
    f_num = int(entry.get())
    entry.delete(0,END)
def but_mul():
    global f_num
    global math
    math="multiplication"
    f_num = int(entry.get())
    entry.delete(0,END)
def but_div():
    global f_num
    global math
    math="divsion"
    f_num = int(entry.get())
    entry.delete(0,END)
def but_modul():
    global f_num
    global math
    math="modulo"
    f_num = int(entry.get())
    entry.delete(0,END)
def but_cos():
    global math
    global f_num
    math="cosine"
    f_num= int(entry.get())
    entry.delete(0,END)
def but_sin():
    global math
    global f_num
    math="sine"
    f_num= int(entry.get())
    entry.delete(0,END)
def but_tan():
    global math
    global f_num
    math="tan"
    f_num= int(entry.get())
    entry.delete(0,END)
def but_equal():
    global s_num
    s_num = int(entry.get())
    entry.delete(0,END)
    if math =="addition" :
        entry.insert (0,f_num+s_num) 
    if math =="subtraction" :
        entry.insert (0,f_num-s_num)
    if math =="multplication" :
        entry.insert (0,f_num * s_num)
    if math =="division" :
        entry.insert (0,f_num / s_num)
    if math =="modulo" :
        entry.insert (0,f_num+s_num)
    if math == "cosine":
        entry.insert(0, math.cos(f_num +s_num))
    if math == "sine":
        entry.insert(0, math.sin(f_num+s_num))
    if math == "tan":
        entry.insert(0, math.tan(f_num +s_num))
      
def but_clear():
    entry.delete(0,END)
    
#designing my button
   #row 1
B1 =Button(text="COS(x)",font= (n),relief=RAISED,height=2, bd= 3,width=5,command=but_tan).place(x=20,y=70)
B2 =Button(text="Tan(x)",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_cos).place(x=103,y=70)
B3 =Button(text="Sin(x)",font= (n),relief=RAISED,height=2, bd=3,width=5,command=but_sin).place(x=185,y=70)
B4 =Button(text="CLR",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_clear).place(x=265,y=70)     
#row 2
B1 =Button(text="1",font= (n),relief=RAISED,height=2, bd= 3,width=5,command=lambda:entry_output(1)).place(x=20,y=140)
B2 =Button(text="2",font= (n),relief=RAISED, height=2,bd=3,width=5,command=lambda:entry_output(2)).place(x=103,y=140)
B3 =Button(text="3",font= (n),relief=RAISED,height=2, bd=3,width=5,command=lambda:entry_output(3)).place(x=185,y=140)
B4 =Button(text="4",font= (n),relief=RAISED, height=2,bd=3,width=5,command=lambda:entry_output(4)).place(x=265,y=140)

#row 3
B5 =Button(text="5",font= (n),relief=RAISED,height=2, bd= 3,width=5,command=lambda:entry_output(5)).place(x=20,y=210)
B6 =Button(text="6",font= (n),relief=RAISED, height=2,bd=3,width=5,command=lambda:entry_output(6)).place(x=103,y=210)
B7 =Button(text="7",font= (n),relief=RAISED,height=2, bd=3,width=5,command=lambda:entry_output(7)).place(x=185,y=210)
B_plus =Button(text="+",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_add).place(x=265,y=210)

#row 4
B8=Button(text="8",font= (n),relief=RAISED,height=2, bd= 3,width=5,command=lambda:entry_output(8)).place(x=20,y=280)
B9 =Button(text="9",font= (n),relief=RAISED, height=2,bd=3,width=5,command=lambda:entry_output(9)).place(x=103,y=280)
B_minus =Button(text="-",font= (n),relief=RAISED,height=2, bd=3,width=5,command=but_sub).place(x=185,y=280)
B_mul =Button(text="x",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_mul).place(x=265,y=280)

#row 5
B0 =Button(text="0",font= (n),relief=RAISED,height=2, bd= 3,width=5,command=lambda:entry_output(0)).place(x=20,y=350)
B_div =Button(text="/",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_div).place(x=105,y=350)
Bmo=Button(text="%",font= (n),relief=RAISED,height=2, bd=3,width=5,command=but_modul).place(x=185,y=350)
B_equal=Button(text="=",font= (n),relief=RAISED, height=2,bd=3,width=5,command=but_equal).place(x=265,y=350)








a.mainloop()
