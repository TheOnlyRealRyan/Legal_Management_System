import mysql.connector
import tkinter.messagebox 

# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

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
        mycursor.execute(f"DELETE FROM case_data WHERE caseId = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
 
    
def remove_archived_state(id):
    try:     
        mycursor.execute(f"DELETE FROM archived_state WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)

    
def remove_case_location(id):
    try:     
        mycursor.execute(f"DELETE FROM case_location WHERE archiveNumber = '{id}';")    
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)


def remove_destruction_state(id):
    try:     
        mycursor.execute(f"DELETE FROM destruction_state WHERE archiveNumber = '{id}';")
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
        mycursor.execute(f"DELETE FROM deletion_confirmation WHERE caseId = '{id}';")
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


def remove_archived_case_request(archiveNumber, employeeId):
    try:     
        mycursor.execute(f"DELETE FROM archived_case_request WHERE archiveNumber = '{archiveNumber}' AND employeeId = '{employeeId}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
  
    
def remove_case_drawn_by(id):
    try:     
        mycursor.execute(f"DELETE FROM case_drawn_by WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
  
    
def remove_case_drawn_history(id):
    try:     
        mycursor.execute(f"DELETE FROM case_drawn_history WHERE archiveNumber = '{id}';")
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully deleted from database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to delete from database")
        print(e)
        
        