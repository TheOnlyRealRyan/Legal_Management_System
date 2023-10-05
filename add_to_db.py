import mysql.connector
import tkinter.messagebox 
import hashlib
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

def add_to_employee_roles(roleDescription) -> None:
    """Inserts a role description and roleId into employee_roles database"""
       
    if roleDescription == "" or len(roleDescription)>49:
        print("Redo")
    else:         
        # sqlFormula = Anti-SQL Injection           
        sqlFormula = "INSERT INTO employee_roles (roleId, roleDescription) VALUE (%s, %s)" # %s = placeholders - replace with anything
        
        # Auto Increment done manually cause it doesnt work :(
        # TODO: Fix auto-increment
        # Grab last added roleId and add 1
        mycursor.execute("SELECT roleId FROM employee_roles ORDER BY roleId DESC LIMIT 1") 
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            id = 0
        else:    
            for x in myresult:
                id = x[0]+1
                
        # Insert into Db     
        employee_role_1 = (id, roleDescription)
        mycursor.execute(sqlFormula, employee_role_1)      
        mydb.commit()
        
        tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
        
        
def add_to_employee_account(age, firstname, lastname, gender, dateOfBirth, roleId) -> None:
    """Inserts details of employee into employee_account database"""
    # TODO: Error handling of inputs
    sqlFormula = "INSERT INTO employee_account (employeeId, age, firstname, lastname, gender, dateOfBirth, roleId) VALUE (%s, %s, %s, %s, %s, %s, %s)"
    
    # Manual auto-increment
    mycursor.execute("SELECT employeeId FROM employee_account ORDER BY employeeId DESC LIMIT 1") 
    myresult = mycursor.fetchall()
    print(myresult)
    if len(myresult) == 0:
        employeeId = 0
    else:    
        for x in myresult:
            employeeId = x[0]+1
     
    # Insert into Db     
    employee_account_details = (employeeId, age, firstname, lastname, gender, dateOfBirth, roleId)
    mycursor.execute(sqlFormula, employee_account_details)   
    mydb.commit()
    
    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
    
def add_to_user_login_data(employeeId, username, password) -> None:
    """Inserts login details into user_login_data database"""
    # TODO: Error handling of inputs
    sqlFormula = "INSERT INTO user_login_data (employeeId, username, passwordHash) VALUE (%s, %s, %s)"
    
    # Take in password and generate Hash
    passwordHash = hash_password(password)
     
    # Insert into Db     
    employee_login_details = (employeeId, username, passwordHash)
    mycursor.execute(sqlFormula, employee_login_details)   
    mydb.commit()

    tkinter.messagebox.showinfo("Success",  "Succesfully Inserted into Database")
    
def hash_password(password):
    """ The function takes in password and returns a hexidecimal hashed number"""
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

# TODO: Fix check_password()
"""
def check_password() -> None:
    username = list('ryan')
    sqlFormula = "SELECT passwordHash FROM user_login_data WHERE username = (%s))"
    mycursor.execute(sqlFormula, username)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
check_password()

"""