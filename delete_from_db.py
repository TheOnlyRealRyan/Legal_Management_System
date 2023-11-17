import mysql.connector
import tkinter.messagebox 
from add_to_db import add_to_deletion_logging
from grab_from_db import deletion_confirmation_by_id, caseId_from_caseCode
from datetime import datetime

# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)


# Initialise cursor:
mycursor = mydb.cursor()

# Display messages upon successful or failed deletion
messagebox_show = True


def remove_employee_role(id):
    try:     
        mycursor.execute(f"DELETE FROM employee_account WHERE roleId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)


def remove_employee_account(id):
    try:     
        mycursor.execute(f"DELETE FROM employee_account WHERE employeeId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
    
 
    
def remove_user_login_data(id):
    try:     
        mycursor.execute(f"DELETE FROM user_login_data WHERE employeeId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
    
   
    
def remove_client_information(id):
    try:     
        mycursor.execute(f"DELETE FROM client_information WHERE clientId = '{id}';")   
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
     


def remove_case_data(id):
    try:     
        
        info = deletion_confirmation_by_id(id)
        caseId = caseId_from_caseCode(id)[0][0]
        add_to_deletion_logging(caseId, info[0][0],  info[0][1], datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        
        mycursor.execute(f"DELETE FROM case_data WHERE caseId = '{caseId}';")
        mydb.commit()
        
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
 
    
def remove_archived_state(id):
    try:     
        mycursor.execute(f"DELETE FROM archived_state WHERE archiveCode = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)

    
def remove_case_location(id):
    try:     
        mycursor.execute(f"DELETE FROM case_location WHERE archiveCode = '{id}';")    
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)


def remove_destruction_state(id):
    try:     
        mycursor.execute(f"DELETE FROM destruction_state WHERE archiveCode = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
 
    
def remove_file_upload_data(id):
    try:     
        mycursor.execute(f"DELETE FROM file_upload_data WHERE fileId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
    
    
def remove_deletion_confirmation(id):
    try:     
        caseId = caseId_from_caseCode(id)[0][0]
        mycursor.execute(f"DELETE FROM deletion_confirmation WHERE caseId = '{caseId}';")
        info = deletion_confirmation_by_id(id)  
        print(caseId)
        print(info)  
        add_to_deletion_logging(caseId, info[0][0],  info[0][1], datetime.today().strftime('%Y-%m-%d %H:%M:%S'))   
        try:     
            mycursor.execute(f"DELETE FROM case_data WHERE caseId = '{caseId}';")
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
        except:
            print("--> Deleting archive first")
            mycursor.execute(f"DELETE FROM archive_state WHERE caseId = '{caseId}';")
            mycursor.execute(f"DELETE FROM case_data WHERE caseId = '{caseId}';")
            mydb.commit()
            if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")        
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)


def remove_deletion_logging(id):
    try:     
        mycursor.execute(f"DELETE FROM deletion_logging WHERE caseId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)


def remove_archived_case_request(archiveCode, employeeId):
    try:     
        mycursor.execute(f"DELETE FROM archived_case_request WHERE archiveCode = '{archiveCode}' AND employeeId = '{employeeId}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
  
    
def remove_case_drawn_by(id):
    try:     
        mycursor.execute(f"DELETE FROM case_drawn_by WHERE archiveCode = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
  
    
def remove_case_drawn_history(id):
    try:     
        mycursor.execute(f"DELETE FROM case_drawn_history WHERE archiveCode = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
        
        