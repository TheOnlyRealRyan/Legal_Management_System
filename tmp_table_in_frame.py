import tmp_mysql_connection as db_conn
import tkinter
from tkinter import ttk
import customtkinter
from functools import partial

class App(customtkinter.CTk):

    frames = {}
    current = None
    bg = ""
    def __init__(self):
        super().__init__()
        self.bg = self.cget("fg_color")
        self.num_of_frames = 0
        # self.state('withdraw')
        self.title("Change Frames")

        # screen size
        self.geometry("800x600")
    def create_frame(self, frame_id, color):
        # data 
        names = []
        ages = []
        data = db_conn.get_all_data()

        for name, age in data:
            names.append(name) 
            ages.append(age)

        App.frames[frame_id] = customtkinter.CTkFrame(self, fg_color=self.cget("fg_color"))
        App.frames[frame_id].configure(corner_radius = 8)
        App.frames[frame_id].configure(fg_color = color)
        App.frames[frame_id].configure(border_width = 2)
        App.frames[frame_id].configure(border_color = "#323232")
        App.frames[frame_id].padx = 8

        # bt_from_frame1 = customtkinter.CTkButton(App.frames[frame_id], text="Test "+ self.color_by_id(self.num_of_frames) , command=lambda:print("test " + color) )
        # bt_from_frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        table = ttk.Treeview(App.frames[frame_id], columns = ('first', 'last'), show = 'headings')
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