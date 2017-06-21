from random import randint
from Tkinter import *
from functools import *
from Tkinter import *

trns=0
mode=0
trnno=0
p1="abc"
p2="abc"
t1=0
t2=0

def fun (diff,strtw,player1,player2):
    global p1
    global p2
    p1=player1.get("1.0",END);
    p2=player2.get("1.0",END);
    strtw.destroy()
    print(p1);
    print(p2);
    play(diff)
    

def askplayernames (diff):
    strtw=Tk();
    strtw.minsize(width=400,height=400);
    l3=Label(strtw,text="Enter Player Names",font=(None,16),height=2,width=30);
    l3.grid(row=0,column=0,sticky=E);
    l1=Label(strtw,text="Player1: ",font=(None,14),height=3,width=10);
    l2=Label(strtw,text="Player2: ",font=(None,14),height=3,width=10);
    l1.grid(row=1,column=0,sticky=W)
    l2.grid(row=2,column=0,sticky=W)
    player1=Text(strtw,width=20,height=2);
    player2=Text(strtw,width=20,height=2);
    player1.grid(row=1,column=0,sticky=E)
    player2.grid(row=2,column=0,sticky=E)
    fun_with_args=partial(fun,diff=diff,strtw=strtw,player1=player1,player2=player2);
    b1=Button(strtw,text="Play",font=(None,14),width=30,height=3,command=fun_with_args);
    b1.grid(row=3,column=0,sticky=E)
    strtw.mainloop()

def mode1(diff,strtw):
    global mode
    mode=0;
    strtw.destroy();
    play(diff)

def mode2(diff,strtw):
    global mode
    mode=1;
    strtw.destroy();
    askplayernames(diff)

def findmode(diff):
    strtw=Tk();
    strtw.minsize(width=400,height=400);
    mode1_with_arg=partial(mode1,diff=diff,strtw=strtw);
    mode2_with_arg=partial(mode2,diff=diff,strtw=strtw);
    b1=Button(strtw,text="Single Player",width=20,height=2,command=mode1_with_arg,font=(None,16))
    b2=Button(strtw,text="Two Player",width=20,height=2,command=mode2_with_arg,font=(None,16))
    l1=Label(strtw,text="",height=3);
    l1.grid(row=2,column=0);
    l2=Label(strtw,text="",height=3);
    l2.grid(row=0,column=0);
    l3=Label(strtw,text="",height=1,width=10);
    l3.grid(row=1,column=0);
    l4=Label(strtw,text="",height=1,width=10);
    l4.grid(row=3,column=0);
    b1.grid(row=1,column=1,sticky=W)
    b2.grid(row=3,column=1,sticky=W)
    strtw.mainloop();

def reset(strt,strt2,D):
    global mode
    global trnnno
    mode=0
    trnno=0
    strt.destroy();
    strt2.destroy();
    easy(D);

def changemode(root,root2,diff):
    global trnno
    trnno=1
    root.destroy()
    root2.destroy()
    play(diff)

def solve(k,root,label1,label2,entry1,diff):
    n=int(entry1.get("1.0",END));
    global trns
    trns=trns + 1
    if n>k:
       label1.config(text="Too High");
    elif n<k:
       label1.config(text="Too Low");
    else:
       label1.config(fg="green");
       label1.config(text="Correct!! The number is " +str(n));
       root2=Tk()
       root2.minsize(300,300);
       label8=Label(root2,text=" ",font=(None,14))
       label8.pack()
       label7=Label(root2,text="You took "+str(trns)+" turns to guess it!",font=(None,12));
       label7.pack(fill=X)
       label9=Label (root2,text="",font=(None,14))
       label10=Label(root2,text="",font=(None,14))
       label9.pack()
       label10.pack()
       reset_with_arg=partial(reset,strt=root,strt2=root2,D=diff);
       button2=Button(root2,text="");
       global mode
       global t1
       if mode==0:
          if trnno==1:
             if t1<trns:
                label8.config(text=p1+" Wins!");
             elif t1==trns:
                label8.config(text="It is a Tie!");
             else:
                label8.config(text=p2+" Wins!");
          label9.config (text=p1+" took " +str(t1) + " turns!")
          label10.config(text=p2+" took " +str(trns) + " turns!")
          button2.config(text="Play Again?",command=reset_with_arg)
       else:
          t1=trns
          trns=0
          changemode_with_args=partial(changemode,root=root,root2=root2,diff=diff)
          button2.config(text="Second Player Ready?",command=changemode_with_args)
       button2.pack(side=BOTTOM)
       root2.mainloop()
    label2.config (text="Turns: " +str(trns))

def easy(diff):
        findmode(diff)

def play(diff):
	root=Tk()
        root.minsize(width=800, height=600)
        l1=Label (root,text="",font=(None,22),width=50)
        global mode
        if mode==1:
           global p1
           global p2
           if trnno==0:
              l1.config(text=p1+" Turn")
           else:
              l1.config(text=p2+" Turn")
              mode=0
        l1.grid(row=0,column=400)
	label1=Label (root,text="",fg="red",font=(None,22));
	label2=Label (root,text="Turns: 0",width=50,height=5,font=(None,22));
	entry1=Text(root,width=40,height=4,font=(None,22));
	label2.grid(row=2,column=400)
	label1.grid(row=1,column=400) 
	label3=Label(root,text="Enter Any Number" + "(1-" + str(diff) +") ",font=(None,22),height=3);
	label3.grid(row=3,column=400)
	entry1.grid(row=4,column=400);
	k=randint(1,diff);
        global trns
        trns=0
        solve_with_args=partial(solve,k=k,root=root,label1=label1,label2=label2,entry1=entry1,diff=diff);
	button1=Button(root,text="That's My Guess",command=solve_with_args,font=(None,22),height=3);
	button1.grid(row=5,column=400);
	root.mainloop()
