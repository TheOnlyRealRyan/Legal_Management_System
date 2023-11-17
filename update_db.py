import mysql.connector
import tkinter.messagebox 
from datetime import datetime
import global_variables as gv
import hashlib
from grab_from_db import caseId_from_caseCode

# Display messages upon successful or failed updation
messagebox_show = True


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


def update_deletion_confirmation_employee2(caseId, confirm):
    try:            
        employeeId2 = gv.get_id()
        mycursor.execute(f"UPDATE deletion_confirmation SET employee2Confirmed = '{confirm}', employeeId2 = '{employeeId2}' WHERE caseId = '{caseId}';")
        mydb.commit()
        
        sqlFormula = "INSERT INTO deletion_logging (caseId, employeeId, deletionDate, deletionConfirmed) VALUE (%s, %s, %s, %s)"
        details = (caseId, employeeId2, datetime.today().strftime('%Y-%m-%d %H:%M:%S'), confirm)
        mycursor.execute(sqlFormula, details)  
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)


def update_employee_role(id, roleDescription):
    try:     
        mycursor.execute(f"UPDATE employee_account SET roleDesciption = '{roleDescription}' WHERE roleId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)


def update_employee_account(id, firstName, lastName, gender, dateOfBirth, roleId):
    try:     
        mycursor.execute(f"UPDATE employee_account SET firstName = '{firstName}', lastName = '{lastName}', gender = '{gender}', dateOfBirth = '{dateOfBirth}', roleId = '{roleId}', WHERE employeeId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
    
 
    
def update_user_login_data(employeeId, username, password):
    try:     
        passwordHash = hash_password(password)
        mycursor.execute(f"UPDATE user_login_data SET firstName = '{username}', password = '{passwordHash}' WHERE employeeId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
    
   
    
def update_client_information(id):
    try:     
        mycursor.execute(f"UPDATE client_information WHERE clientId = '{id}';")   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
     


def update_case_data(id):
    try:     
        mycursor.execute(f"UPDATE case_data WHERE caseId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
        

def update_case_data_date_closed(caseCode):
    try:     
        caseId = caseId_from_caseCode(caseCode)[0][0]
        dateClosed = datetime.today().strftime('%Y-%m-%d')
        mycursor.execute(f"UPDATE case_data SET dateClosed = '{dateClosed}' WHERE caseId = '{caseId}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
 
    
def update_archived_state(id):
    try:     
        mycursor.execute(f"UPDATE archived_state WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)

    
def update_case_location(id):
    try:     
        mycursor.execute(f"UPDATE case_location WHERE archiveNumber = '{id}';")    
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)


def update_destruction_state(id):
    try:     
        mycursor.execute(f"UPDATE destruction_state WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
 
    
def update_file_upload_data(id):
    try:     
        mycursor.execute(f"UPDATE file_upload_data WHERE fileId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
    
    
def update_deletion_confirmation(id):
    try:     
        mycursor.execute(f"UPDATE deletion_confirmation WHERE caseId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)


def update_deletion_logging(id):
    try:     
        mycursor.execute(f"UPDATE deletion_logging WHERE caseId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)


def update_archived_case_request(archiveNumber, employeeId):
    try:     
        mycursor.execute(f"UPDATE archived_case_request WHERE archiveNumber = '{archiveNumber}' AND employeeId = '{employeeId}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
  
    
def update_case_drawn_by(id):
    try:     
        mycursor.execute(f"UPDATE case_drawn_by WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
  
    
def update_case_drawn_history(id):
    try:     
        mycursor.execute(f"UPDATE case_drawn_history WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully updated database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to update database")
        print(e)
        
    
    
