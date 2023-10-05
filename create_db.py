import mysql.connector

# Connect to Database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)
# Initialise cursor
mycursor = mydb.cursor()

# Create Database
# mycursor.execute("CREATE DATABASE projectdb")

# DELETE tables

mycursor.execute("DROP TABLE IF EXISTS employee_account")
mycursor.execute("DROP TABLE IF EXISTS user_login_data")
mycursor.execute("DROP TABLE IF EXISTS employee_roles")
mycursor.execute("DROP TABLE IF EXISTS client_information")
mycursor.execute("DROP TABLE IF EXISTS case_data")
mycursor.execute("DROP TABLE IF EXISTS archived_state")
mycursor.execute("DROP TABLE IF EXISTS deletion_logging")
mycursor.execute("DROP TABLE IF EXISTS deletion_confirmation")
mycursor.execute("DROP TABLE IF EXISTS destruction_state")
mycursor.execute("DROP TABLE IF EXISTS case_location")
mycursor.execute("DROP TABLE IF EXISTS case_drawn_by")
mycursor.execute("DROP TABLE IF EXISTS case_drawn_history")
mycursor.execute("DROP TABLE IF EXISTS file_upload_data")
mycursor.execute("DROP TABLE IF EXISTS archived_case_request")

# Create Tables
mycursor.execute("CREATE TABLE employee_account(employeeId INTEGER(10) NOT NULL AUTO_INCREMENT, age INTEGER(10), firstName VARCHAR(50),  lastName VARCHAR(50), gender VARCHAR(1),  dateOfBirth DATE, roleId INTEGER(10), PRIMARY KEY (employeeId), FOREIGN KEY (roleId) REFERENCES employee_roles(roleId))")
mycursor.execute("CREATE TABLE user_login_data(employeeId INTEGER, username VARCHAR(50), passwordHash VARCHAR(250), PRIMARY KEY (employeeId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE employee_roles(roleId INTEGER(10) NOT NULL AUTO_INCREMENT, roleDescription VARCHAR(20), PRIMARY KEY (roleId))")
mycursor.execute("CREATE TABLE client_information(clientId INTEGER(10) NOT NULL AUTO_INCREMENT, firstName VARCHAR(50), lastName VARCHAR(50), gender VARCHAR(1), dateOfBirth DATE, PRIMARY KEY (clientId))")
mycursor.execute("CREATE TABLE case_data(caseId INTEGER(10), clientId INTEGER(10), employeeId INTEGER(10), description VARCHAR(250), department VARCHAR(30), dateOfCaseOpen DATE, dateUploaded DATE, PRIMARY KEY (caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId), FOREIGN KEY (clientId) REFERENCES client_information(clientId))")
mycursor.execute("CREATE TABLE archived_state(caseId INTEGER(10), archivedState VARCHAR(10), archiveNumber INTEGER(10), archivedDate DATE, dateToBeDestroyed DATE, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
mycursor.execute("CREATE TABLE deletion_logging(caseId INTEGER(10), employeeId INTEGER, deletionDate DATE, deletionConfirmed BOOLEAN, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE deletion_confirmation(caseId INTEGER(10), employeeId1 INTEGER, employeeId2 INTEGER, employee1Confirmed BOOLEAN, employee2Confirmed BOOLEAN, PRIMARY KEY (caseId), FOREIGN KEY (employeeId1) REFERENCES employee_account(employeeId),  FOREIGN KEY (employeeId2) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE destruction_state(caseId INTEGER(10), destructionState VARCHAR(50), PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
mycursor.execute("CREATE TABLE case_location(caseId INTEGER(10), location VARCHAR(50), PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
mycursor.execute("CREATE TABLE case_drawn_by(caseId INTEGER(10), employeeId INTEGER, dateDrawnOut DATE, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE case_drawn_history(caseId INTEGER(10), employeeId INTEGER(10), dateDrawnOut DATE, dateDrawnIn DATE, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE file_upload_data(fileId INTEGER(10), fileName VARCHAR(100), caseId INTEGER(10), recievedDate DATE, dateUploaded DATETIME, PRIMARY KEY (fileId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")
mycursor.execute("CREATE TABLE archived_case_request(caseId INTEGER(10), employeeId INTEGER(10), dateRequested DATETIME, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId) )")

# Display Tables 
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)