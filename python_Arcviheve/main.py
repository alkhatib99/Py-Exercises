from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.ttk import * 
from time import strftime
from typing import Collection, Sized
from tkinter.filedialog import askopenfilename


    
    
root = Tk()
def open():
    Tk().withdraw()
    filename = askopenfilename()# show an "Open" dialog box and return the path to the selected file
    root.title(filename)
def write():
    fullname=str(fname_var.get())+" "+str(lname_var.get())
    department=str(DrbChoose.get())
    gender=str(GrbChoose.get())
    msg="Your full name is "+fullname+"\nYour study is "+department+"\nYou are "+gender+"\nYour hobbies are:\n"+hobby;
    with open('readme.txt','w') as f :
        f.writelines(msg)
    
    
    
def popupmsg():
    fullname=str(fname_var.get())+" "+str(lname_var.get())
    department=str(DrbChoose.get())
    gender=str(GrbChoose.get())
    msg="Your full name is "+fullname+"\nYour study is "+department+"\nYou are "+gender+"\nYour hobbies are:\n"+hobby;
    popup = Toplevel(root)
    popup.geometry("750x270")
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=("normal"))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
#Sizing the window 
root.geometry("550x400")

# Creating Menubar
menubar = Menu(root)
    
    
    # Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = open)
file.add_separator()

file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)

root.config(menu = menubar, width=550, height=400, )




fname_var=StringVar()
lname_var=StringVar()

l1=ttk.Label(root,font=('calibre',10, 'bold'),text="First Name",foreground="#FF0000").grid(row=0,column=0,pady=10,padx=20)
l2=ttk.Label(root,font=('calibre',10, 'bold'),text="Last Name",foreground="#FF0000").grid(row=1,column=0,pady=10,padx=20)
l3=ttk.Label(root,font=('calibre',10, 'bold'),text="Department",foreground="#FF0000").grid(row=2,column=0,pady=10,padx=20)
l4=ttk.Label(root,font=('calibre',10, 'bold'),text="Gender",foreground="#FF0000",).grid(row=3,column=0,pady=10,padx=20)
l5=ttk.Label(root,font=('calibre',10, 'bold'),text="Hobbies",foreground="#FF0000",).grid(row=4,column=0,pady=10,padx=20)


fnText=tkinter.Entry(root,width=30,textvariable=fname_var,font=('calibre',10, 'normal')).grid(row=0,column=1)
lnText=tkinter.Entry(root,width=30,textvariable=lname_var,font=('calibre',10, 'normal')).grid(row=1,column=1)
fname=str(fname_var.get())
lname=str(lname_var.get())
DrbChoose=StringVar()

DR1=tkinter.Radiobutton(root,text="Computer science",value="Computer science",variable=DrbChoose)
DR2=tkinter.Radiobutton(root,text="Software Engeneering",value="Software Engeneering",variable=DrbChoose)
study=""

DR1.grid(row=2, column=1,sticky="W")
DR2.grid(row=2,column=2,sticky="W")


GrbChoose=StringVar()

GR1=tkinter.Radiobutton(root,text="Male",value="Male",variable=GrbChoose)
GR2=tkinter.Radiobutton(root,text="Female",value="Female",variable=GrbChoose)
#gender=GrbChoose.get()

GR1.grid(sticky="W",row=3,column=1)
GR2.grid(sticky="W",row=3,column=2)

hobby_Reading=IntVar()
hobby_Drawing=IntVar()
hobby_Programming=IntVar()
hobby_Painting=IntVar()

ch1=ttk.Checkbutton(root,text="Reading",variable=hobby_Reading)
ch2=ttk.Checkbutton(root,text="Drawing",variable=hobby_Drawing)
ch3=ttk.Checkbutton(root,text="Programming",variable=hobby_Programming)
ch4=ttk.Checkbutton(root,text="Painting",variable=hobby_Painting)

ch1.grid(sticky="W",row=4, column=1)
ch2.grid(sticky="W",row=4,column=2)
ch3.grid(sticky="W",row=5, column=1)
ch4.grid(sticky="W",row=5,column=2)
#gender=""

hobby=""

if(hobby_Reading):
    hobby+="Reading\n"
if(hobby_Drawing):
    hobby+="Drawing\n"
if(hobby_Programming):
    hobby+="Programming\n"
if(hobby_Painting):
    hobby+="Painting\n"


#if(DrbChoose ==1):
    study="Computer Science"
#elif(DrbChoose == 2):
#    study="Software Engineering"

#g=""
#if(gender == 0):
#    g=str("Male")
#elif(gender == 1):
#    g=str("Female")
 
#msg=str(g)    
#msg="Your Fulll Name is "+str(fname)+" "+str(lname)+"\n"+"You study "+study+"\n"+"you are "+str(gender)+"\n Your hobbies are:\n"+str(hobby)



sbutton=tkinter.Button(root,text="show information",background="yellow",width=20,height=10,command=popupmsg ).grid(row=7,padx=10,column=0)

wbutton=tkinter.Button(root,text="Write information",background="yellow",height=10,width=20, command=write).grid(row=7,sticky="W",column=1)

root.mainloop()
   
    