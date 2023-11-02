import mysql.connector
from datetime import date


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
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM employee_roles")
    myresult = mycursor.fetchall()
    return myresult


def login_employee_roles(username):
    mydb.cmd_refresh(1)
    mycursor.execute(f"SELECT employeeId FROM user_login_data WHERE username = '{username}'")
    employeeId = sum(mycursor.fetchone()) # Convert tuple to int
    mycursor.execute(f"SELECT roleId FROM employee_account WHERE employeeId = '{employeeId}'")
    myresult = sum(mycursor.fetchone()) # Convert tuple to int
    return myresult


def login_employee_id(username):
    mydb.cmd_refresh(1)
    mycursor.execute(f"SELECT employeeId FROM user_login_data WHERE username = '{username}'")
    employeeId = sum(mycursor.fetchone()) # Convert tuple to int
    return employeeId


def all_managers():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM employee_account WHERE roleId = '2'")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_user_login_data():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM user_login_data")
    myresult = mycursor.fetchall()
    return myresult


def all_client_information():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM client_information")
    myresult = mycursor.fetchall()
    return myresult


def all_case_data():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT case_data.caseId, client_information.firstName, client_information.lastName, employee_account.firstName, employee_account.lastName, description, department, dateOfCaseOpen, dateUploaded FROM case_data LEFT JOIN employee_account ON case_data.employeeId=employee_account.employeeId LEFT JOIN client_information ON case_data.clientId=client_information.clientId")
    myresult = mycursor.fetchall()
    return myresult


def case_data_by_id(caseId):
    mydb.cmd_refresh(1)
    mycursor.execute(f"SELECT * FROM case_data LEFT JOIN employee_account ON case_data.employeeId=employee_account.employeeId LEFT JOIN client_information ON case_data.clientId=client_information.clientId WHERE caseId = '{caseId}'")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_state():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT archived_state.archiveNumber, archivedState, archivedDate, dateToBeDestroyed, case_location.location FROM archived_state LEFT JOIN case_location ON archived_state.archiveNumber=case_location.archiveNumber")
    myresult = mycursor.fetchall()
    return myresult


def case_location_by_id(archiveNumber):
    mydb.cmd_refresh(1)
    mycursor.execute(f"SELECT * FROM case_location WHERE archiveNumber = '{archiveNumber}'")
    myresult = mycursor.fetchone()
    return myresult
    
    
    
def all_case_location():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM case_location")
    myresult = mycursor.fetchall()
    return myresult


def all_destruction_state():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM destruction_state")
    myresult = mycursor.fetchall()
    return myresult


def all_file_upload_data():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM file_upload_data")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_confirmation():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT caseId, firstName, lastName FROM deletion_confirmation LEFT JOIN employee_account ON employee_account.employeeId=deletion_confirmation.employeeId1 WHERE deletion_confirmation.employee1Confirmed = 1 AND deletion_confirmation.employee2Confirmed = 0")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_logging():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM deletion_logging")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_case_request():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT archived_case_request.archiveNumber, firstName, lastName, archived_case_request.employeeId, dateRequested, Location FROM archived_case_request LEFT JOIN case_location ON archived_case_request.archiveNumber=case_location.archiveNumber LEFT JOIN employee_account ON archived_case_request.employeeId=employee_account.employeeId")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_by():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM case_drawn_by")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_history():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM case_drawn_history")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_cloud_files():
    mydb.cmd_refresh(1)
    mycursor.execute("SELECT fileName FROM file_upload_data")
    myresult = mycursor.fetchall()
    return myresult


def grab_username(employeeId):
    mydb.cmd_refresh(1)
    mycursor.execute(f"SELECT firstName FROM employee_account WHERE employeeId = '{employeeId}'")
    myresult = mycursor.fetchall()
    return myresult


def case_to_be_destroyed_this_month():
    mydb.cmd_refresh(1)
    current_year = date.today().year
    current_month = date.today().month
    # Grab all items that need to be destoyed
    mycursor.execute(f"SELECT archived_state.archiveNumber, archivedState, archivedDate, dateToBeDestroyed, Location FROM archived_state LEFT JOIN case_location ON archived_state.archiveNumber=case_location.archiveNumber WHERE (MONTH(dateToBeDestroyed) <= {current_month} AND YEAR(dateToBeDestroyed) = {current_year}) OR (YEAR(dateToBeDestroyed) < {current_year})")
    myresult = mycursor.fetchall()
    
    myresult2 = list()
    myresult3 = list()
    
    # Grab all cases that have already been destroyed
    for a,b,c,d,e in myresult:
        mycursor.execute(f"SELECT archiveNumber FROM destruction_state WHERE archiveNumber = {a} AND destructionState = 'Destroyed'")
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
    
