from tkinter import *
from tkinter import ttk
from add_to_db import *
import customtkinter as ctk

# Set deafault customtkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class popup_add_to_employee_roles(ctk.CTkToplevel):
    """ add a role to employee_role database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x250")
        self.title("Employee Roles")
        
        ctk.CTkLabel(self, text="Employee Roles", font=("Roboto", 24)).pack(padx=12, pady=10)
     
        txtRoleDescription = ctk.CTkEntry(self, placeholder_text="Role Description")
        txtRoleDescription.pack(pady=12, padx=10)
        
        print(txtRoleDescription)
        ctk.CTkButton(self, text="Submit", command=lambda: add_to_employee_roles(txtRoleDescription.get())).pack(pady=12, padx=10)

 
class popup_add_to_employee_account(ctk.CTkToplevel):
    """ Popup window to add a new employee to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Employee Account")
     
        # Decorate here
        ctk.CTkLabel(self, text="Enter first name", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtName = ctk.CTkEntry(self, placeholder_text="Name")
        txtName.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter surname", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtSurname = ctk.CTkEntry(self, placeholder_text="surname")
        txtSurname.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter date of birth (YYYY-MM-DD)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtBirth = ctk.CTkEntry(self, placeholder_text="DOB")
        txtBirth.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter role ID", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtRoleId = ctk.CTkEntry(self, placeholder_text="Role ID")
        txtRoleId.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter Gender (M/F)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtGender = ctk.CTkEntry(self, placeholder_text="Gender")
        txtGender.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter Age", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtAge = ctk.CTkEntry(self, placeholder_text="Age")
        txtAge.pack(pady=12, padx=10)
        
        # Submit Button
        ctk.CTkButton(self, text="Submit", command=lambda: add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)



class popup_add_to_user_login_data(ctk.CTkToplevel):
    """ Popup window to add a new employee to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("User Login Data")
     
        # Decorate here
        ctk.CTkLabel(self, text="Enter employeeId", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtemployeeId = ctk.CTkEntry(self, placeholder_text="employeeId")
        txtemployeeId.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="Enter username", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtUsername = ctk.CTkEntry(self, placeholder_text="username")
        txtUsername.pack(pady=12, padx=10)
        
        ctk.CTkLabel(self, text="password", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtpassword = ctk.CTkEntry(self, placeholder_text="password")
        txtpassword.pack(pady=12, padx=10)
        
        # Submit Button
        ctk.CTkButton(self, text="Submit", command=lambda: add_to_user_login_data(txtemployeeId.get(), txtUsername.get(), txtpassword.get())).pack(pady=12, padx=10)

# TODO: Update password class

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        
        # Create main instance of customtkinter frame
        win = ctk.CTk()
        win.title('Popup Page')
        win.geometry("750x750")

        # Buttons on main screen 
        # Add to employee Roles
        Label = ctk.CTkLabel(self, text="Add to Employee Roles:", font=('Roboto', 24)).pack(pady=20)
        button = ctk.CTkButton(self, text= "Roles", command= self.open_add_to_employee_roles).pack()

        # Add to employee account
        Label = ctk.CTkLabel(self, text="Add to Employee Account", font=('Roboto', 24)).pack(pady=20)
        button = ctk.CTkButton(self, text= "Account", command= self.open_add_to_employee_account).pack()


        # Add to user login data
        Label = ctk.CTkLabel(self, text="Add to User Login Data", font=('Roboto', 24)).pack(pady=20)
        button = ctk.CTkButton(self, text= "User Login Data", command= self.open_add_to_user_login_data).pack()
        
        self.toplevel_window = None
    
    # TODO: Fix not focusing on new window
    def open_add_to_employee_roles(self):
        # TODO: Fix focusing on main app instead of popup window
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_employee_roles(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
            
            
    def open_add_to_employee_account(self):
        # TODO: Fix focusing on main app instead of popup window
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_employee_account(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
     
            
    def open_add_to_user_login_data(self):
        # TODO: Fix focusing on main app instead of popup window
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_user_login_data(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


# Main Function
if __name__ == "__main__":
    app = App()
    app.mainloop()