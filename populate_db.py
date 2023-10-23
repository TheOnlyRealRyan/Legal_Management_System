import add_to_db as add
import time
import global_variables


wait_time = 0
# Just a bunch of dummy data for testing

# Client Information
for i in range(50):
    name = f"ryan{i}"
    surname = "Putzier"
    gender = "M"
    dob = "2001-06-06"
    add.add_to_client_information(name, surname, gender, dob)
    print("success")
    time.sleep(wait_time)
    
# Employee Roles  

for i in range(10):
    roleDescription= "Role number {i}"
    add.add_to_employee_roles(roleDescription)
    print("success")
    time.sleep(wait_time) 
    
# Employee Account
firstname= "admin"
lastname = "admin"
gender = "M"
dateOfBirth = "2001-06-06"
roleId = 1
add.add_to_employee_account(firstname, lastname, gender, dateOfBirth, roleId)
print("success")
time.sleep(wait_time)  

firstname= "Ryan"
lastname = "Putzier"
gender = "M"
dateOfBirth = "1999-06-06"
roleId = 2
add.add_to_employee_account( firstname, lastname, gender, dateOfBirth, roleId)
print("success")
time.sleep(wait_time)  

for i in range(5):
    firstname= f"Ryan {i}"
    lastname = "Putzier"
    gender = "M"
    dateOfBirth = "1999-06-06"
    roleId = 3
    add.add_to_employee_account( firstname, lastname, gender, dateOfBirth, roleId)
    print("success")
    time.sleep(wait_time)  
    
for i in range(5):
    firstname= f"Ryan {i}"
    lastname = "Putzier"
    gender = "M"
    dateOfBirth = "1999-06-06"
    roleId = 4
    add.add_to_employee_account( firstname, lastname, gender, dateOfBirth, roleId)
    print("success")
    time.sleep(wait_time) 

# Case Data
for i in range(10):
    clientId = 1
    employeeId = 1
    description = "awesome"
    department = "Tax"
    dateOfCaseOpen = "2020-06-06"
    dateUploaded = "2022-06-06"
    add.add_to_case_data(clientId, employeeId, description, department, dateOfCaseOpen, dateUploaded)
    print("success")
    time.sleep(wait_time) 

# File Upload Data    
for i in range(10):
    fileName = f"File Name {i}"
    caseId = 1
    recievedDate = "2001-06-06"

    add.add_to_file_upload_data(fileName, caseId, recievedDate)
    print("success")
    time.sleep(wait_time)    

 
 
# login data


id= 1
username = "admin"
password = "admin"
add.add_to_user_login_data(id, username, password)
print("success")
time.sleep(wait_time)

id= 2
username = "manager"
password = "manager"
add.add_to_user_login_data(id, username, password)
print("success")
time.sleep(wait_time)

id= 3
username = "archive"
password = "archive"
add.add_to_user_login_data(id, username, password)
print("success")
time.sleep(wait_time)

id= 4
username = "attorney"
password = "attorney"
add.add_to_user_login_data(id, username, password)
print("success")
time.sleep(wait_time)

# Destruction State
id= 1
state = "Destroyed"
add.add_to_destruction_state(id, state)
print("success")
time.sleep(wait_time)

# Archive State

# Archived State    
for i in range(5):
    caseId = i
    archivedState = "Archived"
    archivedDate = "2001-06-06"
    add.add_to_archived_state(caseId, archivedState, archivedDate)
    print("success")
    time.sleep(wait_time)   

for i in range(6,10):
    id= i
    archivedState = "Archived"

    archivedDate = f"200{i}-06-06"
    roleId = 1
    add.add_to_archived_state(id, archivedState, archivedDate)
    print("success")
    time.sleep(wait_time)  
    
id= 11
archivedState = "Archived"
archivedDate = "2016-11-06"
add.add_to_archived_state(id, archivedState, archivedDate)
print("success")
time.sleep(wait_time)

id= 12
archivedState = "Archived"
archivedDate = "2016-09-06"
add.add_to_archived_state(id, archivedState, archivedDate)
print("success")
time.sleep(wait_time)


# Case Location
archiveNumner = 0
location = "Cupboard 12"
add.add_to_case_location(archiveNumner, location)
print("success")
time.sleep(wait_time)


# Archive Case Request
# for i in range(10):
archiveNumber = 0
add.add_to_archived_case_request(archiveNumber)
print("success")
time.sleep(wait_time)

archiveNumber = 1
add.add_to_archived_case_request(archiveNumber)
print("success")
time.sleep(wait_time)

# Deletion Request
for i in range(5):
    add.add_to_deletion_confirmation(i, 1, 1, True, False)