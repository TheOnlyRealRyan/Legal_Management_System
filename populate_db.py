import add_to_db as add
import time
for i in range(50):
    name = f"ryan{i}"
    surname = "Putzier"
    gender = "M"
    dob = "2001-06-06"
    add.add_to_client_information(name, surname, gender, dob)
    print("success")
    time.sleep(0.2)
    