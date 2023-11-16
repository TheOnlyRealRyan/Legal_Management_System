import mysql.connector
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



def remove_employee_role(id):
    mycursor.execute(f"DELETE FROM employee_account WHERE employeeId = '{id}';")
    mydb.commit()

def remove_employee_account(id):
    mycursor.execute(f"DELETE FROM employee_account WHERE employeeId = '{id}';")
    mydb.commit()
    
def remove_user_login_data(id):
    mycursor.execute(f"DELETE FROM user_login_data WHERE roleId = '{id}';")
    mydb.commit()
    
def remove_client_information(id):
    mycursor.execute(f"DELETE FROM client_information WHERE clientId = '{id}';")    
    mydb.commit()

def remove_case_data(id):
    mycursor.execute(f"DELETE FROM case_data WHERE caseId = '{id}';")
    mydb.commit()
    
def remove_archived_state(id):
    mycursor.execute(f"DELETE FROM archived_state WHERE archiveNumber = '{id}';")
    mydb.commit()
    
def remove_case_location(id):
    mycursor.execute(f"DELETE FROM case_location WHERE archiveNumber = '{id}';")    
    mydb.commit()

def remove_destruction_state(id):
    mycursor.execute(f"DELETE FROM destruction_state WHERE caseId = '{id}';")
    mydb.commit()
    
def remove_file_upload_data(id):
    mycursor.execute(f"DELETE FROM file_upload_data WHERE fileId = '{id}';")
    mydb.commit()
    
def remove_deletion_confirmation(id):
    mycursor.execute(f"DELETE FROM deletion_confirmation WHERE caseId = '{id}';")
    mydb.commit()

def remove_deletion_logging(id):
    # TODO: complete deletion logging
    mycursor.execute(f"DELETE FROM deletion_logging WHERE employeeId = '{id}';")
    mydb.commit()

def remove_archived_case_request(archiveNumber, employeeId):
    mycursor.execute(f"DELETE FROM archived_case_request WHERE archiveNumber = '{archiveNumber}' AND employeeId = '{employeeId}';")
    mydb.commit()
def remove_case_drawn_by(id):
    mycursor.execute(f"DELETE FROM case_drawn_by WHERE caseId = '{id}';")
    mydb.commit()
    
def remove_case_drawn_history(id):
    mycursor.execute(f"DELETE FROM case_drawn_history WHERE caseId = '{id}';")
    mydb.commit()