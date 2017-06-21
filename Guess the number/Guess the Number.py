from Tkinter import *
from easy import *

def easy2():
    easy(100);

def moderate():
    easy(10000);

def hard():
    easy(100000);

strt=Tk()
strt.minsize(width=600,height=800)
label1=Label (strt,text="Guess the Number",font=(None,18),width=50,height=3);
label2=Label(strt,text="Choose your Level",font=(None,12),width=50,height=5);
button1=Button(strt,text="Easy (1-100)",command=easy2,width=50,height=7)
button2=Button(strt,text="Moderate (1-10000)",command=moderate,width=50,height=7);
button3=Button(strt,text="Hard (1-100000)",command=hard,width=50,height=7);
label1.grid(row=0,column=2)
label2.grid(row=1,column=2)
button1.grid(row=2,column=2)
button2.grid(row=3,column=2)
button3.grid(row=4,column=2)
label3=Label (strt,text="By Jatin Miglani");
label3.grid(row=5,column=2);
strt.mainloop()