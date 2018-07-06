import sys
import tkinter
from tkinter import *


def clear():
    txtentry.delete(0,END)
    return
root=Tk()
root.resizable("False","False")
frame=Frame(root)
frame.pack()
root.title("My Calculator")
num=StringVar()
f1=Frame(root)
f1.pack(side=TOP)
txtentry=Entry(f1,text=num,bd=20,insertwidth=5,font=50)
txtentry.pack(side=TOP)
b1=Button(f1,padx=16,pady=16,bd=8,text="1",fg="black",bg="light pink")
b1.pack(side=LEFT)
b2=Button(f1,padx=16,pady=16,bd=8,text="2",fg="black",bg="light pink")
b2.pack(side=LEFT)
b3=Button(f1,padx=16,pady=16,bd=8,text="3",fg="black",bg="light pink")
b3.pack(side=LEFT)
b4=Button(f1,padx=16,pady=16,bd=8,text="/",fg="black",bg="light pink")
b4.pack(side=LEFT)

f2=Frame(root)
f2.pack(side=TOP)

b5=Button(f2,padx=16,pady=16,bd=8,text="4",fg="black",bg="light pink")
b5.pack(side=LEFT)
b6=Button(f2,padx=16,pady=16,bd=8,text="5",fg="black",bg="light pink")
b6.pack(side=LEFT)
b7=Button(f2,padx=16,pady=16,bd=8,text="7",fg="black",bg="light pink")
b7.pack(side=LEFT)
b8=Button(f2,padx=16,pady=16,bd=8,text="*",fg="black",bg="light pink")
b8.pack(side=LEFT)

f3=Frame(root)
f3.pack(side=TOP)

b9=Button(f3,padx=16,pady=16,bd=8,text="7",fg="black",bg="light pink")
b9.pack(side=LEFT)
b10=Button(f3,padx=16,pady=16,bd=8,text="8",fg="black",bg="light pink")
b10.pack(side=LEFT)
b11=Button(f3,padx=16,pady=16,bd=8,text="9",fg="black",bg="light pink")
b11.pack(side=LEFT)
b12=Button(f3,padx=16,pady=16,bd=8,text="-",fg="black",bg="light pink")
b12.pack(side=LEFT)

f4=Frame(root)
f4.pack(side=TOP)


b13=Button(f4,padx=16,pady=16,bd=8,text="0",fg="black",bg="light pink")
b13.pack(side=LEFT)
b14=Button(f4,padx=16,pady=16,bd=8,text="=",fg="black",bg="light pink")
b14.pack(side=LEFT)
b15=Button(f4,padx=16,pady=16,bd=8,text="C",fg="black",bg="light pink",command=clear)
b15.pack(side=LEFT)
b16=Button(f4,padx=16,pady=16,bd=8,text="+",fg="black",bg="light pink")
b16.pack(side=LEFT)





root.mainloop()