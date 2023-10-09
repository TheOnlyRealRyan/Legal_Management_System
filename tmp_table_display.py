# data 
ids = []
roles = []
data = db_conn.all_employee_roles()
print(data)
for id, role in data:
    ids.append(id) 
    roles.append(role)

# Table 
headers = ['id', 'roles']
for col, header in enumerate(headers):
    label = customtkinter.CTkLabel(self.right_dashboard, text=header, font=("Roboto", 24))
    label.grid(row=2, column=col, padx=10, pady=5)

widths = [50, 1000] # Column Widths
for row, row_data in enumerate(data, start=3):
    for col, value in enumerate(row_data):
        entry = CTkEntry(self.right_dashboard, width=widths[col])
        entry.insert(tkinter.END, value)
        entry.grid(row=row, column=col, padx=10, pady=5)