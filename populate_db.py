import add_to_db as add
import time





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

# Archived State    
for i in range(10):
    caseId = i
    archivedState = "Archived"
    archivedDate = "2001-06-06"
    add.add_to_archived_state(caseId, archivedState, archivedDate)
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
for i in range(5):
    id= i+1
    archivedState = "Archived"

    dateOfBirth = f"200{i}-06-06"
    roleId = 1
    add.add_to_archived_state(id, archivedState, dateOfBirth)
    print("success")
    time.sleep(wait_time)  
    
id= 8
archivedState = "Archived"
dateOfBirth = "2016-11-06"
add.add_to_archived_state(id, archivedState, dateOfBirth)
print("success")
time.sleep(wait_time)

id= 9
archivedState = "Archived"
dateOfBirth = "2016-09-06"
add.add_to_archived_state(id, archivedState, dateOfBirth)
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
employeeId = 1
add.add_to_archived_case_request(archiveNumber, employeeId)
print("success")
time.sleep(wait_time)