import sys
import tkinter
from tkinter import *

# def __init__(self,num):
#     self.num=num

#1
def btnpress(numbers):
    global operator
    operator= operator + str(numbers)
    num.set(operator)

#2
def btnClear():
    global operator
    operator=""
    num.set("")

#3
def btnequal():
    global operator
    sumup = str(eval(operator))
    num.set(sumup)
    operator=""
operator=""



root=Tk()
root.resizable("False","False")
frame=Frame(root)
frame.pack()
root.title("My Calculator")
num = StringVar()

f1=Frame(root)
f1.pack(side=TOP)
textentry=Entry(f1,bd=10,text = num,width=21,font=("arial",18,"bold"),justify='right')
textentry.pack(side=TOP)
b1=Button(f1,padx=16,pady=16,bd=8,text="1",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(1))
b1.pack(side=LEFT)
b2=Button(f1,padx=16,pady=16,bd=8,text="2",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(2))
b2.pack(side=LEFT)
b3=Button(f1,padx=16,pady=16,bd=8,text="3",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(3))
b3.pack(side=LEFT)
b4=Button(f1,padx=16,pady=16,bd=8,text="/",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress("/"))
b4.pack(side=LEFT)

f2=Frame(root)
f2.pack(side=TOP)

b5=Button(f2,padx=16,pady=16,bd=8,text="4",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(4))
b5.pack(side=LEFT)
b6=Button(f2,padx=16,pady=16,bd=8,text="5",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(5))
b6.pack(side=LEFT)
b7=Button(f2,padx=16,pady=16,bd=8,text="6",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(6))
b7.pack(side=LEFT)
b8=Button(f2,padx=16,pady=16,bd=8,text="*",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress("*"))
b8.pack(side=LEFT)

f3=Frame(root)
f3.pack(side=TOP)

b9=Button(f3,padx=16,pady=16,bd=8,text="7",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(7))
b9.pack(side=LEFT)
b10=Button(f3,padx=16,pady=16,bd=8,text="8",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(8))
b10.pack(side=LEFT)
b11=Button(f3,padx=16,pady=16,bd=8,text="9",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress(9))
b11.pack(side=LEFT)
b12=Button(f3,padx=16,pady=16,bd=8,text="-",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda:btnpress("-"))
b12.pack(side=LEFT)

f4=Frame(root)
f4.pack(side=TOP)


b13=Button(f4,padx=16,pady=16,bd=8,text="0",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda :btnpress(0))
b13.pack(side=LEFT)
b14=Button(f4,padx=16,pady=16,bd=8,text="=",fg="black",bg="light pink",font=("arial",16,"bold"),command=btnequal)
b14.pack(side=LEFT)
b15=Button(f4,padx=16,pady=16,bd=8,text="C",fg="black",bg="light pink",command=btnClear,font=("arial",16,"bold"))
b15.pack(side=LEFT)
b16=Button(f4,padx=16,pady=16,bd=8,text="+",fg="black",bg="light pink",font=("arial",16,"bold"),command=lambda :btnpress("+"))
b16.pack(side=LEFT)





root.mainloop()