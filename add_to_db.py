import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

def add_to_employee_roles(roleDescription) -> None:
        # Insert into table
        # %s = placeholders - replace with anything
        # sqlFormula = Anti-SQL Injection
        # roleDescription = txtfld.get()
        if roleDescription == "" or len(roleDescription)>49:
            print("Redo")
        else:            
            sqlFormula = "INSERT INTO employee_roles (roleId, roleDescription) VALUE (%s, %s)" 
            
            # Auto Increment done manually cause it doesnt work :(
            mycursor.execute("SELECT roleId FROM employee_roles ORDER BY roleId DESC LIMIT 1");
            myresult = mycursor.fetchall()
            for x in myresult:
                id = x[0]+1
            # Insert into Db     
            employee_role_1 = (id, roleDescription)
            mycursor.execute(sqlFormula, employee_role_1)
            
            mydb.commit()
            print("Succesfully Inserted")
            