from tkinter import *
from tkinter import ttk
from add_to_db import add_to_employee_roles

#Create main instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x270")

def popup_add_to_employee_roles():
    top= Toplevel(win)
    top.geometry("750x250")
    top.title("Child Window")
   
    lbl=Label(top, text="Enter Details", fg='red', font=("Helvetica", 16))
    lbl.place(x=80, y=50)
    txtfld=Entry(top, bd=5)
    txtfld.place(x=80, y=150)
    btn=Button(top, text="Submit", fg='blue', command=lambda: add_to_employee_roles(txtfld.get()))
    btn.place(x=80, y=100) 

Label(win, text=" Click the Below Button to Open the Popup Window", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Open", command= popup_add_to_employee_roles).pack()
win.mainloop()