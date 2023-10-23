import customtkinter
from PIL import Image
import tkinter
import tksheet

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
        
        # 1 second update function
        def update():
            # print(user_role_logged_in)
            # self.update()
            self.after(1000, update)
        self.after(1000, update)
        
          
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
        
        # left_side_panel Menu
        self.menu_label = customtkinter.CTkLabel(self.left_side_panel, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.menu_label.grid(row=0, column=0, padx=20, pady=(20, 10))      
        
        # Focus on dashboard first
        self.dashboard()
        
        # buttons on left_side_panel to select canvas     
        self.btn_dashboard = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("dashboard"), fg_color="transparent", width=45, text="", command=lambda: self.dashboard())
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10)

        self.btn_archive = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("archive"), fg_color="transparent", width=45, text="", command=self.archive)
        self.btn_archive.grid(row=2, column=0, padx=20, pady=10)
            
        self.btn_case = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("case"), fg_color="transparent", width=45, text="", command=self.case)
        self.btn_case.grid(row=3, column=0, padx=20, pady=10)
        
        if global_variables.get_id() != 2: # If not archivist
            self.btn_files = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("files"), fg_color="transparent", width=45, text="", command=self.files)
            self.btn_files.grid(row=4, column=0, padx=20, pady=10)
        
        self.btn_client = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("customer"), fg_color="transparent", width=45, text="", command=self.client)
        self.btn_client.grid(row=5, column=0, padx=20, pady=10)
             
        if global_variables.get_id() == 1: # If admin        
            self.btn_admin = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("admin"), fg_color="transparent", width=45, text="", command=self.admin)
            self.btn_admin.grid(row=7, column=0, padx=20, pady=10)
        
        self.btn_user = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("user"), fg_color="transparent", width=45, text="", command=self.user)
        self.btn_user.grid(row=8, column=0, padx=20, pady=10)
        
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
        
        self.notifications = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e", scrollregion = (0,0,2000,10000))
        self.notifications.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.Y, expand=False, padx=10, pady=10)
        
        # Decorate Heading Banner    
        Label = customtkinter.CTkLabel(self.heading_banner, text="Dashboard", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )    
        
        # Decorate Notification Bar
        headers = ['archiveNumber', 'employee', 'dateRequested', 'Location']
        self.data = [[f"{a}",f"{h} {i}",f"{c}",f"{e}"] for a,b,c,d,e,f,g,h,i,j,k,l in refresh_data()]
        # Create table
        # populate Table  
        self.sheet = tksheet.Sheet(self.notifications, data = self.data, height = 800, theme = "dark")
        # self.sheet.grid(row=0, column=0, padx=10, pady=10)
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


        self.sheet.create_header_dropdown(c = 0,
                                            values = ["all", "1", "2", "3"], # TODO: change this to variable from data[0]
                                            set_value = "all",
                                            selection_function = self.header_dropdown_selected,
                                            text = headers[0])
        self.sheet.create_header_dropdown(c = 1,
                                            values = ["all", "a", "b", "c"],
                                            set_value = "all",
                                            selection_function = self.header_dropdown_selected,
                                            text = "Header B Name")
        self.sheet.create_header_dropdown(c = 2,
                                            values = ["all", "x", "y", "z"],
                                            set_value = "all",
                                            selection_function = self.header_dropdown_selected,
                                            text = "Header C Name")
        self.sheet.create_header_dropdown(c = 3,
                                            values = ["all", "x", "y", "z"],
                                            set_value = "all",
                                            selection_function = self.header_dropdown_selected,
                                            text = "Header C Name")
        self.sheet.create_header_dropdown(c = 4,
                                            values = ["all", "x", "y", "z"],
                                            set_value = "all",
                                            selection_function = self.header_dropdown_selected,
                                            text = "Header C Name")

             
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
        
        # Decorate Main Page
        # grab data 
        def refresh_data():
            return db_conn.all_archived_state()
            
        headers = ['case Id', 'State', 'Archive Number', 'Archived Date', 'Date To Be Destroyed', 'Location']
        self.data = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}",f"{g}"] for a,b,c,d,e,f,g in refresh_data()]
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel,data = self.data, theme = "dark", height = 800, width = 1750)
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
        self.data = [[f"{a}",f"{p} {q}",f"{j} {k}",f"{d}",f"{e}",f"{f}",f"{g}"] for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s in gathered_data ]
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel, data = self.data, theme = "dark", height = 800, width = 1750)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        # self.sheet.grid(row=0, column = 0, padx = 10, pady = 10)
        
        self.sheet.headers((f"{x}" for x in headers))
        
        # populate Table
        
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
        self.sheet = tksheet.Sheet(self.inner_right_panel,data = self.data, theme = "dark", height = 800, width = 1750)
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
                                    width = 1750,)

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
        

    def user(self):
        self.clear_canvas()
        # Decorate Right Frame
        
        
    #------------------------------------------------------------------   
    # Function for headers on sheets
    def header_dropdown_selected(self, event = None):
        hdrs = self.sheet.headers()
        # this function is run before header cell data is set by dropdown selection
        # so we have to get the new value from the event
        hdrs[event.column] = event.text
        if all(dd == "all" for dd in hdrs):
            self.sheet.display_rows("all")
        else:
            for c, e in enumerate(hdrs):
                print(c,e)

            # for row in enumerate(self.data):
                # print(row[2])
 
            rows = [rn for rn, row in enumerate(self.data) if all(row[c][1] == e or e == "all" for c, e in enumerate(hdrs))]
            
            self.sheet.display_rows(rows = rows,
                                    all_displayed = False)
        self.sheet.redraw()
            
        # Decorate Main dashboard page
        # If archivist, show to be deleted
        # If attorney, show your cases/analytics
        # If manager, show analytics
        # TODO: User based Dashboard
        
        # Decorate inner right panel
        """
        # grab data 
        data = list(db_conn.case_to_be_destroyed_this_month())
        location = db_conn.all_case_location()
        location_list = list()
        headers = ['caseId', 'archivedState', 'archiveNumber', 'archivedDate', 'DateToBeDestroyed', 'Location']

        # Link location to archiveNumber
        for id_location,location_data in location:
            for id_data,q,w,j,r in data:               
                if id_location == id_data:
                    location_list.append(location_data)
                else:
                    location_list.append("No Location")
        
        #TODO: Add location_list to data          
        final_data = list()                      
        for i in range(len(location_list)):
            new_list = list(data[i]).append(location_list[i])
            print(new_list)
            
        print(type(data))
        print(location)
        print(location_list)
        # Create table
        self.sheet = tksheet.Sheet(self.notifications, height = 800)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        # self.sheet.grid(row=0, column =0, padx = 10, pady = 10)
        
        self.sheet.headers((f"{x}" for x in headers))
        
        # populate Table
        self.sheet.set_sheet_data([[f"{a}", f"{b}", f"{c}", f"{d}",f"{e}",f"{f}"] for a,b,c,d,e,f in data])
        
        # table enable choices listed below:
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
        """
    
    
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