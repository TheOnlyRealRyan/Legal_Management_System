import customtkinter
import add_to_db as db_conn
from tkcalendar import Calendar
from tkinter.filedialog import askopenfile
import upload_file
import global_variables

# POPUP windows Decoration classes
class popup_add_to_employee_roles(customtkinter.CTkToplevel):
    """ Popup window to add to employee_role database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x250")
        self.title("Employee Roles")
        
        customtkinter.CTkLabel(self, text="Employee Roles", font=("Roboto", 24)).pack(padx=12, pady=10)
     
        txtRoleDescription = customtkinter.CTkEntry(self, placeholder_text="Role Description")
        txtRoleDescription.pack(pady=12, padx=10)
        
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_roles(txtRoleDescription.get())).pack(pady=12, padx=10)

 
class popup_add_to_employee_account(customtkinter.CTkToplevel):
    """ Popup window to add to employee_account database"""
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
        
        customtkinter.CTkLabel(self, text="Date Of Birth", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtBirth = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        txtBirth.pack(padx=12, pady=10)
        
        customtkinter.CTkLabel(self, text="Enter role ID", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtRoleId = customtkinter.CTkEntry(self, placeholder_text="Role ID")
        txtRoleId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Gender (M/F)", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtGender = customtkinter.CTkEntry(self, placeholder_text="Gender")
        txtGender.pack(pady=12, padx=10)
        

        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account( txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_user_login_data(customtkinter.CTkToplevel):
    """ Popup window to add to employee_account database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_user_login_data(txtemployeeId.get(), txtUsername.get(), txtpassword.get())).pack(pady=12, padx=10)
      
      
class popup_add_to_client_information(customtkinter.CTkToplevel):
    """ Popup window to add to client_information database"""
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
        
        customtkinter.CTkLabel(self, text="Date Of Birth", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtDOB = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        txtDOB.pack(padx=12, pady=10)
               
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_client_information(txtName.get(), txtSurname.get(), txtGender.get(), txtDOB.get())).pack(pady=12, padx=10)


class popup_add_to_case_data(customtkinter.CTkToplevel):
    """ Popup window to add to case_data database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x1000")
        self.title("Case Data")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter client Id", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtclientId = customtkinter.CTkEntry(self, placeholder_text="clientId")
        txtclientId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter employee Id", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtemployeeId = customtkinter.CTkEntry(self, placeholder_text="employeeId")
        txtemployeeId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter description", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtdescription = customtkinter.CTkEntry(self, placeholder_text="description", height = 30)
        txtdescription.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Department", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtDepartment = customtkinter.CTkEntry(self, placeholder_text="Department")
        txtDepartment.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter date Of Case Open", font=("Roboto", 24)).pack(padx=12, pady=10)
        case_open = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        case_open.pack(padx=12, pady=10)
        
        customtkinter.CTkLabel(self, text="Enter date Uploaded", font=("Roboto", 24)).pack(padx=12, pady=10)
        date_upload = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        date_upload.pack(padx=12, pady=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_case_data(txtclientId.get(), txtemployeeId.get(), txtdescription.get(), txtDepartment.get(), case_open.get_date(), date_upload.get_date())).pack(pady=12, padx=10)


class popup_add_to_archived_state(customtkinter.CTkToplevel):
    """ Popup window to add to archived_state database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Employee Account")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter case Id", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtcaseId = customtkinter.CTkEntry(self, placeholder_text="caseId")
        txtcaseId.pack(pady=12, padx=10)
        
        def optionmenu_insert(choice):
            print("Inserted")
        
        customtkinter.CTkLabel(self, text="Choose Archive State", font=('Roboto', 24)).pack(pady=12, padx=10)
           
        optionmenu_var = customtkinter.StringVar(value="Archive State")
        optionmenu = customtkinter.CTkOptionMenu(self, values=["Archived", 
                                                                               "Live"],
                                                command=optionmenu_insert,
                                                variable=optionmenu_var)
        optionmenu.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Archived Date", font=("Roboto", 24)).pack(padx=12, pady=10)
        archive_date = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        archive_date.pack(padx=12, pady=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_archived_state(txtcaseId.get(), optionmenu.get(), archive_date.get_date())).pack(pady=12, padx=10)


