from Tkinter import *
from PIL import ImageTk,Image
from random import randint
import os
root=Tk()
root.minsize(width=400,height=400)
op='1.jpg';
img=ImageTk.PhotoImage(Image.open(op));
panel=Label(root,image=img,width=300,height=300);
panel.pack(fill="both",expand="yes")
def solve():     
      k=randint(1,6)
      p=str(k)+ ".jpg"
      op=p;
      img2=ImageTk.PhotoImage(Image.open(op));
      panel.configure(image=img2)
      panel.image=img2;
button1=Button(root,text="Throw Dice",command=solve);
button1.pack(side=BOTTOM);
root.mainloop()
