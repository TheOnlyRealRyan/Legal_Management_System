import customtkinter
import add_to_db as db_conn

# ----- POPUP windows Decoration classes
class popup_add_to_employee_roles(customtkinter.CTkToplevel):
    """ add a role to employee_role database"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x250")
        self.title("Employee Roles")
        
        customtkinter.CTkLabel(self, text="Employee Roles", font=("Roboto", 24)).pack(padx=12, pady=10)
     
        txtRoleDescription = customtkinter.CTkEntry(self, placeholder_text="Role Description")
        txtRoleDescription.pack(pady=12, padx=10)
        
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_roles(txtRoleDescription.get())).pack(pady=12, padx=10)

 
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_user_login_data(txtemployeeId.get(), txtUsername.get(), txtpassword.get())).pack(pady=12, padx=10)
      
      
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_client_information(txtName.get(), txtSurname.get(), txtGender.get(), txtDOB.get())).pack(pady=12, padx=10)


class popup_add_to_case_data(customtkinter.CTkToplevel):
    """ Popup window to add a case to case_data database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_archived_state(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to archived_state database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_case_location(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to case_location database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)

class popup_add_to_destruction_state(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to destruction_state database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_file_upload_data(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_deletion_confirmation(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_deletion_logging(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_case_request(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_case_drawn_by(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_case_drawn_history(customtkinter.CTkToplevel):
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)


class popup_add_to_archived_case_request(customtkinter.CTkToplevel):
    """ Popup window to add a new employee to archived_case_request database"""
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
        customtkinter.CTkButton(self, text="Submit", command=lambda: db_conn.add_to_employee_account(txtAge.get(), txtName.get(), txtSurname.get(), txtGender.get(), txtBirth.get(), txtRoleId.get())).pack(pady=12, padx=10)
