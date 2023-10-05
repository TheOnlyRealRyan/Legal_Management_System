from tkinter import *
from tkinter import ttk
from add_to_db import *

# Create main instance of Tkinter frame
win = Tk()
win.geometry("750x750")


def popup_add_to_employee_roles():
    """ Popup window to add a role to employee_role database"""
    # Create a popup window here
    top= Toplevel(win)
    top.geometry("750x250")
    top.title("Employee Roles")
    
    # Decorate popup here 
    lbl=Label(top, text="Enter Details", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=50)
    txtfld=Entry(top, bd=5)
    txtfld.place(x=80, y=150)
    btn=Button(top, text="Submit", fg='blue', command=lambda: add_to_employee_roles(txtfld.get())) # Pass in a value like this!
    btn.place(x=80, y=100) 
    
    
def popup_add_to_employee_account():
    """ Popup window to add a new employee to employee_account database"""
    # Create a popup window here
    top= Toplevel(win)
    top.geometry("750x750")
    top.title("Employee Account")
    
    # Decorate popup here 
    lbl=Label(top, text="Enter first name", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=50)
    txtName=Entry(top, bd=5)
    txtName.place(x=80, y=75)
    
    lbl=Label(top, text="Enter surname", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=125)
    txtSurname=Entry(top, bd=5)
    txtSurname.place(x=80, y=150)
    
    lbl=Label(top, text="Enter date of birth (YYYY-MM-DD)", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=200)
    txtBirth=Entry(top, bd=5)
    txtBirth.place(x=80, y=225)
    
    lbl=Label(top, text="Enter role ID", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=275)
    txtRoleId=Entry(top, bd=5)
    txtRoleId.place(x=80, y=300)
    
    lbl=Label(top, text="Enter Gender (M/F)", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=350)
    txtGender=Entry(top, bd=5)
    txtGender.place(x=80, y=375)
    
    lbl=Label(top, text="Enter Age", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=425)
    txtAge=Entry(top, bd=5)
    txtAge.place(x=80, y=475)
    
    btn=Button(top, text="Submit", fg='blue', command=lambda: add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get()))
    btn.place(x=80, y=525)
    # TODO: Close window after submit

def popup_add_to_user_login_data():
    """ Popup window to add a new employee to employee_account database"""
    # Create a popup window here
    top= Toplevel(win)
    top.geometry("750x750")
    top.title("User Login Data")
    
    # Decorate popup here 
    lbl=Label(top, text="Enter employeeId", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=50)
    txtemployeeId=Entry(top, bd=5)
    txtemployeeId.place(x=80, y=75)
    
    lbl=Label(top, text="Enter username", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=125)
    txtUsername=Entry(top, bd=5)
    txtUsername.place(x=80, y=150)
    
    lbl=Label(top, text="Enter password", fg='blue', font=("Helvetica", 16))
    lbl.place(x=80, y=200)
    txtpassword=Entry(top, bd=5)
    txtpassword.place(x=80, y=225)
    
    btn=Button(top, text="Submit", fg='blue', command=lambda: add_to_user_login_data(txtemployeeId.get(), txtUsername.get(), txtpassword.get()))
    btn.place(x=80, y=275)

# Buttons on main screen  
# Add to employee Roles
Label(win, text="Add to Employee Roles:", font=('Helvetica 14 bold')).pack(pady=20)
ttk.Button(win, text= "Roles", command= popup_add_to_employee_roles).pack()

# Add to employee account
Label(win, text="Add to Employee Account", font=('Helvetica 14 bold')).pack(pady=40)
ttk.Button(win, text= "Account", command= popup_add_to_employee_account).pack()

# Add to user login data
Label(win, text="Add to User Login Data", font=('Helvetica 14 bold')).pack(pady=40)
ttk.Button(win, text= "User Login Data", command= popup_add_to_user_login_data).pack()

win.mainloop()