import customtkinter

self.canvas = customtkinter.CTkCanvas(self)
self.canvas.grid(row=0, column=1, columnspan=1, sticky="nsew")
self.canvas.create_line(500, 25, 850, 25)
self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
self.canvas.create_oval(10, 10, 20, 20, fill="red")
self.canvas.create_oval(1400, 1400, 220, 220, fill="blue")

# create CTk scrollbar
self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self, command=self.canvas.yview)
self.ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

self.canvas.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)