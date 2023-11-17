import customtkinter
from PIL import Image
import tkinter
import tksheet 
"""
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from string import ascii_letters
import pandas as pd
import matplotlib.pyplot as plt
"""

import grab_from_db as db_conn
import create_db as create_db
from validatePassword import *
import popup
import global_variables as global_variables


# TODO: change title headings from database titles to normal titles
# TODO: Adapt tables to only show what user logged in should see
# TODO: Search and filter


# Initialise Appearance for customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  
        
        # open login page
        self.login()
    
    
    def clear_canvas(self):
        """ Clears canvas from right_dashboard before loading the new canvas """
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()     
            
            
    def load_image(self, img_picked):
        """Load an image only if its called using the image name"""
        try:
            resource_path = "resources/icons_variation_2/"                
            img= (Image.open(f"{resource_path}{img_picked}.png"))
            resized_image= img.resize((30,30), Image.LANCZOS)
            return customtkinter.CTkImage(resized_image)             
        except IOError:
            print("File not found") 
            pass
        
        
    def login_success(self):
        """Checks to see if the username and password is correct then sets the session user id and role"""       
        username = self.username.get() # "admin"
        password = self.password.get() # "admin"
        success = validate(username, password)
        if success:         
            # Set Role and employee ID for session                 
            global_variables.set_role(db_conn.login_employee_roles(username))
            global_variables.set_id(db_conn.login_employee_id(username)) 
            print(f"--> Employee {global_variables.get_id()} logged in")
            print("--> Login Successful")
            # Destroy Login Pagge. Load Main Page
            for widget in self.login_page.winfo_children():
                widget.destroy()
            self.login_page.destroy()
            self.load_main_page()  
    
    
    # --------------------------------------------------------------------------------------------------
    # Different Pages that can be loaded
    # --------------------------------------------------------------------------------------------------  
    
    
    def load_main_page(self):    
        self.title("Law Firm Management Software")
        # Dimensions relating to screen size
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()-75))
        
               
        # root page
        self.main_container = customtkinter.CTkCanvas(self, bg="#00253e")
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkCanvas(self.main_container, width=125, bg="#00406c")
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
       
        # Configure the weights of rows in left_side_panel
        self.left_side_panel.grid_rowconfigure((7), weight=6)
        
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
        
        if global_variables.get_id() != 3: # If not archivist
            self.btn_files = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("files"), fg_color="transparent", width=45, text="", command=self.files)
            self.btn_files.grid(row=5, column=0, padx=20, pady=10)
        
        self.btn_client = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("customer"), fg_color="transparent", width=45, text="", command=self.client)
        self.btn_client.grid(row=6, column=0, padx=20, pady=10)
        
        
        self.btn_logout = customtkinter.CTkButton(self.left_side_panel, image=self.load_image("logout"), fg_color="transparent", width=45, text="", command=lambda: logout())
        self.btn_logout.grid(row=8, column=0, padx=20, pady=10)
        
        def logout():
            for widget in self.main_container.winfo_children():
                widget.destroy()
            self.main_container.destroy()
            self.login()
        
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
    
    
    def dashboard(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)       
        
        self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=800, bg="#00253e")
        self.inner_right_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate Heading Banner    
        try:
            name = "".join(db_conn.grab_username(global_variables.get_id())[0])
        except:
            name = "admin"
        
        
        Label = customtkinter.CTkLabel(self.heading_banner, text=f"Hello {name}!", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )    

        # Decorate inner panel        
        
        if global_variables.get_role() == 4: # if Attorney
            self.my_cases_panel = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.my_cases_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.my_cases_panel, text="My cases", width=30, height=30, font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=(10,10), pady=(10,10)) 

            # Create table
            self.sheet = tksheet.Sheet(self.my_cases_panel, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     

            # grab data 
            gathered_data = db_conn.case_data_of_employee(global_variables.get_id())
            headers = ['id', 'Client', 'Employee', 'Description', 'Department', 'Date of Open', 'Date Closed']
            self.data = [[f"{a}",f"{b} {c}",f"{d} {e}",f"{f}",f"{g}",f"{h}",f"{i}"] for a,b,c,d,e,f,g,h,i in gathered_data ]
            
            self.sheet.headers((f"{x}" for x in headers))
            self.sheet.data_reference(self.data)   

         
        def refresh_table():
            try:
                gathered_data = db_conn.case_data_of_employee(global_variables.get_id())
                self.data = [[f"{a}",f"{b} {c}",f"{d} {e}",f"{f}",f"{g}",f"{h}",f"{i}"] for a,b,c,d,e,f,g,h,i in gathered_data ]
                print("--> Updated Table")
            except:
                print("--> Wrong user")          
        
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)
         
            
        # TODO: Analytics    
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Analytics and Metrics TBC", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
                   
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Graph of cases closed over time here...", font=('Roboto', 30))
        Label.grid(row=1, column=0, padx=10, pady=10 )   
        
        # if role is attorney, show their current cases
        # case_data_of_employee()
        
        # TEMPORARY!
        """
        def create_plot():
            sns.set(style="white")

            # Generate a large random dataset
            dataset = db_conn.all_case_data()
            # print(dataset)
            rs = np.random.RandomState(33)
            d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                            columns=list(ascii_letters[26:]))

            # Compute the correlation matrix
            corr = d.corr()

            # Generate a mask for the upper triangle
            mask = np.zeros_like(corr, dtype=np.bool_)
            mask[np.triu_indices_from(mask)] = True

            # Set up the matplotlib figure
            f, ax = plt.subplots(figsize=(11, 9))

            # Generate a custom diverging colormap
            cmap = sns.diverging_palette(220, 10, as_cmap=True)

            # Draw the heatmap with the mask and correct aspect ratio
            sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                        square=True, linewidths=.5, cbar_kws={"shrink": .5})

            return f

        # Load table
        table = create_plot()
        canvas = FigureCanvasTkAgg(table, master=self.inner_right_panel)  # A tk.DrawingArea.
        # canvas.draw()
        canvas.get_tk_widget().pack()
        """
        
    def notification(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)


        # Decorate Heading Banner    
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Notifications", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )  
        
        
        def optionmenu_options(choice):
            if choice == "Archival Retrieval Requests":
                return self.open_popup("remove_archivedCaseRequest")
            elif choice == "Deletion Requests":
                return self.open_popup("update_deletionConfirm")
            elif choice == "Destruction Dates":
                return self.open_popup("destructionState")
            
                 
        optionmenu_var = customtkinter.StringVar(value="Mark Complete")
        optionmenu = customtkinter.CTkOptionMenu(self.heading_banner, values=["Archival Retrieval Requests",
                                                                                "Deletion Requests", 
                                                                                "Destruction Dates"],
                                                command=optionmenu_options,
                                                variable=optionmenu_var)
              
        optionmenu.grid(row=0, column=11, padx=20, pady=(10, 10))
        
        # if role is a attorney, show what archive requests they have. show their deletion requests. 
        if global_variables.get_role() == 4:
            self.archive_requests_panel = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.archive_requests_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.archive_requests_panel, text="Archival Retrieval Requests", width=30, height=30, font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=(10,10), pady=(10,10)) 

            # Create table
            self.sheet4 = tksheet.Sheet(self.archive_requests_panel, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet4.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet4.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     
            
            # grab data 
            headers = ['Archive Number', 'Employee ID', 'Date Requested']
            self.sheet4.headers((f"{x}" for x in headers))
            
            gathered_data4 = db_conn.my_archive_case_request(global_variables.get_id())
            self.data4 = [[f"{a}",f"{b}", f"{c}"] for a,b,c in gathered_data4]
            self.sheet4.data_reference(self.data4)   
            
            
            self.my_deletion_requests_panel = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.my_deletion_requests_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.my_deletion_requests_panel, text="My Deletion Requests", width=30, height=30, font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=(10,10), pady=(10,10)) 

            # Create table
            self.sheet5 = tksheet.Sheet(self.my_deletion_requests_panel, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet5.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet5.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     
            
            # grab data 
            headers = ['Case ID', 'Employee ID 1', 'Employee ID 2', 'Employee 1 Confirmed','Employee 2 Confirmed']
            self.sheet5.headers((f"{x}" for x in headers))
            
            gathered_data5 = db_conn.my_deletion_requests(global_variables.get_id())
            self.data5 = [[f"{a}",f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in gathered_data5]
            self.sheet5.data_reference(self.data5)
        
        # Decorate Archival Retrieval Requests Notification Bar
        
        if global_variables.get_role() != 4:
            self.archival = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.archival.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.archival, text="Archival Retrieval Requests", width=30, height=30, font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=(10,10), pady=(10,10)) 
            # Label.grid(row=0, column=0, padx=20, pady=(10, 10))
            # TODO: fix location of filter button
            # btn_filter = customtkinter.CTkButton(self.archival, text="", image=self.load_image("filter"), fg_color="transparent", width=30, height=30, command= lambda: print("-->filter Not Implemented"))
            # btn_filter.pack(side=tkinter.TOP, anchor=tkinter.NE, padx=(10,10), pady=(10,10))
            # btn_filter.grid(row=0, column=0, padx=20, pady=(10, 10))

            # Create table
            self.sheet = tksheet.Sheet(self.archival, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     
            
            # grab data 
            headers = ['Archive Number', 'Employee', 'Employee ID', 'Date Requested', 'Location']
            self.sheet.headers((f"{x}" for x in headers))
            
            gathered_data = db_conn.all_archived_case_request()
            self.data = [[f"{a}",f"{b} {c}",f"{d}",f"{e}",f"{f}"] for a,b,c,d,e,f in gathered_data]
            self.sheet.data_reference(self.data)                   
            
                   
        # Decorate Deletion Requests Notification Bar
        if global_variables.get_role() == 2 or global_variables.get_role() == 1: # manager or admin role
            self.deletion = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.deletion.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.deletion, text="Deletion Requests", font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, padx=10, pady=10)

            # Create table
            self.sheet2 = tksheet.Sheet(self.deletion, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet2.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     
            
            # grab data 
            headers = ['Case ID', 'Employee Requested']
            self.sheet2.headers((f"{x}" for x in headers))
            
            gathered_data2 = db_conn.all_deletion_confirmation()
            self.data2 = [[f"{a}",f"{b} {c}"] for a,b,c in gathered_data2]
            self.sheet2.data_reference(self.data2)
                   
            
            
        # Decorate Destruction Dates Notification Bar
        if global_variables.get_role() != 4: # manager or admin or archival role
            self.destruction = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
            self.destruction.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            
            Label = customtkinter.CTkLabel(self.destruction, text="Destruction Dates", font=('Roboto', 24))
            Label.pack(side=tkinter.TOP, padx=10, pady=10)          
  
            # Create table
            self.sheet3 = tksheet.Sheet(self.destruction, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
            self.sheet3.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
            self.sheet3.enable_bindings(("single_select",
                                "double_click_column_resize",
                                "column_width_resize",
                                "row_select",
                                "column_width_resize",
                                "arrowkeys",
                                "copy"))     
            
            # grab data 
            headers = ['Archive Number', 'Archived State',  'Archived Date', 'Date To Be Destroyed', 'Location']
            self.sheet3.headers((f"{x}" for x in headers))
            
            gathered_data3 = db_conn.all_archived_state()
            self.data3 = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data3]
            self.sheet3.data_reference(self.data3)
                
        def refresh_table():
            try:
                gathered_data = db_conn.all_archived_case_request()
                self.data = [[f"{a}",f"{b} {c}",f"{d}",f"{e}",f"{f}"] for a,b,c,d,e,f in gathered_data]
                self.sheet.data_reference(self.data)
                print("--> Updated Table")
            except:
                print("--> Wrong user") 
            try:   
                gathered_data2 = db_conn.all_deletion_confirmation()
                self.data2 = [[f"{a}",f"{b} {c}"] for a,b,c in gathered_data2]
                self.sheet2.data_reference(self.data2)
                print("--> Updated Table")
            except:
                print("--> Wrong user") 
            try:
                gathered_data3 = db_conn.case_to_be_destroyed_this_month()
                self.data3 = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data3]
                self.sheet3.data_reference(self.data3)  
                print("--> Updated Table") 
            except:
                print("--> Wrong user")      
            try:
                gathered_data4 = db_conn.my_archive_case_request()
                self.data4 = [[f"{a}",f"{b}", f"{c}"] for a,b,c in gathered_data4]  
                self.sheet4.data_reference(self.data4)  
                print("--> Updated Table") 
            except:
                print("--> Wrong user")    
            try:
                gathered_data5 = db_conn.my_deletion_requests(global_variables.get_id())
                self.data5 = [[f"{a}",f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in gathered_data5]
                self.sheet5.data_reference(self.data5) 
                print("--> Updated Table") 
            except:
                print("--> Wrong user")     
                  
                
                       
            
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)
    
    
    def archive(self):
        self.clear_canvas()
        
        # Layout
        self.heading_banner = customtkinter.CTkCanvas(self.right_dashboard, height = 50, bg="#00253e")
        self.heading_banner.pack(side=tkinter.TOP, fill=tkinter.X, expand=False, padx=10, pady=10)
        
        # self.inner_right_panel = customtkinter.CTkCanvas(self.right_dashboard, width=1500, bg="#00253e")
        # self.inner_right_panel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.archivedCases_panel = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
        self.archivedCases_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.caseDrawnBy_panel = customtkinter.CTkCanvas(self.right_dashboard,width=500, bg="#00253e")
        self.caseDrawnBy_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # Decorate heading Banner   
        self.heading_banner.grid_columnconfigure((1,2,3), weight=2)  
           
        Label = customtkinter.CTkLabel(self.heading_banner, text="Archive", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        
        def optionmenu_options(choice):
            if choice == "New Archive":
                return self.open_popup("archiveState")
            elif choice == "Request Archive":
                return self.open_popup("archivedCaseRequest")
            elif choice == "Give Location":
                return self.open_popup("CaseLocation")            
        
         
        optionmenu_var = customtkinter.StringVar(value="Archive Functions")
        optionmenu = customtkinter.CTkOptionMenu(self.heading_banner, values=["New Archive",
                                                                                "Request Archive", 
                                                                                "Give Location"],
                                                command=optionmenu_options,
                                                variable=optionmenu_var)
              
        optionmenu.grid(row=0, column=11, padx=20, pady=(10, 10))
        
        
        # Decorate Main Page
        # archived cases       
        Label = customtkinter.CTkLabel(self.archivedCases_panel, text="Archived Cases", font=('Roboto', 24))
        Label.pack(side=tkinter.TOP, padx=10, pady=10) 
        
        # Create table
        self.sheet = tksheet.Sheet(self.archivedCases_panel, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))     
        
        # grab data 
        headers = ['Archive Number', 'State', 'Archived Date', 'Date To Be Destroyed', 'Location']
        self.sheet.headers((f"{x}" for x in headers))
        
        gathered_data = db_conn.all_archived_state()
        self.data = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data]
        self.sheet.data_reference(self.data)        
        
        # case drawn by     
        Label = customtkinter.CTkLabel(self.caseDrawnBy_panel, text="Case Drawn By", font=('Roboto', 24))
        Label.pack(side=tkinter.TOP, padx=10, pady=10) 
                     
        # Create table
        self.sheet2 = tksheet.Sheet(self.caseDrawnBy_panel, theme = "dark", height = 800, width = 500, show_row_index=False, show_top_left=False)
        self.sheet2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.sheet2.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))     
        
        # grab data 
        headers = ['Archive Number', 'Employee ID', 'Date Drawn Out']
        self.sheet2.headers((f"{x}" for x in headers))
        
        gathered_data = db_conn.all_case_drawn_by()
        self.data2 = [[f"{a}",f"{b}",f"{c}"] for a,b,c in gathered_data] 
        self.sheet2.data_reference(self.data2)
                
        def refresh_table():
            gathered_data = db_conn.all_archived_state()
            self.data = [[f"{a}",f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data]
            self.sheet.data_reference(self.data)
            
            gathered_data2 = db_conn.all_case_drawn_by()
            self.data2 = [[f"{a}",f"{b}",f"{c}"] for a,b,c in gathered_data2] 
            self.sheet2.data_reference(self.data2)
            print("--> Updated Table")
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)
        
        
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
        
        def optionmenu_options(choice):
            if choice == "New Case":
                return self.open_popup("case")
            elif choice == "Delete Case Request":
                return self.open_popup("deletionConfirm")           
        
         
        optionmenu_var = customtkinter.StringVar(value="Case Functions")
        optionmenu = customtkinter.CTkOptionMenu(self.heading_banner, values=["New Case",
                                                                                "Delete Case Request"],
                                                command=optionmenu_options,
                                                variable=optionmenu_var)
              
        optionmenu.grid(row=0, column=11, padx=20, pady=(10, 10))
        
        
        # Decorate inner right panel
        
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
        
        # grab data 
        gathered_data = db_conn.all_case_data()
        headers = ['ID', 'Client', 'Employee', 'Description', 'Department', 'Date of Open', 'Date Closed']
        self.data = [[f"{a}",f"{b} {c}",f"{d} {e}",f"{f}",f"{g}",f"{h}",f"{i}"] for a,b,c,d,e,f,g,h,i in gathered_data ]
        self.sheet.headers((f"{x}" for x in headers))
        self.sheet.data_reference(self.data)   
            
        def refresh_table():
            gathered_data = db_conn.all_case_data()
            self.data = [[f"{a}",f"{b} {c}",f"{d} {e}",f"{f}",f"{g}",f"{h}",f"{i}"] for a,b,c,d,e,f,g,h,i in gathered_data ]
            self.sheet.data_reference(self.data)
            print("--> Updated Table")
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)
    
        
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
        
        Label = customtkinter.CTkLabel(self.heading_banner, text="Cloud", font=('Roboto', 30))
        Label.grid(row=0, column=0, padx=10, pady=10 )
        
        def optionmenu_options(choice):
            if choice == "Download File":
                return self.open_popup("fileDownload")
            elif choice == "Upload File":
                return self.open_popup("fileUpload")           
        
         
        optionmenu_var = customtkinter.StringVar(value="Cloud Functions")
        optionmenu = customtkinter.CTkOptionMenu(self.heading_banner, values=["Download File",
                                                                                "Upload File"],
                                                command=optionmenu_options,
                                                variable=optionmenu_var)
              
        optionmenu.grid(row=0, column=11, padx=20, pady=(10, 10))
        
        
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))
        # grab data 
        headers = ['File ID', 'File Name', 'Case ID', 'Recieved Date', 'Date Uploaded']
        self.sheet.headers((f"{x}" for x in headers))
        
        gathered_data = db_conn.all_file_upload_data()
        self.data = [[f"{a}", f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in gathered_data ]
        self.sheet.data_reference(self.data)
                
        def refresh_table():
            gathered_data = db_conn.all_file_upload_data()
            self.data = [[f"{a}", f"{b}", f"{c}", f"{d}", f"{e}"] for a,b,c,d,e in gathered_data ]
            self.sheet.data_reference(self.data)
            print("--> Updated Table")
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)


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
        
        def optionmenu_options(choice):
            if choice == "New Client":
                return self.open_popup("client")
            elif choice == "Remove Client":
                return self.open_popup("remove_client")          
        
         
        optionmenu_var = customtkinter.StringVar(value="Client Functions")
        optionmenu = customtkinter.CTkOptionMenu(self.heading_banner, values=["New Client",
                                                                                "Remove Client"],
                                                command=optionmenu_options,
                                                variable=optionmenu_var)
              
        optionmenu.grid(row=0, column=11, padx=20, pady=(10, 10))
        
        
        # Decorate inner right panel      
        # Create table
        self.sheet = tksheet.Sheet(self.inner_right_panel, theme = "dark", height = 800, width = 1750, show_row_index=False, show_top_left=False)
        self.sheet.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.sheet.enable_bindings(("single_select",
                            "double_click_column_resize",
                            "column_width_resize",
                            "row_select",
                            "column_width_resize",
                            "arrowkeys",
                            "copy"))     
        
        # grab data 
        headers = ['ID', 'Name', 'Surname', 'Gender', 'Date of Birth']
        self.sheet.headers((f"{x}" for x in headers))
        
        gathered_data = db_conn.all_client_information()
        self.data = [[f"{a}", f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data]
        self.sheet.data_reference(self.data)
                
        def refresh_table():
            gathered_data = db_conn.all_client_information()
            self.data = [[f"{a}", f"{b}",f"{c}",f"{d}",f"{e}"] for a,b,c,d,e in gathered_data]
            self.sheet.data_reference(self.data)
            print("--> Updated Table")
                
        btn_refresh= customtkinter.CTkButton(self.heading_banner, text= "", image=self.load_image("refresh"), fg_color="transparent", width=30, height=30, command= lambda: refresh_table())
        btn_refresh.grid(row=0, column=10, padx=10, pady=10)
    
    
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
                return self.open_popup("role")
            elif choice == "Employee Account":
                return self.open_popup("account")
            elif choice == "User Login Data":
                return self.open_popup("login")
            elif choice == "Client Information":
                return self.open_popup("client")
            elif choice == "Case data":
                return self.open_popup("case")
            elif choice == "Archived State":
                return self.open_popup("archiveState")
            elif choice == "Case Location":
                return self.open_popup("CaseLocation")
            elif choice == "Destruction State":
                return self.open_popup("destructionState")
            elif choice == "File Upload Data":
                return self.open_popup("fileUpload")
            elif choice == "Deletion Confirmation":
                return self.open_popup("DeletionConfirm")
            elif choice == "Deletion Logging":
                return self.open_popup("DeletionLogging")
            elif choice == "Case Request":
                return self.open_popup("archivedCaseRequest")
            elif choice == "Case Drawn By":
                return self.open_popup("CaseDrawnBy")
            elif choice == "Case Drawn History":
                return self.open_popup("CaseDrawnHistory")
        
        
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
                return self.open_popup("remove_role")
            elif choice == "Employee Account":
                return self.open_popup("remove_account")
            elif choice == "User Login Data":
                return self.open_popup("remove_login")
            elif choice == "Client Information":
                return self.open_popup("remove_client")
            elif choice == "Case data":
                return self.open_popup("remove_case")
            elif choice == "Archived State":
                return self.open_popup("remove_archiveState")
            elif choice == "Case Location":
                return self.open_popup("remove_CaseLocation")
            elif choice == "Destruction State":
                return self.open_popup("remove_destructionState")
            elif choice == "File Upload Data":
                return self.open_popup("remove_fileUpload")
            elif choice == "Deletion Confirmation":
                return self.open_popup("remove_DeletionConfirm")
            elif choice == "Deletion Logging":
                return self.open_popup("remove_DeletionLogging")
            elif choice == "Case Request":
                return self.open_popup("remove_archivedCaseRequest")
            elif choice == "Case Drawn By":
                return self.open_popup("remove_CaseDrawnBy")
            elif choice == "Case Drawn History":
                return self.open_popup("remove_CaseDrawnHistory")
        
         
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
        
        
        def optionmenu_update(choice):
            if choice == "Employee Roles":
                return self.open_popup("remove_role")
            elif choice == "Employee Account":
                return self.open_popup("remove_account")
            elif choice == "User Login Data":
                return self.open_popup("remove_login")
            elif choice == "Client Information":
                return self.open_popup("remove_client")
            elif choice == "Case data":
                return self.open_popup("remove_case")
            elif choice == "Archived State":
                return self.open_popup("remove_archiveState")
            elif choice == "Case Location":
                return self.open_popup("remove_CaseLocation")
            elif choice == "Destruction State":
                return self.open_popup("remove_destructionState")
            elif choice == "File Upload Data":
                return self.open_popup("remove_fileUpload")
            elif choice == "Deletion Confirmation":
                return self.open_popup("remove_DeletionConfirm")
            elif choice == "Deletion Logging":
                return self.open_popup("remove_DeletionLogging")
            elif choice == "Case Request":
                return self.open_popup("remove_archivedCaseRequest")
            elif choice == "Case Drawn By":
                return self.open_popup("remove_CaseDrawnBy")
            elif choice == "Case Drawn History":
                return self.open_popup("remove_CaseDrawnHistory")
        
         
        optionmenu_var = customtkinter.StringVar(value="Update from")
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
                                                command=optionmenu_update,
                                                variable=optionmenu_var)

        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Update Database", font=('Roboto', 24))
        Label.grid(row=4, column=0, padx=20, pady=(10, 0))      
        optionmenu.grid(row=5, column=0, padx=20, pady=(10, 0))
        
    
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Create/Clear New Database", font=('Roboto', 24))
        Label.grid(row=6, column=0, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.inner_right_panel, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= lambda: create_db.create_database())
        button.grid(row=7, column=0, padx=5, pady=5) 
        
        Label = customtkinter.CTkLabel(self.inner_right_panel, text="Populate Database", font=('Roboto', 24))
        Label.grid(row=8, column=0, padx=10, pady=10 )
        
        button = customtkinter.CTkButton(self.inner_right_panel, text= "", image=self.load_image("add"), fg_color="transparent", width=30, height=30, command= lambda: create_db.populate_database())
        button.grid(row=9, column=0, padx=5, pady=5) 


    # ----------------------------------------------------------------------------------------  
    # Popup windows focus function
    # ----------------------------------------------------------------------------------------    
    
    def open_popup(self, popupName):
        """Using a string input to indicate which popup window should be called"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            if popupName == "role": # INSERTION Segment --------------------------
                self.toplevel_window = popup.popup_add_to_employee_roles(self)  # create window if its None or destroyed
            elif popupName == "account":
                self.toplevel_window = popup.popup_add_to_employee_account(self) 
            elif popupName == "login":
                self.toplevel_window = popup.popup_add_to_user_login_data(self)
            elif popupName == "client":
                self.toplevel_window = popup.popup_add_to_client_information(self)
            elif popupName == "case":
                self.toplevel_window = popup.popup_add_to_case_data(self)
            elif popupName == "archiveState":
                self.toplevel_window = popup.popup_add_to_archived_state(self)
            elif popupName == "destructionState":
                self.toplevel_window = popup.popup_add_to_destruction_state(self)
            elif popupName == "fileUpload":
                self.toplevel_window = popup.popup_add_to_file_upload_data(self)
            elif popupName == "deletionConfirm":
                self.toplevel_window = popup.popup_add_to_deletion_confirmation(self)
            elif popupName == "archivedCaseRequest":
                self.toplevel_window = popup.popup_add_to_archived_case_request(self)
            elif popupName == "CaseDrawnBy":
                self.toplevel_window = popup.popup_add_to_case_drawn_by(self)
            elif popupName == "CaseDrawnHistory":
                self.toplevel_window = popup.popup_add_to_case_drawn_history(self)
            elif popupName == "CaseLocation":
                self.toplevel_window = popup.popup_add_to_case_location(self)
            elif popupName == "DeletionLogging":
                self.toplevel_window = popup.popup_add_to_deletion_logging(self)
            elif popupName == "fileDownload":
                self.toplevel_window = popup.popup_download_from_cloud(self)
            elif popupName == "remove_role": # DELETION Segment --------------------------
                self.toplevel_window = popup.popup_remove_employee_role(self)
            elif popupName == "remove_account":
                self.toplevel_window = popup.popup_remove_employee_account(self) 
            elif popupName == "remove_login":
                self.toplevel_window = popup.popup_remove_user_login_data(self)
            elif popupName == "remove_client":
                self.toplevel_window = popup.popup_remove_client_information(self)
            elif popupName == "remove_case":
                self.toplevel_window = popup.popup_remove_case_data(self)
            elif popupName == "remove_archiveState":
                self.toplevel_window = popup.popup_remove_archived_state(self)
            elif popupName == "remove_destructionState":
                self.toplevel_window = popup.popup_remove_destruction_state(self)
            elif popupName == "remove_fileUpload":
                self.toplevel_window = popup.popup_remove_file_upload_data(self)
            elif popupName == "remove_deletionConfirm":
                self.toplevel_window = popup.popup_remove_deletion_confirmation(self)
            elif popupName == "remove_archivedCaseRequest":
                self.toplevel_window = popup.popup_remove_archived_case_request(self)
            elif popupName == "remove_CaseDrawnBy":
                self.toplevel_window = popup.popup_remove_case_drawn_by(self)
            elif popupName == "remove_CaseDrawnHistory":
                self.toplevel_window = popup.popup_remove_case_drawn_history(self)
            elif popupName == "remove_CaseLocation":
                self.toplevel_window = popup.popup_remove_case_location(self)
            elif popupName == "remove_DeletionLogging":
                self.toplevel_window = popup.popup_remove_deletion_logging(self)
            elif popupName == "update_deletionConfirm": # UPDATE SEGMENT --------------------------------------------------
                self.toplevel_window = popup.popup_update_deletion_confirmation(self)    
            else:
                print("Popup failed")
                                              
            self.toplevel_window.after(50, self.toplevel_window.lift) # Focus on popup window after 50ms
        else:
            self.toplevel_window.focus()  # if window exists focus it               
    
      
# Main Function
if __name__ == "__main__":
    app = App()
    app.mainloop()  