import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Login Tkinter')
root.geometry('300x170')
root.resizable(0,0)
root.iconbitmap('user.ico')

box_user = ttk.Labelframe(root, text='User')
box_user.grid(row=0, column=0, padx=7, pady=(10,5))
login_btn = ttk.Button(root, text='Login')
login_btn.grid(row=2, column=0, ipadx=10, ipady=5, padx=(0, 20), sticky='E')


label_user = ttk.Label(box_user, text='Username')
label_user.grid(row=0, column=0, padx=10, pady=(5,10))
user_entry = ttk.Entry(box_user, width=30)
user_entry.grid(row=0, column=1, padx=10, pady=(5,10))
label_password = ttk.Label(box_user, text='Password')
label_password.grid(row=1, column=0, padx=10, pady=(5,10))
password_entry = ttk.Entry(box_user, width=30, show='*')
password_entry.grid(row=1, column=1, padx=10)
show_password = ttk.Checkbutton(box_user, text='Show password')
show_password.grid(row=2, column=1, padx=10, pady=(0,5), sticky='W')

root.mainloop()
