import mysql.connector
import tkinter.messagebox 
import hashlib
from datetime import datetime, date


# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

def all_employee_roles():
    mycursor.execute("SELECT * FROM employee_roles")
    myresult = mycursor.fetchall()
    return myresult


def login_employee_roles(username):
    mycursor.execute(f"SELECT employeeId FROM user_login_data WHERE username = '{username}'")
    employeeId = sum(mycursor.fetchone()) # Convert tuple to int
    mycursor.execute(f"SELECT roleId FROM employee_account WHERE employeeId = '{employeeId}'")
    myresult = sum(mycursor.fetchone()) # Convert tuple to int
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_user_login_data():
    mycursor.execute("SELECT * FROM user_login_data")
    myresult = mycursor.fetchall()
    return myresult


def all_client_information():
    mycursor.execute("SELECT * FROM client_information")
    myresult = mycursor.fetchall()
    return myresult


def all_case_data():
    mycursor.execute("SELECT * FROM case_data LEFT JOIN employee_account ON case_data.employeeId=employee_account.employeeId LEFT JOIN client_information ON case_data.clientId=client_information.clientId")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_state():
    mycursor.execute("SELECT * FROM archived_state LEFT JOIN case_location ON archived_state.archiveNumber=case_location.caseId")
    myresult = mycursor.fetchall()
    return myresult


def all_case_location():
    mycursor.execute("SELECT * FROM case_location")
    myresult = mycursor.fetchall()
    return myresult


def all_destruction_state():
    mycursor.execute("SELECT * FROM destruction_state")
    myresult = mycursor.fetchall()
    return myresult


def all_file_upload_data():
    mycursor.execute("SELECT * FROM file_upload_data")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_confirmation():
    mycursor.execute("SELECT * FROM deletion_confirmation")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_logging():
    mycursor.execute("SELECT * FROM deletion_logging")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_case_request():
    mycursor.execute("SELECT * FROM archived_case_request LEFT JOIN case_location ON archived_case_request.archiveNumber=case_location.caseId LEFT JOIN employee_account ON archived_case_request.employeeId=employee_account.employeeId")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_by():
    mycursor.execute("SELECT * FROM case_drawn_by")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_history():
    mycursor.execute("SELECT * FROM case_drawn_history")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def case_to_be_destroyed_this_month():
    # TODO: check that case is already not destroyed
    current_year = date.today().year
    current_month = date.today().month
    # Grab all items that need to be destoyed
    mycursor.execute(f"SELECT * FROM archived_state WHERE (MONTH(dateToBeDestroyed) <= {current_month} AND YEAR(dateToBeDestroyed) = {current_year}) OR (YEAR(dateToBeDestroyed) < {current_year})")
    myresult = mycursor.fetchall()
    
    myresult2 = list()
    myresult3 = list()
    
    # Grab all cases that have already been destroyed
    for a,b,c,d,e in myresult:
        mycursor.execute(f"SELECT caseId FROM destruction_state WHERE caseId = {a} AND destructionState = 'Destroyed'")
        myresult2.append(mycursor.fetchone())
        
    # convert (1,) to 1 if not None from already Destroyed list
    for a in myresult2:
        if a != None:       
            myresult3.append(sum(a)) 
            
    # If a case has already been destroyed, then remove that case from the to be destroyed list
    for a in myresult3:
        for b,c,d,e,f in myresult:           
            if (b == a):
                final_list = [x for x in myresult if x[0] != a]   
                break
   
    # If list is empty        
    if len(final_list) > 0:      
        return final_list
    else:
        print("Doesnt exist")
        pass
    