class popup_add_to_case_location(customtkinter.CTkToplevel):
    """ Popup window to add to case_location database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Employee Account")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter case Id", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtcaseId = customtkinter.CTkEntry(self, placeholder_text="caseId")
        txtcaseId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter location", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtlocation = customtkinter.CTkEntry(self, placeholder_text="location")
        txtlocation.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_case_location(txtcaseId.get(), txtlocation.get())).pack(pady=12, padx=10)

class popup_add_to_destruction_state(customtkinter.CTkToplevel):
    """ Popup window to add to destruction_state database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Destruction State")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter case Id", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtcaseId = customtkinter.CTkEntry(self, placeholder_text="caseId")
        txtcaseId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Destruction State", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtState = customtkinter.CTkEntry(self, placeholder_text="State")
        txtState.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_destruction_state(txtcaseId.get(), txtState.get())).pack(pady=12, padx=10)


class popup_add_to_file_upload_data(customtkinter.CTkToplevel):
    """ Popup window to add to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("File Upload")
     
        # Decorate here
        customtkinter.CTkLabel(self, text="Enter File name", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtName = customtkinter.CTkEntry(self, placeholder_text="Name")
        txtName.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter Case ID", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtcaseId = customtkinter.CTkEntry(self, placeholder_text="caseId")
        txtcaseId.pack(pady=12, padx=10)
        
        customtkinter.CTkLabel(self, text="Enter date Recieved", font=("Roboto", 24)).pack(padx=12, pady=10)
        recieved = Calendar(self, selectmode='day', font=("Roboto", 12),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white', height = 20, width = 20)
        recieved.pack(padx=12, pady=10)
        
        
        def get_file():            
            # TODO: Call Upload to cloud function here
            filename = askopenfile() # open file explorer and return the path
            upload_file.upload_object_from_filename(filename)
            
            
        customtkinter.CTkButton(self, text="Grab from Computer", command=lambda: get_file()).pack(pady=12, padx=10)
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_file_upload_data(txtName.get(), txtcaseId.get(), recieved.get_date())).pack(pady=12, padx=10)


class popup_add_to_deletion_confirmation(customtkinter.CTkToplevel):
    """ Popup window to add to deletion_confirmation database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Deletion Confirmation")

        # Decorate here        
        customtkinter.CTkLabel(self, text="Enter caseId", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtcaseId = customtkinter.CTkEntry(self, placeholder_text="id")
        txtcaseId.pack(pady=12, padx=10)

        # Todo: grab the manager Id
        employeeId2 = 1 # manager ID
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_deletion_confirmation(txtcaseId.get(), 
                                                                                                          global_variables.get_id(),
                                                                                                          employeeId2,
                                                                                                          True,
                                                                                                          False                                                                                                         
                                                                                                          )).pack(pady=12, padx=10)

        
        # Submit Button
        # customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_deletion_logging(customtkinter.CTkToplevel):
    """ Popup window to add to deletion_logging database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Deletion Logging")
     
        # Decorate here
        
        # Submit Button
        # customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_archived_case_request(customtkinter.CTkToplevel):
    """ Popup window to add to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Archive Request")
     
        # Decorate here        
        customtkinter.CTkLabel(self, text="Enter Archive Number", font=("Roboto", 24)).pack(padx=12, pady=10)
        txtArchive = customtkinter.CTkEntry(self, placeholder_text="number")
        txtArchive.pack(pady=12, padx=10)
        
        # Submit Button
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_archived_case_request(txtArchive.get())).pack(pady=12, padx=10)


class popup_add_to_case_drawn_by(customtkinter.CTkToplevel):
    """ Popup window to add to employee_account database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Case Drawn By")
     
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_case_drawn_by(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_case_drawn_history(customtkinter.CTkToplevel):
    """ Popup window to add to case_drawn_history database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x750")
        self.title("Case Drawn History")
     
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


