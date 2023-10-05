import customtkinter as ctk
from functools import partial

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title('Login Page')
root.geometry("500x350")

def validateLogin(username, password):
    """Validate Login Details through database here"""
    print("username entered :", username.get())
    print("password entered :", password.get())
    return
    
    
frame = ctk.CTkFrame(master= root)

frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login Page", font=("Roboto", 24))
label.pack(pady=12, padx=10)

username = ctk.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password.pack(pady=12, padx=10)

validateLogin = partial(validateLogin, username, password)

button = ctk.CTkButton(master=frame, text="Login", command=validateLogin)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember me") 

root.mainloop()
