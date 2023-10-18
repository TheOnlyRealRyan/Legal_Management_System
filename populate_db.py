import add_to_db as add
import time

id= 1
state = "Destroyed"
add.add_to_destruction_state(id, state)
print("success")
time.sleep(0.1)

"""
for i in range(5):
    id= i+1
    archivedState = "Archived"

    dateOfBirth = f"200{i}-06-06"
    roleId = 1
    add.add_to_archived_state(id, archivedState, dateOfBirth)
    print("success")
    time.sleep(0.1)  
    
id= 8
archivedState = "Archived"
dateOfBirth = "2016-11-06"
add.add_to_archived_state(id, archivedState, dateOfBirth)
print("success")
time.sleep(0.1)

id= 9
archivedState = "Archived"
dateOfBirth = "2016-09-06"
add.add_to_archived_state(id, archivedState, dateOfBirth)
print("success")
time.sleep(0.1)

archiveNumner = 0
location = "Cupboard 12"
add.add_to_case_location(archiveNumner, location)
print("success")
time.sleep(0.1)


# for i in range(10):
archiveNumber = 0
employeeId = 1
add.add_to_archived_case_request(archiveNumber, employeeId)
print("success")
time.sleep(0.1)


for i in range(50):
    name = f"ryan{i}"
    surname = "Putzier"
    gender = "M"
    dob = "2001-06-06"
    add.add_to_client_information(name, surname, gender, dob)
    print("success")
    time.sleep(0.2)
    
    
for i in range(10):
    roleDescription= "New{i}"
    add.add_to_employee_roles(roleDescription)
    print("success")
    time.sleep(0.1) 
    

for i in range(10):
    firstname= f"Ryan {i}"
    lastname = "Putzier"
    gender = "M"
    age = i
    dateOfBirth = "2022-06-06"
    roleId = 1
    add.add_to_employee_account(age, firstname, lastname, gender, dateOfBirth, roleId)
    print("success")
    time.sleep(0.1)  
 

for i in range(10):
    clientId = 1
    employeeId = 1
    description = "awesome"
    department = "Tax"
    dateOfCaseOpen = "2020-06-06"
    dateUploaded = "2022-06-06"
    add.add_to_case_data(clientId, employeeId, description, department, dateOfCaseOpen, dateUploaded)
    print("success")
    time.sleep(0.1) 

    
for i in range(10):
    fileName = f"File Name {i}"
    caseId = 1
    recievedDate = "2001-06-06"

    add.add_to_file_upload_data(fileName, caseId, recievedDate)
    print("success")
    time.sleep(0.1)    

    
for i in range(10):
    caseId = i
    archivedState = "Archived"
    archivedDate = "2001-06-06"
    add.add_to_archived_state(caseId, archivedState, archivedDate)
    print("success")
    time.sleep(0.1)    
    
"""