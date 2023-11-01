import mysql.connector
import tkinter.messagebox 
from datetime import datetime


import global_variables as gv


messagebox_show = True


# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)


# Initialise cursor:
mycursor = mydb.cursor()


def update_deletion_confirmation_employee2(caseId, confirm):
    try:            
        employeeId2 = gv.get_id()
        mycursor.execute(f"UPDATE deletion_confirmation SET employee2Confirmed = '{confirm}', employeeId2 = '{employeeId2}' WHERE caseId = '{caseId}';")
        mydb.commit()
        
        sqlFormula = "INSERT INTO deletion_logging (caseId, employeeId, deletionDate, deletionConfirmed) VALUE (%s, %s, %s, %s)"
        details = (caseId, employeeId2, datetime.today().strftime('%Y-%m-%d %H:%M:%S'), confirm)
        mycursor.execute(sqlFormula, details)  
        mydb.commit()
        if messagebox_show == True: tkinter.messagebox.showinfo("Success",  "Succesfully Updated Database")
    except Exception as e:
        if messagebox_show == True: tkinter.messagebox.showinfo("Failed",  "Failed to Update Database")
        print(e)
        
    
    
