import tkinter as tk
from tkinter import messagebox 
from database import init_db, add_user, validate_user

from busca import abrir_busca

def abrir_login():
    init_db()

    root = tk.Tk()
    root.title("Login Form")
    root.geometry("350x300")
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
            root.destroy()
            abrir_busca()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def register():
        user = username_var.get()
        pwd = password_var.get()
        if add_user(user, pwd):
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário já existe.")

    def toggle_password():
        if show_password.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    #titulo
    tk.Label(root, text="Login", font=("Arial", 19, "bold"), bg="#f0f0f0").pack(pady=10)

    #usuario
    tk.Label(root, text="Usuário:", bg="#f0f0f0").pack(anchor="w", padx=30)
    tk.Entry(root, textvariable=username_var, width=30).pack(pady=2)

    #senha
    tk.Label(root, text="Senha:", bg="#f0f0f0").pack(anchor="w", padx=30)
    password_entry = tk.Entry(root, textvariable=password_var, width=30, show="*")
    password_entry.pack(pady=2)

    #visualizar senha
    toggle_btn = tk.Checkbutton(root, text="Mostrar senha", variable=show_password, bg="#f0f0f0", command=toggle_password)
    toggle_btn.pack(anchor="w", padx=30,pady=5)

    #lembrarsenha
    remember_cb = tk.Checkbutton(root, text="Lembrar senha", variable=remember_me, bg="#f0f0f0")
    remember_cb.pack(anchor="w", padx=30,pady=5)

    #botoes de login ou registro
    tk.Button(root, text="Login", command=login, width=25, bg="#9d88e9", fg="white").pack(pady=8)
    tk.Button(root, text="Registro", command=register, width=25, bg="#725dbb", fg="white").pack()


    root.mainloop()