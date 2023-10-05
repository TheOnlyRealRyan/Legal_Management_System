import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database="testdb"
)
# mycursor.execute("")

def get_all_data():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    myresult = mycursor.fetchall() # only one result = .fetchone()

    return myresult

"""
# Create Database
mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW DATABASES")

# Create Table
mycursor.execute("CREATE TABLE students (name VARCHAR(225), age INTEGER(10))")
for db in mycursor:
    print(db)

# show tables
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

# Insert into table
# %s = placeholders - replace with anything
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)" # ALWAYS USE THIS FOR SQL INJECTION
student1 = ("Rachel", 22)
student_array = [("Amber", 20),
                 ("Ryan", 21),
                 ("James", 24),]

mycursor.execute(sqlFormula, student1)
mycursor.executemany(sqlFormula, student_array)

mydb.commit()

# Query Database
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall() # only one result = .fetchone()

for row in myresult:
    print(row)

# update database    
sql = "UPDATE students SET age = 13 WHERE name = 'Rachel'"

# delete from database    
sql = "DELETE FROM students WHERE name = 'Rachel'"

# DROP table
sql = "DROP TABLE IF EXISTS students"


"""

