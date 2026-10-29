import tkinter as tk
from tkinter import ttk

window = tk.Tk() 
window.geometry('500x200') 
window.title('LoginTable')

first_names = ['Muhammad', 'Isa', 'Omar', 'Bob', 'Nastya', 'Andrew', 'Daniel', 'Huseyn', 'Yusuf', 'David', 'Seo-ah']
last_names = ['Ibrahimovic', 'Qadir', 'Othman', 'Omar', 'Niazi', 'Nasir', 'Moghadam', 'Mirza', 'Harroun', 'Hai']

table = ttk.Treeview(window, columns = ('first', 'last', 'email')) 
table.pack()

window.mainloop()
