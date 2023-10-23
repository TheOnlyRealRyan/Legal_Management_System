import customtkinter
from PIL import Image
import tkinter
import tksheet
import time 

from add_to_db import *
import grab_from_db as db_conn
from validatePassword import *
import popup
import global_variables


# TODO: validate Login into main page
# TODO: change title headings from database titles to normal titles


# Initialise Appearance for customtkinter
DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  
        
        # open login page
        self.login()
        
          
    def update(self):
        """1 second update function """ 
        self.after(1000, self.update)
    
                 
    def load_image(self, img_picked):
        """Load an image only if its called"""
        try:
            resource_path = "resources/icons_variation_2/"                
            img= (Image.open(f"{resource_path}{img_picked}.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            return customtkinter.CTkImage(resized_image)             
        except IOError:
            print("File not found") 
            pass
    
    # --------------------------------------------------------------------------------------------------
    # Different Pages that can be loaded
    # --------------------------------------------------------------------------------------------------  
    def load_main_page(self):    
        self.title("Main Program")
        # Dimensions relating to screen size
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()-75))
        
        
        
        # root page
        self.main_container = customtkinter.CTkCanvas(self, bg="#00253e")
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkCanvas(self.main_container, width=125, bg="#00406c")
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
       
        # Configure the weights of rows in left_side_panel
        # self.left_side_panel.grid_rowconfigure((0,1,2,3,4,5,6), weight=0)
        self.left_side_panel.grid_rowconfigure((7,8), weight=3)
        # self.left_side_panel.grid_rowconfigure((9), weight=0)
        
        # right_dashboard creation
        self.right_dashboard = customtkinter.CTkCanvas(self.main_container, bg="#003356")
        self.right_dashboard.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        
        # left_side_panel Menu
        self.menu_label = customtkinter.CTkLabel(self.left_side_panel, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.menu_label.grid(row=0, column=0, padx=20, pady=(20, 10))      
              
        # buttons on left_side_panel to select canvas     
        self.btn_dashboard = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("dashboard"), fg_color="transparent", width=45, text="", command=lambda: self.dashboard())
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10)
        
        self.btn_notification = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("notification"), fg_color="transparent", width=45, text="", command=lambda: self.notification())
        self.btn_notification.grid(row=2, column=0, padx=20, pady=10)

        self.btn_archive = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("archive"), fg_color="transparent", width=45, text="", command=self.archive)
        self.btn_archive.grid(row=3, column=0, padx=20, pady=10)
            
        self.btn_case = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("case"), fg_color="transparent", width=45, text="", command=self.case)
        self.btn_case.grid(row=4, column=0, padx=20, pady=10)
        
        if global_variables.get_id() != 2: # If not archivist
            self.btn_files = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("files"), fg_color="transparent", width=45, text="", command=self.files)
            self.btn_files.grid(row=5, column=0, padx=20, pady=10)
        
        self.btn_client = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("customer"), fg_color="transparent", width=45, text="", command=self.client)
        self.btn_client.grid(row=6, column=0, padx=20, pady=10)
             
        if global_variables.get_id() == 1: # If admin        
            self.btn_admin = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("admin"), fg_color="transparent", width=45, text="", command=self.admin)
            self.btn_admin.grid(row=9, column=0, padx=20, pady=10)
        
        # Focus on dashboard first
        self.dashboard()
        
        self.toplevel_window = None  
        
    def login(self):              
        # Layout        
        self.title("Login Page")
        self.geometry("500x350")
        
        # root page
        self.login_page = customtkinter.CTkCanvas(self, bg="#00253e")

        self.login_page.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(self.login_page, text="Login Page", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        self.username = customtkinter.CTkEntry(self.login_page, placeholder_text = "username")
        self.username.pack(pady=12, padx=10)

        self.password = customtkinter.CTkEntry(self.login_page, placeholder_text = "password", show="*")
        self.password.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(self.login_page, text="Login", command=lambda: self.login_success())
        button.pack(pady=12, padx=10)
    
    
    def login_success(self):       
        username = "admin" # self.username.get()
        password = "admin" # self.password.get()
        success = validate(username, password)
        if success:                          
            global_variables.set_role(db_conn.login_employee_roles(username))
            global_variables.set_id(db_conn.login_employee_id(username)) 
            
            print("Login Successful")
            for widget in self.login_page.winfo_children():
                widget.destroy()
            self.login_page.destroy()
            self.load_main_page()         


    def dashboard(self):
        self.clear_canvas()
        
        def refresh_data(): 
            # TODO: The table should update somehow
            return db_conn.all_archived_case_request()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=800, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate Heading Banner    
        Label = customtkinter.CTkLabel(self.heading_banner, text="Dashboard", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )    

        # Decorate inner panel
        # TODO: Analytics go here
        
        
    def notification(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.archival = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
        self.archival.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.deletion = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
        self.deletion.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.destruction = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
        self.destruction.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=400, bg="#00253e")
        # self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=False, padx=10, pady=10)
        
        # Decorate inner right panel
        
        
        
        # Decorate Heading Banner    
        Label = customtkinter.CTkLabel(self.heading_banner, text="Notifications", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )    

        # Decorate Deletion Notification Bar
        if global_variables.get_id() == 2 or global_variables.get_id() == 1:
            Label = customtkinter.CTkLabel(self.archival, text="Archival Retrieval Requests", font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, padx=10, pady=10) 
            
            headers = ['archiveNumber', 'employee', 'dateRequested', 'Location']
            self.data = [[f"{a}",f"{b} {c}",f"{d}",f"{e}"] for a,b,c,d,e in db_conn.all_archived_case_request()]
            
            # Create table
            self.sheet1 = tksheet.Sheet(self.archival, data = self.data, height = 800, theme = "dark", show_row_index=False, show_top_left=False)
            self.sheet1.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

            self.sheet1.headers((f"{x}" for x in headers))   
            
            # table enable choices listed below:
            self.sheet1.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy")) 
            
                   
        # Decorate Deletion Notification Bar
        if global_variables.get_id() == 2 or global_variables.get_id() == 1: # manager or admin role
            Label = customtkinter.CTkLabel(self.deletion, text="Deletion Requests", font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, padx=10, pady=10)
            
            headers = ['caseId', 'employee requested']
            self.data = [[f"{a}",f"{b} {c}"] for a,b,c in db_conn.all_deletion_confirmation()]
            
            self.sheet2 = tksheet.Sheet(self.deletion, data = self.data, height = 800, theme = "dark", show_row_index=False, show_top_left=False)
            self.sheet2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

            self.sheet2.headers((f"{x}" for x in headers))   
            
            # table enable choices listed below:
            self.sheet2.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy")) 
            
        # Decorate Deletion Notification Bar
        if global_variables.get_id() == 2 or global_variables.get_id() == 1 or global_variables.get_id() == 3: # manager or admin or archival role
            Label = customtkinter.CTkLabel(self.destruction, text="Destruction Dates", font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, padx=10, pady=10)
            
            headers = ['caseId', 'archived State', 'ArchiveNumber', 'archivedDate', 'dateToBeDestroyed']
            self.data = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in db_conn.case_to_be_destroyed_this_month()]
            
            self.sheet2 = tksheet.Sheet(self.destruction, data = self.data, height = 800, theme = "dark", show_row_index=False, show_top_left=False)
            self.sheet2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

            self.sheet2.headers((f"{x}" for x in headers))   
            
            # table enable choices listed below:
            self.sheet2.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))      
    def archive(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)     
        Label = customtkinter.CTkLabel(self.heading_banner, text="Archive", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="New Archive", font=('Roboto', 24))
        Label.grid(row=0, column=4, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_archived_state)
        button.grid(row=0, column=5, padx=5, pady=5)
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Request Archive", font=('Roboto', 24))
        Label.grid(row=0, column=6, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_archived_case_request)
        button.grid(row=0, column=7, padx=5, pady=5)
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Give Location", font=('Roboto', 24))
        Label.grid(row=0, column=8, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_case_location)
        button.grid(row=0, column=9, padx=5, pady=5)
        
        # Decorate Main Page
        # grab data 
        def refresh_data():
            return db_conn.all_archived_state()
            
        headers = ['case Id', 'State', 'Archive Number', 'Archived Date', 'Date To Be Destroyed', 'Location']
        self.data = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}",f"{g}"] for a,b,c,d,e,f,g in refresh_data()]
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel,data = self.data, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
     
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
    
        
    def case(self):
        self.clear_canvas()
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)     
        Label = customtkinter.CTkLabel(self.heading_banner, text="Cases", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="New Case", font=('Roboto', 24))
        Label.grid(row=0, column=4, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_case_data)
        button.grid(row=0, column=5, padx=5, pady=5)
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Delete Case Request", font=('Roboto', 24))
        Label.grid(row=0, column=6, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_deletion_confirmation)
        button.grid(row=0, column=7, padx=5, pady=5)
        
        # Decorate inner right panel
        # grab data 
        gathered_data = db_conn.all_case_data()
        headers = ['id', 'client', 'employee', 'Description', 'Department', 'Date of Open', 'Date of Upload']
        self.data = [[f"{a}",f"{b} {c}",f"{d} {e}",f"{f}",f"{g}",f"{h}",f"{i}"] for a,b,c,d,e,f,g,h,i in gathered_data ]
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel, data = self.data, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.sheet.headers((f"{x}" for x in headers))
               
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
    
        
    def files(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate Right Frame     
        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)     
        Label = customtkinter.CTkLabel(self.heading_banner, text="Cloud Upload", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Download File", font=('Roboto', 24))
        Label.grid(row=0, column=4, padx=10, pady=10 )
        # TODO: change this button to download from cloud
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_file_upload_data)
        button.grid(row=0, column=5, padx=5, pady=5) 
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Upload File", font=('Roboto', 24))
        Label.grid(row=0, column=6, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_file_upload_data)
        button.grid(row=0, column=7, padx=5, pady=5) 
        
        # grab data 
        gathered_data = db_conn.all_file_upload_data()
        headers = ['fileId', 'fileName', 'caseId', 'recievedDate', 'dateUploaded']
        self.data = [[f"{a}", f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in gathered_data ]
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel,data = self.data, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        # self.sheet.grid(row=0, column =0, padx = 10, pady = 10)
        
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))


    def client(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)    
         
        Label = customtkinter.CTkLabel(self.heading_banner, text="Client", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="New Client", font=('Roboto', 24))
        Label.grid(row=0, column=4, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= self.open_add_to_client_information)
        button.grid(row=0, column=5, padx=5, pady=5) 

        # Decorate inner right panel
        # grab data 
        gathered_data = db_conn.all_client_information()
        headers = ['id', 'Name', 'Surname', 'Gender', 'Date of Birth', 'Checked']
        self.data = [[f"{a}", f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data ]
        
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel,  
                                    data = self.data, 
                                    theme = "dark", 
                                    height = 800, 
                                    width = 1750,
                                    show_row_index=False, 
                                    show_top_left=False)

        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10,)

        # self.sheet.grid(row=0, column = 0, padx = 10, pady = 10)
        
        self.sheet.headers((f" {x}" for x in headers))
        
        # populate Table
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))

    
    def admin(self):
        self.clear_canvas()
              # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)    
         
        Label = customtkinter.CTkLabel(self.heading_banner, text="Admin Page", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )

        def optionmenu_insert(choice):
            if choice == "Employee Roles":
                return self.open_add_to_employee_roles()
            elif choice == "Employee Account":
                return self.open_add_to_employee_account()
            elif choice == "User Login Data":
                return self.open_add_to_user_login_data()
            elif choice == "Client Information":
                return self.open_add_to_client_information()
            elif choice == "Case data":
                return self.open_add_to_case_data()
            elif choice == "Archived State":
                return self.open_add_to_archived_state()
            elif choice == "Case Location":
                return self.open_add_to_case_location()
            elif choice == "Destruction State":
                return self.open_add_to_destruction_state()
            elif choice == "File Upload Data":
                return self.open_add_to_file_upload_data()
            elif choice == "Deletion Confirmation":
                return self.open_add_to_deletion_confirmation()
            elif choice == "Deletion Logging":
                return self.open_add_to_deletion_logging()
            elif choice == "Case Request":
                return self.open_add_to_archived_case_request()
            elif choice == "Case Drawn By":
                return self.open_add_to_case_drawn_by()
            elif choice == "Case Drawn History":
                return self.open_add_to_case_drawn_history()
        
        
        # Decorate Right Frame    
        optionmenu_var = customtkinter.StringVar(value="Insert Into")
        optionmenu = customtkinter.CTkOptionMenu(self.inner_right_panel, values=["Employee Roles", 
                                                                               "Employee Account", 
                                                                               "User Login Data", 
                                                                               "Client Information", 
                                                                               "Case data", 
                                                                               "Archived State", 
                                                                               "Case Location", 
                                                                               "Destruction State", 
                                                                               "File Upload Data", 
                                                                               "Deletion Confirmation", 
                                                                               "Deletion Logging", 
                                                                               "Case Request", 
                                                                               "Case Drawn By", 
                                                                               "Case Drawn History"],
                                                command=optionmenu_insert,
                                                variable=optionmenu_var)
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Insert into Database:", font=('Roboto', 24))
        Label.grid(row=0, column=0, padx=20, pady=(10, 0))
        optionmenu.grid(row=1, column=0, padx=20, pady=(10, 0))
        
             
        def optionmenu_delete(choice):
            if choice == "Employee Roles":
                return self.open_add_to_employee_roles()
            elif choice == "Employee Account":
                return self.open_add_to_employee_account()
            elif choice == "User Login Data":
                return self.open_add_to_user_login_data()
            elif choice == "Client Information":
                return self.open_add_to_client_information()
            elif choice == "Case data":
                return self.open_add_to_case_data()
            elif choice == "Archived State":
                return self.open_add_to_archived_state()
            elif choice == "Case Location":
                return self.open_add_to_case_location()
            elif choice == "Destruction State":
                return self.open_add_to_destruction_state()
            elif choice == "File Upload Data":
                return self.open_add_to_file_upload_data()
            elif choice == "Deletion Confirmation":
                return self.open_add_to_deletion_confirmation()
            elif choice == "Deletion Logging":
                return self.open_add_to_deletion_logging()
            elif choice == "Case Request":
                return self.open_add_to_archived_case_request()
            elif choice == "Case Drawn By":
                return self.open_add_to_case_drawn_by()
            elif choice == "Case Drawn History":
                return self.open_add_to_case_drawn_history()
        
         
        optionmenu_var = customtkinter.StringVar(value="Delete from")
        optionmenu = customtkinter.CTkOptionMenu(self.inner_right_panel, values=["Employee Roles", 
                                                                               "Employee Account", 
                                                                               "User Login Data", 
                                                                               "Client Information", 
                                                                               "Case data", 
                                                                               "Archived State", 
                                                                               "Case Location", 
                                                                               "Destruction State", 
                                                                               "File Upload Data", 
                                                                               "Deletion Confirmation", 
                                                                               "Deletion Logging", 
                                                                               "Case Request", 
                                                                               "Case Drawn By", 
                                                                               "Case Drawn History"],
                                                command=optionmenu_delete,
                                                variable=optionmenu_var)
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Delete from Database", font=('Roboto', 24))
        Label.grid(row=2, column=0, padx=20, pady=(10, 0))      
        optionmenu.grid(row=3, column=0, padx=20, pady=(10, 0))
        
        
    #------------------------------------------------------------------     
    
    # Clear the page function                         
    def clear_canvas(self):
        """ Clears canvas from right_dashboard before loading the new canvas """
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()
    
    
    # -------------------------------------------- 
    # Popup windows focus functions
    # --------------------------------------------        
    # TODO: Combine these into one function (pass in a value maybe)   
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
                
    
    def open_add_to_archived_case_request(self):
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
            
    
    def open_add_to_case_location(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_case_location(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it
            
            
    def open_add_to_deletion_logging(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = popup.popup_add_to_deletion_logging(self)  # create window if its None or destroyed
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it


        
# Main Function
if __name__ == "__main__":
    app = App()
    # run = Login(app)
    app.mainloop()  