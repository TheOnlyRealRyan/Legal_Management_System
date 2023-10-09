import mysql.connector
import tkinter.messagebox 
import hashlib
from datetime import datetime, date


# Conenct to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="projectdb"
)

# Initialise cursor:
mycursor = mydb.cursor()

def all_employee_roles():
    mycursor.execute("SELECT * FROM employee_roles")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_user_login_data():
    mycursor.execute("SELECT * FROM user_login_data")
    myresult = mycursor.fetchall()
    return myresult


def all_client_information():
    mycursor.execute("SELECT * FROM client_information")
    myresult = mycursor.fetchall()
    return myresult


def all_case_data():
    mycursor.execute("SELECT * FROM case_data")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_state():
    mycursor.execute("SELECT * FROM archived_state")
    myresult = mycursor.fetchall()
    return myresult


def all_case_location():
    mycursor.execute("SELECT * FROM case_location")
    myresult = mycursor.fetchall()
    return myresult


def all_destruction_state():
    mycursor.execute("SELECT * FROM destruction_state")
    myresult = mycursor.fetchall()
    return myresult


def all_file_upload_data():
    mycursor.execute("SELECT * FROM file_upload_data")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_confirmation():
    mycursor.execute("SELECT * FROM deletion_confirmation")
    myresult = mycursor.fetchall()
    return myresult


def all_deletion_logging():
    mycursor.execute("SELECT * FROM deletion_logging")
    myresult = mycursor.fetchall()
    return myresult


def all_archived_case_request():
    mycursor.execute("SELECT * FROM archived_case_request")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_by():
    mycursor.execute("SELECT * FROM case_drawn_by")
    myresult = mycursor.fetchall()
    return myresult


def all_case_drawn_history():
    mycursor.execute("SELECT * FROM case_drawn_history")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult
