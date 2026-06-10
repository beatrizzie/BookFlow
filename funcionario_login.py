import tkinter as tk

COR_FUNDO = "#FFFFFF"      
COR_BOTAO = "#000000"      
COR_TEXTO = "#000000"      
COR_TEXTO_BOTAO = "#FFFFFF"  

from tkinter import messagebox

from database import (
    add_funcionario,
    validate_funcionario
)


def abrir_login_funcionario(root, limpar_tela, tela_inicial):

    limpar_tela()

    tk.Label(
        root,
        text="📚 Login do Funcionário",
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        root,
        text="Usuário",
        font=("Arial", 15, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    ).pack()

    entry_usuario = tk.Entry(
        root,
        width=40
    )
    entry_usuario.pack(pady=5)

    tk.Label(
        root,
        text="Senha",
        font=("Arial", 15, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO,
    ).pack()

    entry_senha = tk.Entry(
        root,
        width=40,
        show="*"
    )
    entry_senha.pack(pady=5)



    def mostrar_senha():

        if var_senha.get():
            entry_senha.config(show="")
        else:
            entry_senha.config(show="*")

    var_senha = tk.BooleanVar()

    tk.Checkbutton(
        root,
        text="Mostrar senha",
        variable=var_senha,
        command=mostrar_senha,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 12, "bold"),
    ).pack(pady=5)



    def registrar():

        usuario = entry_usuario.get().strip()
        senha = entry_senha.get().strip()

        if not usuario or not senha:

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )
            return

        try:

            add_funcionario(
                usuario,
                senha
            )

            messagebox.showinfo(
                "Sucesso",
                "Funcionário cadastrado!"
            )

        except:

            messagebox.showerror(
                "Erro",
                "Funcionário já existe."
            )



    def login():

        funcionario = validate_funcionario(
            entry_usuario.get(),
            entry_senha.get()
        )

        if funcionario:

            from funcionario import abrir_area_funcionario

            abrir_area_funcionario(
                root,
                limpar_tela,
                tela_inicial
            )

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha inválidos."
            )

    tk.Button(
        root,
        text="Entrar",
        width=25,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 12, "bold"),
        command=login
    ).pack(pady=10)

    tk.Button(
        root,
        text="Cadastrar Funcionário",
        width=25,
        height=2,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 8, "bold"),
        command=registrar
    ).pack(pady=5)

    tk.Button(
        root,
        text="Voltar",
        width=25,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 7, "bold"),
        command=tela_inicial
    ).pack(pady=5)