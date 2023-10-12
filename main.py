import tkinter
from PIL import Image
import customtkinter
from add_to_db import *
from validatePassword import *
import grab_from_db as db_conn
import tksheet
import popup

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
        self.main_container = customtkinter.CTkCanvas(self, bg="#00253e")

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
        self.main_container = customtkinter.CTkCanvas(self, bg="#00253e")
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkCanvas(self.main_container, width=125, bg="#00406c")
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
       
        # Configure the weights of rows in left_side_panel
        self.left_side_panel.grid_rowconfigure((0,1,2,3,4,5), weight=0)
        self.left_side_panel.grid_rowconfigure((6), weight=3)
        self.left_side_panel.grid_rowconfigure((7,8), weight=0)
        
        # right_side_panel has right_dashboard inside
        self.right_side_panel = customtkinter.CTkCanvas(self.main_container, bg="#003356")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
                
        self.right_dashboard = customtkinter.CTkCanvas(self.main_container, bg="#003356")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        
        # Configure the weights of rows in right_dashboard
        self.right_dashboard.grid_rowconfigure((0,1,2,3), weight=0)
        self.right_dashboard.grid_rowconfigure((4), weight=1)   
        self.right_dashboard.grid_rowconfigure((5), weight=0)
        # self.right_dashboard.grid_columnconfigure((0,1,2,3), weight=0)   
        
        # left_side_panel Menu
        self.menu_label = customtkinter.CTkLabel(self.left_side_panel, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.menu_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Load Images from resources/icons
        try:
            img= (Image.open("resources/icons/dashboard.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_dashboard= customtkinter.CTkImage(resized_image)   
            
            img= (Image.open("resources/icons/archive.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_archive= customtkinter.CTkImage(resized_image)  
            
            img= (Image.open("resources/icons/case.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_case= customtkinter.CTkImage(resized_image)  
            
            img= (Image.open("resources/icons/files.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_files= customtkinter.CTkImage(resized_image)  
            
            img= (Image.open("resources/icons/customer.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_client= customtkinter.CTkImage(resized_image)  
            
            img= (Image.open("resources/icons/admin.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_admin= customtkinter.CTkImage(resized_image)  
            
            img= (Image.open("resources/icons/user.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            btnImg_user= customtkinter.CTkImage(resized_image)     
        except IOError:
            print("File not found") 
            pass
        
        
        # buttons on left_side_panel to select canvas     
        self.bt_dashboard = customtkinter.CTkButton(self.left_side_panel, image=btnImg_dashboard, fg_color="transparent", width=45, text="", command=self.dashboard)
        self.bt_dashboard.grid(row=1, column=0, padx=20, pady=10)

        self.bt_archive = customtkinter.CTkButton(self.left_side_panel, image=btnImg_archive, fg_color="transparent", width=45, text="", command=self.archive)
        self.bt_archive.grid(row=2, column=0, padx=20, pady=10)
        
        self.bt_case = customtkinter.CTkButton(self.left_side_panel, image=btnImg_case, fg_color="transparent", width=45, text="", command=self.case)
        self.bt_case.grid(row=3, column=0, padx=20, pady=10)
        
        self.bt_files = customtkinter.CTkButton(self.left_side_panel, image=btnImg_files, fg_color="transparent", width=45, text="", command=self.files)
        self.bt_files.grid(row=4, column=0, padx=20, pady=10)
        
        self.bt_client = customtkinter.CTkButton(self.left_side_panel, image=btnImg_client, fg_color="transparent", width=45, text="", command=self.client)
        self.bt_client.grid(row=5, column=0, padx=20, pady=10)
        
        # TODO: If statement here to see if admin
        self.bt_admin = customtkinter.CTkButton(self.left_side_panel, image=btnImg_admin, fg_color="transparent", width=45, text="", command=self.admin)
        self.bt_admin.grid(row=7, column=0, padx=20, pady=10)
        
        self.bt_user = customtkinter.CTkButton(self.left_side_panel, image=btnImg_user, fg_color="transparent", width=45, text="", command=self.user)
        self.bt_user.grid(row=8, column=0, padx=20, pady=10)
        
        

        self.toplevel_window = None
    
    
    # --------------------------------------------------------------------------------------------------
    # Functions for navigating to and decorating different frames 
    # --------------------------------------------------------------------------------------------------  
    def dashboard(self):
        self.clear_canvas()
        # Decorate Right Frame
     
        
    def archive(self):
        self.clear_canvas()
        # Load image
        try:
            img= (Image.open("resources/icons/add.png"))
            resized_image= img.resize((30, 30), Image.LANCZOS)
            btnImg_add= customtkinter.CTkImage(resized_image)        
        except IOError:
            print("File not found") 
            pass
        
        # Decorate Right Frame
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Archive", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        Label = customtkinter.CTkLabel(self.right_dashboard, text="New Archive", font=('Roboto', 24))
        Label.grid(row=0, column=38, padx=0, pady=10 )
        button = customtkinter.CTkButton(self.right_dashboard, text= "", image=btnImg_add, fg_color="transparent", width=50, height=50, command= self.open_add_to_archived_state)
        button.grid(row=0, column=39, padx=0, pady=0)
        
        # grab data 
        data = db_conn.all_client_information()
        headers = ['id', 'Name', 'Surname', 'Gender', 'Date of Birth']
        
        # Create table
        self.sheet = tksheet.Sheet(self.right_dashboard, height = 800, width = 1750)
        self.sheet.grid(row=4, column =0, padx = 20, pady = 20, columnspan = 40)

        
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        self.sheet.set_sheet_data([[f"{a}", f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in data ])
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
    
        
    def case(self):
        self.clear_canvas()
        # Decorate Right Frame
    
        
    def files(self):
        self.clear_canvas()
        # Load image
        try:
            img= (Image.open("resources/icons/add.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_add= customtkinter.CTkImage(resized_image)        
        except IOError:
            print("File not found") 
            pass
        
        # Decorate Right Frame      
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Upload File", font=('Roboto', 24))
        Label.grid(row=0, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "", image=btnImg_add, fg_color="transparent", width=45, command= self.open_add_to_file_upload_data)
        button.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        # grab data 
        data = db_conn.all_file_upload_data()
        headers = ['fileId', 'fileName', 'caseId', 'recievedDate', 'dateUploaded']
        
        # Create table
        self.sheet = tksheet.Sheet(self.right_dashboard, height = 500, width = 1000)
        self.sheet.grid(row=3, column =0)
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        self.sheet.set_sheet_data([[f"{a}", f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in data ])
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))


    def client(self):
        self.clear_canvas()
        # Load image
        try:
            img= (Image.open("resources/icons/add.png"))
            resized_image= img.resize((25,25), Image.LANCZOS)
            btnImg_add= customtkinter.CTkImage(resized_image)        
        except IOError:
            print("File not found") 
            pass
        
        # Decorate Right Frame
        Label = customtkinter.CTkLabel(self.right_dashboard, text="New Client", font=('Roboto', 24))
        Label.grid(row=0, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "", image=btnImg_add, fg_color="transparent", width=45, command= self.open_add_to_client_information)
        button.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        # grab data 
        data = db_conn.all_client_information()
        headers = ['id', 'Name', 'Surname', 'Gender', 'Date of Birth']
        
        # Create table
        self.sheet = tksheet.Sheet(self.right_dashboard, height = 500, width = 1000)
        self.sheet.grid(row=3, column =0)
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        self.sheet.set_sheet_data([[f"{a}", f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in data ])
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))

    
    def admin(self):
        self.clear_canvas()
        
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
        Label.grid(row=4, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "User Login Data", command= self.open_add_to_user_login_data)
        button.grid(row=5, column=0, padx=20, pady=(10, 0))
        
        # Add to client info
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=6, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        # Add to case_data
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=8, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=9, column=0, padx=20, pady=(10, 0))
        
        # Add to archived_state
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=10, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=11, column=0, padx=20, pady=(10, 0))
        
        # Add to case_location
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=12, column=0, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=13, column=0, padx=20, pady=(10, 0))
        
        # Add to destruction_state
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=0, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=1, column=1, padx=20, pady=(10, 0))
        
        # Add to file_upload_data
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=2, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=3, column=1, padx=20, pady=(10, 0))
        
        # Add to deletion_confirmation
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=4, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=5, column=1, padx=20, pady=(10, 0))
        
        # Add to deletion_logging
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=6, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=7, column=1, padx=20, pady=(10, 0))
        
        # Add to arcived_case_request
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=8, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=9, column=1, padx=20, pady=(10, 0))
        
        # Add to case_drawn_by
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=10, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=11, column=1, padx=20, pady=(10, 0))
        
        # Add to case_drawn_history
        Label = customtkinter.CTkLabel(self.right_dashboard, text="Add to Client Information", font=('Roboto', 24))
        Label.grid(row=12, column=1, padx=20, pady=(10, 0))
        button = customtkinter.CTkButton(self.right_dashboard, text= "Client Information", command= self.open_add_to_client_information)
        button.grid(row=13, column=1, padx=20, pady=(10, 0))
        

    def user(self):
        self.clear_canvas()
        # Decorate Right Frame
        
                             
    def clear_canvas(self):
        """ Clears canvas from right_dashboard before loading the new canvas """
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()
    
    
    # -------------------------------------------- 
    # Popup windows focus functions
    # --------------------------------------------        
    def open_add_to_employee_roles(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_employee_roles(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it
            
            
    def open_add_to_employee_account(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_employee_account(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it
        
            
    def open_add_to_user_login_data(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_user_login_data(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it


    def open_add_to_client_information(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_client_information(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
    def open_add_to_case_data(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_case_data(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
    
    
    def open_add_to_archived_state(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_archived_state(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
                
    def open_add_to_destruction_state(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_destruction_state(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
                
    def open_add_to_file_upload_data(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_file_upload_data(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
                
    def open_add_to_deletion_confirmation(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_deletion_confirmation(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
    
    def open_add_to_arcived_case_request(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_archived_case_request(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
                
    def open_add_to_case_drawn_by(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = popup.popup_add_to_case_drawn_by(self)  # create window if its None or destroyed
                self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
            else:
                self.toplevel_window.focus()  # if window exists focus it
                
    
    def open_add_to_case_drawn_history(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_case_drawn_history(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it


        
# Main Function
if __name__ == "__main__":
    
    # login = Login()
    # login.mainloop()
    app = App()
    app.mainloop()  