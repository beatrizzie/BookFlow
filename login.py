import tkinter as tk
from tkinter import messagebox 
from database import init_db, add_user, validate_user

init_db()

root = tk.Tk()
root.title("Login Form")
root.geometry("350x200")
root.config(bg="#f0f0f0")
root.resizable(False, False)

username_var = tk.StringVar()
password_var = tk.StringVar()
show_password = tk.BooleanVar(value=False)
remember_me = tk.BooleanVar()

def login():
    user = username_var.get()
    pwd = password_var.get()
    if validate_user(user, pwd):
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def register():
    user = username_var.get()
    pwd = password_var.get()
    if add_user(user, pwd):
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário já existe.")

root.mainloop()