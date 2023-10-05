import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)
# Initialise cursor
mycursor = mydb.cursor()


"""
# create Database
mycursor.execute("CREATE DATABASE projectdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
"""

# Create Tables

# VARCHAR
# INTEGER
# NOT NULL AUTO_INCREMENT
# PRIMARY KEY (employeeId)
# FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId)

# mycursor.execute("CREATE TABLE employee_account(employeeId INTEGER(10) NOT NULL AUTO_INCREMENT, age INTEGER(10), firstName VARCHAR(50),  lastName VARCHAR(50), gender VARCHAR(1),  dateOfBirth DATE, roleId INTEGER(10), PRIMARY KEY (employeeId), FOREIGN KEY (roleId) REFERENCES employee_roles(roleId))")
# mycursor.execute("CREATE TABLE user_login_data(employeeId INTEGER, username VARCHAR(50), passwordHash VARCHAR(250), PRIMARY KEY (employeeId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId))")
mycursor.execute("CREATE TABLE employee_roles(roleId integer NOT NULL AUTO_INCREMENT, roleDescription varchar(20), PRIMARY KEY (roleId))")

mycursor.execute("CREATE TABLE case_data(caseId INTEGER(10), clientId INTEGER(10), employeeId INTEGER(10), description VARCHAR(250), department VARCHAR(30), dateOfCaseOpen DATE, dateUploaded DATE, PRIMARY KEY (caseId), FOREIGN KEY (employeeId) REFERENCES employee_account(employeeId), FOREIGN KEY (clientId) REFERENCES client_information(clientId))")

mycursor.execute("CREATE TABLE client_information(clientId INTEGER NOT NULL AUTO_INCREMENT, firstName VARCHAR(50), lastName VARCHAR(50), gender VARCHAR(1), dateOfBirth DATE, PRIMARY KEY (clientId))")

mycursor.execute("CREATE TABLE archived_state(caseId INTEGER(10), archivedState VARCHAR(10), archiveNumber INTEGER(10), archivedDate DATE, dateToBeDestroyed DATE, PRIMARY KEY (caseId), FOREIGN KEY (caseId) REFERENCES case_data(caseId))")


mycursor.execute("CREATE TABLE deletion_logging(employeeId INTEGER)")
mycursor.execute("CREATE TABLE deletion_confirmation(employeeId INTEGER)")
mycursor.execute("CREATE TABLE destruction_state(employeeId INTEGER)")
mycursor.execute("CREATE TABLE case_location(employeeId INTEGER)")
mycursor.execute("CREATE TABLE case_drawn_history(employeeId INTEGER)")
mycursor.execute("CREATE TABLE file_upload_data(employeeId INTEGER)")
mycursor.execute("CREATE TABLE archived_case_request(employeeId INTEGER)")




mycursor.execute("SELECT * FROM employee_account")
for db in mycursor:
    print(db)