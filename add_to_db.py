import mysql.connector
import tkinter.messagebox 
import hashlib
from datetime import datetime, date


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

# TODO: Error handling of inputs
# TODO: Fix auto-increment
# TODO: check that a case already doesnt have an assignment to it (case has a location already)


def hash_password(password):
    """ The function takes in password and returns a hexidecimal hashed number"""
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

def add_years(input_date):
    """ Takes in YYYY-MM-DD string and converts to datetime object then outputs formatted string YYY-MM-DD with added 7 years"""
    years = 7
    start_date = datetime.strptime(input_date, '%Y-%m-%d')
    try:
        var = start_date.replace(year=start_date.year + years)
        final_date = f'{var:%Y-%m-%d}'
        return final_date
    except ValueError:
        # preserve calendar day (if Feb 29th doesn't exist, set to 28th)
        var = start_date.replace(year=start_date.year + years, day=28)
        final_date = f'{var:%Y-%m-%d}'
        return final_date
        
        
def add_to_employee_roles(roleDescription) -> None:
    """Inserts a role description and roleId into employee_roles database"""
       
    if roleDescription == "" or len(roleDescription)>49:
        print("Redo")
    else:         
        # sqlFormula = Anti-SQL Injection           
        sqlFormula = "INSERT INTO employee_roles (roleId, roleDescription) VALUE (%s, %s)" # %s = placeholders - replace with anything
        
        # Auto Increment done manually cause it doesnt work :(
        # Grab last added roleId and add 1
        mycursor.execute("SELECT roleId FROM employee_roles ORDER BY roleId DESC LIMIT 1") 
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            id = 0
        else:    
            for x in myresult:
                id = x[0]+1
                
        # Insert into Db     
        details = (id, roleDescription)
        mycursor.execute(sqlFormula, details)      
        mydb.commit()
        
        tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
        
        
