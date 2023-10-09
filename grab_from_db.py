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


def all_client_information():
    mycursor.execute("SELECT * FROM client_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult


def all_employees():
    mycursor.execute("SELECT * FROM employee_information")
    myresult = mycursor.fetchall()
    return myresult
