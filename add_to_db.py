import mysql.connector
import tkinter.messagebox 
import hashlib
from datetime import datetime
import grab_from_db as grab
import global_variables as gv


# Display messages upon successful or failed insertion
messagebox_show = False


# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)


# Initialise cursor:
mycursor = mydb.cursor()


def hash_password(password):
    """ The function takes in password and returns a hexidecimal hashed number"""
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()


def add_years(input_date):
    """ Takes in YYYY-MM-DD string and converts to datetime object then outputs formatted string YYY-MM-DD with added 7 years"""
    mydb.cmd_refresh(1)
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
    mydb.cmd_refresh(1)
    if roleDescription == "" or len(roleDescription)>49:
        print("Redo")
    else:  
        """        
        # Without Auto-Increment:
        sqlFormula = "INSERT INTO employee_roles (roleDescription) VALUE (%s)" # %s = placeholders - replace with anything
        # Insert into Db     
        try: 
            details = list(roleDescription)
            mycursor.execute(sqlFormula, details)      
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
        except Exception as e:
            if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
            print(e)
        """
        # sqlFormula = Anti-SQL Injection           
        sqlFormula = "INSERT INTO employee_roles (roleId, roleDescription) VALUE (%s, %s)" # %s = placeholders - replace with anything
        
        # Auto Increment done manually cause it doesnt work
        # Grab last added roleId and add 1
        
        mycursor.execute("SELECT roleId FROM employee_roles ORDER BY roleId DESC LIMIT 1") 
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            id = 0
        else:    
            for x in myresult:
                id = x[0]+1
               
        # Insert into Db     
        try: 
            details = (id, roleDescription)
            mycursor.execute(sqlFormula, details)      
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
        except Exception as e:
            if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
            print(e)
        
        
def add_to_employee_account(firstname, lastname, gender, dateOfBirth, roleId) -> None:
    """Inserts details of employee into employee_account database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO employee_account (firstname, lastname, gender, dateOfBirth, roleId) VALUE (%s, %s, %s, %s, %s)"
    
    # Insert into Db     
    try:
        details = (firstname, lastname, gender, dateOfBirth, roleId)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    
    
def add_to_user_login_data(employeeId, username, password) -> None:
    """Inserts login details into user_login_data database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO user_login_data (employeeId, username, passwordHash) VALUE (%s, %s, %s)"
    
    # Take in password and generate Hash
    passwordHash = hash_password(password)
     
    # Insert into Db  
    try:   
        details = (employeeId, username, passwordHash)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    
def add_to_client_information(firstName, lastName, gender, dateOfBirth) -> None:
    """Inserts login details into client_information database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO client_information (firstName, lastName, gender, dateOfBirth) VALUE (%s, %s, %s, %s)"
    """
    # Manual auto-increment
    mycursor.execute("SELECT clientId FROM client_information ORDER BY clientId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        clientId = 0
    else:    
        for x in myresult:
            clientId = x[0]+1
     """       
    # Insert into Db     
    try: 
        details = (firstName, lastName, gender, dateOfBirth)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e)    
    

def add_to_case_data(caseCode, clientId, employeeId, description, department, dateOfCaseOpen) -> None:
    """Inserts login details into case_data database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO case_data (caseId, caseCode, clientId, employeeId, description, department, dateOfCaseOpen) VALUE (%s, %s, %s, %s, %s, %s, %s)"
    
    # Manual auto-increment
    mycursor.execute("SELECT caseId FROM case_data ORDER BY caseId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        caseId = 0
    else:    
        for x in myresult:
            caseId = x[0]+1
            
    # Insert into Db    
    try:  
        details = (caseId, caseCode, clientId, employeeId, description, department, dateOfCaseOpen)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e)  


def add_to_archived_state(caseId, archivedState, archiveCode, archivedDate) -> None:
    """Inserts login details into archived_state database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO archived_state (caseId, archivedState, archiveCode, archivedDate, dateToBeDestroyed) VALUE (%s, %s, %s, %s, %s)"
     
    # Determine when the file should be destroyed (7 years)
    dateToBeDeestroyed = add_years(archivedDate)

            
    # Insert into Db 
    try:    
        details = (caseId, archivedState, archiveCode, archivedDate, dateToBeDeestroyed)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e)  
  
    
def add_to_case_location(archiveCode, location) -> None:
    """Inserts into case_location database"""
    
    mydb.cmd_refresh(1)
    find = grab.case_location_by_id(archiveCode)
    print(find)
    
    if find != None:
        sqlFormula = f"UPDATE case_location SET location = '{location}' WHERE archiveCode = '{archiveCode}'"  
        # Insert into Db  
        try: 
            mycursor.execute(sqlFormula)       
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated Database")
        except Exception as e:
            if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update Database")
            print(e)
    else:
        # Insert into Db  
        try:   
            sqlFormula = "INSERT INTO case_location (archiveCode, location) VALUE (%s, %s)"
            details = (archiveCode, location)
            mycursor.execute(sqlFormula, details)   
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
        except Exception as e:
            if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
            print(e) 

    # Insert into Db  
    try:   
        sqlFormula = "INSERT INTO case_location (archiveCode, location) VALUE (%s, %s)"
        details = (archiveCode, location)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 

def add_to_destruction_state(archiveCode, destructionState) -> None:
    """Inserts login details into destruction_state database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO destruction_state (archiveCode, destructionState) VALUE (%s, %s)"
                
    # Insert into Db     
    try:
        details = (archiveCode, destructionState)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    

def add_to_file_upload_data(fileName, caseId, recievedDate) -> None:
    """Inserts file_upload_data database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO file_upload_data (fileId, fileName, caseId, recievedDate, dateUploaded) VALUE (%s, %s, %s, %s, %s)"
    
     # Manual auto-increment            
    mycursor.execute("SELECT fileId FROM file_upload_data ORDER BY fileId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        fileId = 0
    else:    
        for x in myresult:
            fileId = x[0]+1
    # Insert into Db     
    try:
        details = (fileId, fileName, caseId, recievedDate, datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 


def add_to_deletion_confirmation(caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed) -> None:
    """Inserts login details into deletion_confirmation database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO deletion_confirmation (caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed) VALUE (%s, %s, %s, %s, %s)"
                
    # Insert into Db
    try:     
        details = (caseId, employeeId1, employeeId2, employee1Confirmed, employee2Confirmed)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    

def add_to_deletion_logging(caseId, employeeId1, employeeId2, deletionDate) -> None:
    """Inserts login details into deletion_logging database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO deletion_logging (caseId, employeeId1, employeeId2, deletionDate, deletionConfirmed) VALUE (%s, %s, %s, %s, %s)"
                
    # Insert into Db
    try:     
        details = (caseId, employeeId1, employeeId2, deletionDate, 1)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 


def add_to_archived_case_request(archiveCode) -> None:
    """Inserts login details into archived_case_request database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO archived_case_request (archiveCode, employeeId, dateRequested) VALUE (%s, %s, %s)" 
               
    # Insert into Db
    try:     
        details = (archiveCode, gv.get_id(), datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    
    
def add_to_case_drawn_by(archiveCode, employeeId, dateDrawnOut) -> None:
    """Inserts login details into case_drawn_by database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO case_drawn_by (archiveCode, employeeId, dateDrawnOut) VALUE (%s, %s, %s)"
                
    # Insert into Db
    try:     
        details = (archiveCode, employeeId, dateDrawnOut)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
    
    
def add_to_case_drawn_history(archiveCode, employeeId, dateDrawnOut, dateDrawnIn) -> None:
    """Inserts login details into case_drawn_history database"""
    mydb.cmd_refresh(1)
    sqlFormula = "INSERT INTO case_drawn_history (archiveCode, employeeId, dateDrawnOut, dateDrawnIn) VALUE (%s, %s, %s, %s)"
                
    # Insert into Db
    try:     
        details = (archiveCode, employeeId, dateDrawnOut, dateDrawnIn)
        mycursor.execute(sqlFormula, details)   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to insert into Database")
        print(e) 
        



