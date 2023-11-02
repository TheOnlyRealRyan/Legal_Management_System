from tksheet import Sheet
import tkinter as tk


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.sheet_demo = Sheet(self,
                                height = 500,
                                width = 700) 
        self.sheet_demo.enable_bindings(("single",
                                         "drag_select",
                                         "column_drag_and_drop",
                                         "row_drag_and_drop",
                                         "column_select",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         "row_width_resize",
                                         "column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "right_click_popup_menu",
                                         "rc_insert_column",
                                         "rc_delete_column",
                                         "rc_insert_row",
                                         "rc_delete_row",
                                         "copy",
                                         "cut",
                                         "paste",
                                         "delete",
                                         "undo",
                                         "edit_cell"))
    
        self.sheet_demo.grid(row = 0, column = 0, sticky = "nswe")
    
 
        self.data = [[f"" for c in range(1)] for r in range(100)]
        self.sheet_demo.data_reference(self.data)
    

        def click_this():
            for i in (self.sheet_demo.get_column_data(0)): 
                if i == '':
                    break
                else:
                    print(i.strip())
                    self.data = [[f"" for c in range(1)]for r in range(100)]
                    self.sheet_demo.data_reference(self.data)
                
        button=tk.Button(text=" click this",command= click_this)
        button.grid(row= 1, column=0, sticky= "n")


    
app = demo()
app.mainloop()