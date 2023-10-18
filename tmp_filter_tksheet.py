from tksheet import Sheet
import tkinter as tk


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.data = ([["3", "c", "z"],
                      ["1", "a", "x"],
                      ["1", "b", "y"],
                      ["2", "b", "y"],
                      ["2", "c", "z"]])
        self.sheet = Sheet(self.frame,
                           data = self.data,
                           theme = "dark",
                           height = 700,
                           width = 1100)
        self.sheet.enable_bindings("copy",
                                   "rc_select",
                                   "arrowkeys",
                                   "double_click_column_resize",
                                   "column_width_resize",
                                   "column_select",
                                   "row_select",
                                   "drag_select",
                                   "single_select",
                                   "select_all")
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
        self.sheet.create_header_dropdown(c = 0,
                                          values = ["all", "1", "2", "3"],
                                          set_value = "all",
                                          selection_function = self.header_dropdown_selected,
                                          text = "Header A Name")
        self.sheet.create_header_dropdown(c = 1,
                                          values = ["all", "a", "b", "c"],
                                          set_value = "all",
                                          selection_function = self.header_dropdown_selected,
                                          text = "Header B Name")
        self.sheet.create_header_dropdown(c = 2,
                                          values = ["all", "x", "y", "z"],
                                          set_value = "all",
                                          selection_function = self.header_dropdown_selected,
                                          text = "Header C Name")

    def header_dropdown_selected(self, event = None):
        hdrs = self.sheet.headers()
        # this function is run before header cell data is set by dropdown selection
        # so we have to get the new value from the event
        hdrs[event.column] = event.text
        if all(dd == "all" for dd in hdrs):
            self.sheet.display_rows("all")
        else:
            rows = [rn for rn, row in enumerate(self.data) if all(row[c] == e or e == "all" for c, e in enumerate(hdrs))]
            self.sheet.display_rows(rows = rows,
                                    all_displayed = False)
        self.sheet.redraw()
    
app = demo()
app.mainloop()