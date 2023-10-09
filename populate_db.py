import add_to_db as add
import time
"""
for i in range(50):
    name = f"ryan{i}"
    surname = "Putzier"
    gender = "M"
    dob = "2001-06-06"
    add.add_to_client_information(name, surname, gender, dob)
    print("success")
    time.sleep(0.2)
"""  
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
    dateUploaded = "2020-06-06"
    add.add_to_file_upload_data(fileName, caseId, recievedDate, dateUploaded)
    print("success")
    time.sleep(0.1)    