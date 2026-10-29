import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('500x300')
window.title('LoginTable')

first_names = ['Muhammad', 'Isa', 'Omar', 'Bob', 'Nastya', 'Andrew', 'Daniel', 'Yusuf', 'David', 'Seo-ah']
last_names = ['Ibrahimovic', 'Qadir', 'Othman', 'Omar', 'Niazi', 'Nasir', 'Moghadam', 'Mirza', 'Harroun', 'Hai']

table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')

# Use the exact column identifiers ('first', 'last') matching columns
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand=True, padx=10, pady=10)

# Insert random values into the table
for i in range(100):
    first = choice(first_names)
    last = choice(last_names) 
    email = f'{first.lower()}.{last.lower()}@email.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

window.mainloop()