def add_to_employee_account(age, firstname, lastname, gender, dateOfBirth, roleId) -> None:
    """Inserts details of employee into employee_account database"""
    
    sqlFormula = "INSERT INTO employee_account (employeeId, age, firstname, lastname, gender, dateOfBirth, roleId) VALUE (%s, %s, %s, %s, %s, %s, %s)"
    
    # Manual auto-increment
    mycursor.execute("SELECT employeeId FROM employee_account ORDER BY employeeId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        employeeId = 0
    else:    
        for x in myresult:
            employeeId = x[0]+1
     
    # Insert into Db     
    details = (employeeId, age, firstname, lastname, gender, dateOfBirth, roleId)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()
    
    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
    
def add_to_user_login_data(employeeId, username, password) -> None:
    """Inserts login details into user_login_data database"""
    sqlFormula = "INSERT INTO user_login_data (employeeId, username, passwordHash) VALUE (%s, %s, %s)"
    
    # Take in password and generate Hash
    passwordHash = hash_password(password)
     
    # Insert into Db     
    details = (employeeId, username, passwordHash)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
def add_to_client_information(firstName, lastName, gender, dateOfBirth) -> None:
    """Inserts login details into client_information database"""
    sqlFormula = "INSERT INTO client_information (clientId, firstName, lastName, gender, dateOfBirth) VALUE (%s, %s, %s, %s, %s)"
    
    # Manual auto-increment
    mycursor.execute("SELECT clientId FROM client_information ORDER BY clientId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        clientId = 0
    else:    
        for x in myresult:
            clientId = x[0]+1
            
    # Insert into Db     
    details = (clientId, firstName, lastName, gender, dateOfBirth)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")


def add_to_case_data(clientId, employeeId, description, department, dateOfCaseOpen, dateUploaded) -> None:
    """Inserts login details into case_data database"""
    sqlFormula = "INSERT INTO case_data (caseId, clientId, employeeId, description, department, dateOfCaseOpen, dateUploaded) VALUE (%s, %s, %s, %s, %s, %s, %s)"
    
    # Manual auto-increment
    mycursor.execute("SELECT caseId FROM case_data ORDER BY caseId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        caseId = 0
    else:    
        for x in myresult:
            caseId = x[0]+1
            
    # Insert into Db     
    details = (caseId, clientId, employeeId, description, department, dateOfCaseOpen, dateUploaded)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")


def add_to_archived_state(caseId, archivedState, archivedDate) -> None:
    """Inserts login details into archived_state database"""
    sqlFormula = "INSERT INTO archived_state (caseId, archivedState, archiveNumber, archivedDate, archivedDate) VALUE (%s, %s, %s, %s, %s)"
     
    # Determine when the file should be destroyed (7 years)
    dateToBeDeestroyed = add_years(archivedDate)

    # Create Archive Number
    # TODO: Make this more creative IE: {departmentCode}0001
    mycursor.execute("SELECT archiveNumber FROM archived_state ORDER BY archiveNumber DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        archiveNumber = 0
    else:    
        for x in myresult:
            archiveNumber = x[0]+1
            
    # Insert into Db     
    details = (caseId, archivedState, archiveNumber, archivedDate, archivedDate)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
  
    
def add_to_case_location(caseId, location) -> None:
    """Inserts login details into case_location database"""
    sqlFormula = "INSERT INTO case_location (caseId, location) VALUE (%s, %s)"
                
    # Insert into Db     
    details = (caseId, location)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    

def add_to_destruction_state(caseId, destructionState) -> None:
    """Inserts login details into destruction_state database"""
    sqlFormula = "INSERT INTO destruction_state (caseId, destructionState) VALUE (%s, %s)"
                
    # Insert into Db     
    details = (caseId, destructionState)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    

def add_to_file_upload_data(fileName, caseId, receivedDate, dateUploaded) -> None:
    """Inserts login details into file_upload_data database"""
    sqlFormula = "INSERT INTO file_upload_data (fileId, fileName, caseId, receivedDate, dateUploaded) VALUE (%s, %s, %s, %s, %s)"
    
     # Manual auto-increment            
    mycursor.execute("SELECT fileId FROM file_upload_data ORDER BY fileId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        fileId = 0
    else:    
        for x in myresult:
            fileId = x[0]+1
    # Insert into Db     
    details = (fileId, fileName, caseId, receivedDate, dateUploaded)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")


def add_to_deletion_confirmation(caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed) -> None:
    """Inserts login details into deletion_confirmation database"""
    sqlFormula = "INSERT INTO deletion_confirmation (caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed) VALUE (%s, %s, %s, %s, %s)"
                
    # Insert into Db     
    details = (caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    


def add_to_deletion_logging(caseId, employeeId1, employeeId2, deletionDate, deletionConfirmed) -> None:
    """Inserts login details into deletion_logging database"""
    sqlFormula = "INSERT INTO deletion_logging (caseId, employeeId1, employeeId2, deletionDate, deletionConfirmed) VALUE (%s, %s, %s, %s, %s)"
                
    # Insert into Db     
    details = (caseId, employeeId1, employeeId2, deletionDate, deletionConfirmed)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")


def add_to_arcived_case_request(archiveNumber, employeeId, dateRequested) -> None:
    """Inserts login details into arcived_case_request database"""
    sqlFormula = "INSERT INTO arcived_case_request (archiveNumber, employeeId, dateRequested) VALUE (%s, %s, %s)"
                
    # Insert into Db     
    details = (archiveNumber, employeeId, dateRequested)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
    
def add_to_case_drawn_by(archiveNumber, employeeId, dateDrawnOut) -> None:
    """Inserts login details into case_drawn_by database"""
    sqlFormula = "INSERT INTO case_drawn_by (archiveNumber, employeeId, dateDrawnOut) VALUE (%s, %s, %s)"
                
    # Insert into Db     
    details = (archiveNumber, employeeId, dateDrawnOut)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
    
def add_to_case_drawn_history(archiveNumber, employeeId, dateDrawnOut, dateDrawnIn) -> None:
    """Inserts login details into case_drawn_history database"""
    sqlFormula = "INSERT INTO case_drawn_history (archiveNumber, employeeId, dateDrawnOut, dateDrawnIn) VALUE (%s, %s, %s, %s)"
                
    # Insert into Db     
    details = (archiveNumber, employeeId, dateDrawnOut, dateDrawnIn)
    mycursor.execute(sqlFormula, details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
"""
# TODO: Fix check_password()
def check_password() -> None:
    
    username = list('ryan')
    sqlFormula = "SELECT passwordHash FROM user_login_data WHERE username = (%s))"
    mycursor.execute(sqlFormula, username)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
check_password()

"""