import tkinter as tk
from tkinter import ttk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login Tkinter')
        self.geometry('300x170')
        self.resizable(0,0)
        self.iconbitmap('user.ico')
    
        self._create_components()

    def _create_components(self):
        self.box_user = ttk.Labelframe(self, text='User')
        self.box_user.grid(row=0, column=0, padx=7, pady=(10,5))
        self.login_btn = ttk.Button(self, text='Login')
        self.login_btn.grid(row=2, column=0, ipadx=10, ipady=5, padx=(0, 20), sticky=tk.E)


        label_user = ttk.Label(self.box_user, text='Username')
        label_user.grid(row=0, column=0, padx=10, pady=(5,10))
        self.user_entry = ttk.Entry(self.box_user, width=30)
        self.user_entry.grid(row=0, column=1, padx=10, pady=(5,10))
        label_password = ttk.Label(self.box_user, text='Password')
        label_password.grid(row=1, column=0, padx=10, pady=(5,10))
        self.password_entry = ttk.Entry(self.box_user, width=30, show='*')
        self.password_entry.grid(row=1, column=1, padx=10)
        self.show_password = ttk.Checkbutton(self.box_user, text='Show password')
        self.show_password.grid(row=2, column=1, padx=10, pady=(0,5), sticky=tk.W)

if __name__ == "__main__":
    login_window = Login()
    login_window.mainloop()

