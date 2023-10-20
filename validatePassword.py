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


def hash_password(password):
    """ The function takes in password and returns a hexidecimal hashed number"""
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()


def validate(username, password):
    """ Check if password hash given is equal to password hash associate with username from database"""
    hashed_password = hash_password(password)
    mycursor.execute(f"SELECT passwordHash FROM user_login_data WHERE username = '{username}'") 
    myresult = mycursor.fetchall() 
    for x in myresult:  
        db_password_hash = x[0]

    
    if hashed_password == db_password_hash:
        tkinter.messagebox.showinfo("Success",  "Welcome")
        return True
    else:
        tkinter.messagebox.showinfo("Failed",  "Incorrect login details")
        return False
    
    
    