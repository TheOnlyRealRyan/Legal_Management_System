import tkinter
from PIL import Image
from PIL import ImageTk
import customtkinter
from add_to_db import *
from validatePassword import *

# TODO: validate Login into main page

# Initialise Appearance for customtkinter
DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")


class Login(customtkinter.CTk):
    """Login Page"""
    def __init__(self):
        super().__init__()       
        self.title("Login Page")
        self.geometry("500x350")
        
        # root page
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)

        self.main_container.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(self.main_container, text="Login Page", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        username = customtkinter.CTkEntry(self.main_container, placeholder_text="Username")
        username.pack(pady=12, padx=10)

        password = customtkinter.CTkEntry(self.main_container, placeholder_text="Password", show="*")
        password.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(self.main_container, text="Login", command=lambda: validate(username.get(), password.get())) # Do login command/function here
        button.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(self.main_container, text="Remember me") 
        
        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()       
        self.title("Main Program")
      
        # Dimensions relating to screen size (Overlaps with taskbar)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()-75))

        # root page
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
        
        self.left_side_panel.grid_columnconfigure(0, weight=0)
        # Left Frame - Placed higher up
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        # Left Frame - Placed lower down
        self.left_side_panel.grid_rowconfigure((6, 7), weight=1)
        
        
        # self.left_side_panel WIDGET
        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="Options: \n", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Load Images from resources/icons
        try:
            # TODO: Convert this to CTkImage
            img= (Image.open("resources/icons/dashboard.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_dashboard= ImageTk.PhotoImage(resized_image)   
            
            img= (Image.open("resources/icons/archive.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_archive= ImageTk.PhotoImage(resized_image)  
            
            img= (Image.open("resources/icons/case.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_case= ImageTk.PhotoImage(resized_image)  
            
            img= (Image.open("resources/icons/files.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_files= ImageTk.PhotoImage(resized_image)  
            
            img= (Image.open("resources/icons/customer.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_customer= ImageTk.PhotoImage(resized_image)  
            
            img= (Image.open("resources/icons/admin.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_admin= ImageTk.PhotoImage(resized_image)  
            
            img= (Image.open("resources/icons/user.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_user= ImageTk.PhotoImage(resized_image)              
        except IOError:
            print("File not found") 
            pass
        
        
        # button to select correct frame IN self.left_side_panel WIDGET       
        self.bt_dashboard = customtkinter.CTkButton(self.left_side_panel, image=btnImg_dashboard, text="", command=self.dashboard)
        self.bt_dashboard.grid(row=1, column=0, padx=20, pady=10)

        self.bt_archive = customtkinter.CTkButton(self.left_side_panel, image=btnImg_archive, text="", command=self.archive)
        self.bt_archive.grid(row=2, column=0, padx=20, pady=10)
        
        self.bt_case = customtkinter.CTkButton(self.left_side_panel, image=btnImg_case, text="", command=self.case)
        self.bt_case.grid(row=3, column=0, padx=20, pady=10)
        
        self.bt_files = customtkinter.CTkButton(self.left_side_panel, image=btnImg_files, text="", command=self.files)
        self.bt_files.grid(row=4, column=0, padx=20, pady=10)
        
        self.bt_customer = customtkinter.CTkButton(self.left_side_panel, image=btnImg_customer, text="", command=self.customer)
        self.bt_customer.grid(row=5, column=0, padx=20, pady=10)
        
        self.bt_admin = customtkinter.CTkButton(self.left_side_panel, image=btnImg_admin, text="", command=self.admin)
        self.bt_admin.grid(row=6, column=0, padx=20, pady=10)
        
        self.bt_user = customtkinter.CTkButton(self.left_side_panel, image=btnImg_user, text="", command=self.user)
        self.bt_user.grid(row=7, column=0, padx=20, pady=10)
        

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
                
        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        
        self.toplevel_window = None
        
    # Functions for navigating to and decorating different frames   
    def dashboard(self):
        """ self.right_dashboard   ----> dashboard widget """
        self.clear_frame()
        # Decorate Right Frame
        
    def archive(self):
        """ self.right_dashboard   ----> archive widget """
        self.clear_frame()
        # Decorate Right Frame
        
    def case(self):
        """ self.right_dashboard   ----> case widget """
        self.clear_frame()
        # Decorate Right Frame
        
    def files(self):
        """ self.right_dashboard   ----> files widget """
        self.clear_frame()
        # Decorate Right Frame
        
    def customer(self):
        """ self.right_dashboard   ----> dashbcustomeroard widget """
        self.clear_frame()
        # Decorate Right Frame
    
    
    def admin(self):
        """ self.right_dashboard   ----> Admin widget """
        self.clear_frame()
        
        # Decorate Right Frame
        # Add to employee Roles
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Employee Roles:", font=('Roboto', 24))
        Label.grid(row=0, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Roles", command= self.open_add_to_employee_roles)
        button.grid(row=1, column=0, padx=20, pady=(10, 0))

        # Add to employee account
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Employee Account", font=('Roboto', 24))
        Label.grid(row=2, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Account", command= self.open_add_to_employee_account)
        button.grid(row=3, column=0, padx=20, pady=(10, 0))

        # Add to user login data
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to User Login Data", font=('Roboto', 24))
        Label.grid(row=6, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "User Login Data", command= self.open_add_to_user_login_data)
        button.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        # Add to client info
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=4, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=5, column=0, padx=20, pady=(10, 0))
        
    def user(self):
        """ self.right_dashboard   ----> dashboard widget """
        self.clear_frame()
        # Decorate Right Frame
        
                             
    def clear_frame(self):
        """ Clears frame from self.right_dashboard(frame) before loading the widget of the concerned page """
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()
     
            
    def open_add_to_employee_roles(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_employee_roles(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            print("actually here")
        else:
            print("here")
            self.toplevel_window.focus()  # if window exists focus it
            
            
    def open_add_to_employee_account(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_employee_account(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it
        
            
    def open_add_to_user_login_data(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup_add_to_user_login_data(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it


    def open_add_to_client_information(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup_add_to_client_information(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
                print("actually here")
            else:
                print("here")
                self.toplevel_window.focus()  # if window exists focus it

class popup_add_to_employee_roles(customtkinter.CTkToplevel):
    """ add a role to employee_role database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x250")
        self.title("Employee Roles")
        
        customtkinter.CTkLabel(self, text="Employee Roles", font=("Roboto", 24)).pack(padx=12, pady=10)
     
        txtRoleDescription = customtkinter.CTkEntry(self, placeholder_text="Role Description")
        txtRoleDescription.pack(pady=12, padx=10)
        
        customtkinter.CTkButton(self, text="Submit", command=lambda: add_to_employee_roles(txtRoleDescription.get())).pack(pady=12, padx=10)

 
class popup_add_to_employee_account(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Employee Account")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter first name", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtName = customtkinter.CTkEntry(self, placeholder_text="Name")
        txtName.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter surname", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtSurname = customtkinter.CTkEntry(self, placeholder_text="surname")
        txtSurname.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter date of birth (YYYY-MM-DD)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtBirth = customtkinter.CTkEntry(self, placeholder_text="DOB")
        txtBirth.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter role ID", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtRoleId = customtkinter.CTkEntry(self, placeholder_text="Role ID")
        txtRoleId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Gender (M/F)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtGender = customtkinter.CTkEntry(self, placeholder_text="Gender")
        txtGender.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Age", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtAge = customtkinter.CTkEntry(self, placeholder_text="Age")
        txtAge.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_user_login_data(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("User Login Data")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter employeeId", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtemployeeId = customtkinter.CTkEntry(self, placeholder_text="employeeId")
        txtemployeeId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter username", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtUsername = customtkinter.CTkEntry(self, placeholder_text="username")
        txtUsername.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="password", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtpassword = customtkinter.CTkEntry(self, placeholder_text="password")
        txtpassword.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: add_to_user_login_data(txtemployeeId.get(), txtUsername.get(), txtpassword.get())).pack(pady=12, padx=10)
      
      
class popup_add_to_client_information(customtkinter.CTkToplevel):
    """ Popup window to add a new client to client_information database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Client Information Input")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Client First Name", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtName = customtkinter.CTkEntry(self, placeholder_text="First Name")
        txtName.pack(pady=12, padx=10)
        
        
        customtkinter.CTkLabel(self, text="Client Last Name", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtSurname = customtkinter.CTkEntry(self, placeholder_text="Last Name")
        txtSurname.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Client Gender", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtGender = customtkinter.CTkEntry(self, placeholder_text="Gender")
        txtGender.pack(pady=12, padx=10)

        
        customtkinter.CTkLabel(self, text="Date Of Birth (YYYY-MM-DD)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtDOB = customtkinter.CTkEntry(self, placeholder_text="DOB")
        txtDOB.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: add_to_client_information(txtName.get(), txtSurname.get(), txtGender.get(), txtDOB.get())).pack(pady=12, padx=10)
        
        
# Main Function
if __name__ == "__main__":
    
    # login = Login()
    # login.mainloop()
    app = App()
    app.mainloop()  
    
    
    
    
    
    