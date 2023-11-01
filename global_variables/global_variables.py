global user_role_logged_in
user_role_logged_in = 1
global user_id_logged_in
user_id_logged_in = 1

def get_role():
    return user_role_logged_in

def get_id():
    return user_id_logged_in

def set_role(role):
    global user_role_logged_in
    user_role_logged_in = role
    

def set_id(employeeId):
    global user_id_logged_in
    user_id_logged_in = employeeId