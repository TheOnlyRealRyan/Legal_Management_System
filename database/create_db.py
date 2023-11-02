import mysql.connector
import database.add_to_db as add
import time


def connect_to_database():
    # Connect to Database
    print("--> Trying to Connect to Database")
    try:   
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "mysql",
            database="projectdb"
        )
        
        print("--> Successfully Connected to projectdb")
        
        return mydb
    except Exception as e:
        print(e)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "mysql",
        )
        
        print("--> Successfully Connected to MySQL")
        
        try:            
            mycursor = mydb.cursor()
            # Create Database
            mycursor.execute("CREATE DATABASE projectdb")
            print("--> Successfully Created projectdb")            
        except Exception as e:
            print(e)
        
        return mydb


def create_database():
    mydb = connect_to_database()
    # Initialise cursor
    mycursor = mydb.cursor()

    try:
        # DELETE tables
        print("--> Trying to Drop Existing Tables")
        mycursor.execute("DROP TABLE IF EXISTS archived_case_request")
        mycursor.execute("DROP TABLE IF EXISTS file_upload_data")
        mycursor.execute("DROP TABLE IF EXISTS case_drawn_history")
        mycursor.execute("DROP TABLE IF EXISTS case_drawn_by")
        mycursor.execute("DROP TABLE IF EXISTS case_location")
        mycursor.execute("DROP TABLE IF EXISTS destruction_state")
        mycursor.execute("DROP TABLE IF EXISTS deletion_confirmation")
        mycursor.execute("DROP TABLE IF EXISTS deletion_logging")
        mycursor.execute("DROP TABLE IF EXISTS archived_state")
        mycursor.execute("DROP TABLE IF EXISTS case_data")
        mycursor.execute("DROP TABLE IF EXISTS client_information")
        mycursor.execute("DROP TABLE IF EXISTS user_login_data")
        mycursor.execute("DROP TABLE IF EXISTS employee_account")
        mycursor.execute("DROP TABLE IF EXISTS employee_roles")
        print("--> Successfuly Dropped Tables")
    except Exception as e:
        print(e)
    
    
    try:
        print("--> Trying to Create Tables")
        # Create Tables
        mycursor.execute("CREATE TABLE employee_roles(roleId INTEGER(10) NOT NULL AUTO_INCREMENT, roleDescription VARCHAR(20), PRIMARY KEY (roleId))")
        mycursor.execute("CREATE TABLE employee_account(employeeId INTEGER(10) NOT NULL AUTO_INCREMENT, firstName VARCHAR(50),  lastName VARCHAR(50), gender VARCHAR(2),  dateOfBirth DATE, roleId INTEGER(10), PRIMARY KEY (employeeId), FOREIGN KEY (roleId) REFERENCES employee_roles(roleId))")
        mycursor.execute("CREATE TABLE user_login_data(employeeId INTEGER, username VARCHAR(50), passwordHash VARCHAR(250), PRIMARY KEY (employeeId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
        mycursor.execute("CREATE TABLE client_information(clientId INTEGER(10) NOT NULL AUTO_INCREMENT, firstName VARCHAR(50), lastName VARCHAR(50), gender VARCHAR(1), dateOfBirth DATE, PRIMARY KEY (clientId))")
        mycursor.execute("CREATE TABLE case_data(caseId INTEGER(10), clientId INTEGER(10), employeeId INTEGER(10), description VARCHAR(250), department VARCHAR(30), dateOfCaseOpen DATE, dateUploaded DATE, PRIMARY KEY (caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId), FOREIGN KEY (clientId) REFERENCES client_information(clientId))")
        mycursor.execute("CREATE TABLE archived_state(caseId INTEGER(10), archivedState VARCHAR(10), archiveNumber INTEGER(10), archivedDate DATE, dateToBeDestroyed DATE, UNIQUE (caseId), PRIMARY KEY (archiveNumber), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
        mycursor.execute("CREATE TABLE deletion_logging(caseId INTEGER(10), employeeId INTEGER, deletionDate DATE, deletionConfirmed BOOLEAN, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
        mycursor.execute("CREATE TABLE deletion_confirmation(caseId INTEGER(10), employeeId1 INTEGER, employeeId2 INTEGER, employee1Confirmed BOOLEAN, employee2Confirmed BOOLEAN, PRIMARY KEY (caseId), FOREIGN KEY (employeeId1) REFERENCES employee_account(employeeId),  FOREIGN KEY (employeeId2) REFERENCES employee_account(employeeId))")
        mycursor.execute("CREATE TABLE destruction_state(archiveNumber INTEGER(10), destructionState VARCHAR(50), PRIMARY KEY (archiveNumber), FOREIGN KEY (archiveNumber) REFERENCES archived_state(archiveNumber))")
        mycursor.execute("CREATE TABLE case_location(archiveNumber INTEGER(10), location VARCHAR(50), PRIMARY KEY (archiveNumber), FOREIGN KEY (archiveNumber) REFERENCES archived_state(archiveNumber))")
        mycursor.execute("CREATE TABLE case_drawn_by(archiveNumber INTEGER(10), employeeId INTEGER, dateDrawnOut DATE, PRIMARY KEY (archiveNumber), FOREIGN KEY (archiveNumber) REFERENCES archived_state(archiveNumber), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
        mycursor.execute("CREATE TABLE case_drawn_history(archiveNumber INTEGER(10), employeeId INTEGER(10), dateDrawnOut DATE, dateDrawnIn DATE, PRIMARY KEY (archiveNumber), FOREIGN KEY (archiveNumber) REFERENCES archived_state(archiveNumber), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
        mycursor.execute("CREATE TABLE file_upload_data(fileId INTEGER(10), fileName VARCHAR(100), caseId INTEGER(10), recievedDate DATE, dateUploaded DATETIME, PRIMARY KEY (fileId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
        mycursor.execute("CREATE TABLE archived_case_request(archiveNumber INTEGER(10), employeeId INTEGER(10), dateRequested DATETIME, PRIMARY KEY (archiveNumber, employeeId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId), FOREIGN KEY (archiveNumber) REFERENCES archived_state(archiveNumber))")
        print("--> Successfuly Created Tables")
    except Exception as e:
        print(e)    


    # Display Tables  
    mycursor.execute("SHOW TABLES")
    for tb in mycursor:
        print(tb)
    
        
def populate_database():
    print("--> Trying to Populate Database")
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

    # Archived State    
    for i in range(5):
        caseId = i
        archivedState = "Archived"
        archivedDate = "2001-06-06"
        add.add_to_archived_state(caseId, archivedState, archivedDate)
        print("success")
        time.sleep(wait_time)   

    for i in range(5,10):
        id= i
        archivedState = "Archived"

        archivedDate = f"200{i}-06-06"
        roleId = 1
        add.add_to_archived_state(id, archivedState, archivedDate)
        print("success")
        time.sleep(wait_time)  
        
    id= 10
    archivedState = "Archived"
    archivedDate = "2016-11-06"
    add.add_to_archived_state(id, archivedState, archivedDate)
    print("success")
    time.sleep(wait_time)

    id= 11
    archivedState = "Archived"
    archivedDate = "2016-09-06"
    add.add_to_archived_state(id, archivedState, archivedDate)
    print("success")
    time.sleep(wait_time)


    # Case Location
    archiveNumber = 0
    location = "Cupboard 12"
    add.add_to_case_location(archiveNumber, location)
    print("success")
    time.sleep(wait_time)
    
    # Destruction State
    id= 1
    state = "Destroyed"
    add.add_to_destruction_state(id, state)
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
        print("success")
        time.sleep(wait_time)
    
    archiveNumber = 1
    archivedDate = "2016-09-06"
    add.add_to_case_drawn_by(archiveNumber, employeeId, archivedDate)
    print("success")
    time.sleep(wait_time)    
# create_database()
# populate_database()