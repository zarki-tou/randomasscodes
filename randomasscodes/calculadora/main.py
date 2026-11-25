import pyautogui as p
from tkinter import *
window =Tk() # gives a ideia of a window
wh=420
wl=420
window.geometry("420x420")
window.title("67")
window.config(background="gray")
button=Button(window,text="PLS CLICK ME MOMMY")
button.pack()
def submit():
    username=entry.get()
    print(username)
    name.config(text=username)
def delete():
    entry.delete(0,END) #delete the line of text
def back():
    entry.delete(len(entry.get())-1,END) #delete last character
def display():
    if(x.get()==1):
        print("u gay")
    else:
        print("u r even more gay")
submit=Button(window,text="submit",command=submit)
submit.pack(side=RIGHT)
delete=Button(window,text="delete",command=delete)
delete.pack(side=RIGHT)
back=Button(window,text="backspace",command=back)
back.pack(side=RIGHT)
count=1
def click():
    global count
    count+=1
    label.config(text=count)
    label2.pack()
    label2.config(font=("Arial",count,"bold"))
button.config(command=click) #call a def
button.config(font=("Papyrus",50,"bold"))
button.config(bg="purple",fg="pink")
button.config(activebackground="pink",activeforeground="purple")
label=Label(window,text=count,font=("Arial",20,"bold"),fg="white",bg="gray",relief=SUNKEN,bd=10)
label.place(x=210,y=210)
label2=Label(window,text="AI MEU CUUUU")
entry=Entry()
entry.pack(side="bottom")
entry.insert(0,"hiii")
entry.config(width=10)
#entry.config(show="🙂")
name=Label(window,text=entry,width=10)
name.pack(side="bottom")
x=IntVar()
check=Checkbutton(window,text="i like dick",variable=x,onvalue=1,offvalue=0,command=display,font=("Arial",15,"bold"))
check.pack()
window.mainloop() # creates main window lister for events