import tkinter as tk
from tkinter import ttk
from random import choice
import mysql_test_connection as db_conn

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data 
names = []
ages = []
data = db_conn.get_all_data()
print(data)
for name, age in data:
	names.append(name) 
	ages.append(age)



# treeview 
table = ttk.Treeview(window, columns = ('first', 'last'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.pack(fill = 'both', expand = True)

# insert values into a table
for i in range(len(names)):
    data = (names[i], ages[i])
    table.insert(parent = '', index = 0, values = data)


# events
def item_select(_):
	print(table.selection())
	for i in table.selection():
		print(table.item(i)['values'])
	# table.item(table.selection())

def delete_items(_):
	print('delete')
	for i in table.selection():
		table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run 
window.mainloop()