import tkinter as tk

COR_FUNDO = "#FFFFFF"      # fundo branco
COR_BOTAO = "#000000"      # botão preto
COR_TEXTO = "#000000"      # textos normais pretos
COR_TEXTO_BOTAO = "#FFFFFF"  # texto dos botões branco

from tkinter import messagebox

from database import add_user, validate_user


def abrir_login_usuario(root, limpar_tela, tela_inicial):

    limpar_tela()

    tk.Label(
        root,
        text="📚 Login do Usuário",
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
        width=40,
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
    )
    entry_senha.pack(pady=5)

    # Mostrar senha

    mostrar_senha = tk.BooleanVar()

    def alternar_senha():

        if mostrar_senha.get():
            entry_senha.config(show="")
        else:
            entry_senha.config(show="*")

    tk.Checkbutton(
        root,
        text="Mostrar senha",
        variable=mostrar_senha,
        command=alternar_senha,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 12, "bold"),
    ).pack(pady=5)

    # Cadastro

    def cadastrar():

        usuario = entry_usuario.get().strip()
        senha = entry_senha.get().strip()

        if not usuario or not senha:

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )
            return

        try:

            add_user(
                usuario,
                senha
            )

            messagebox.showinfo(
                "Sucesso",
                "Usuário cadastrado com sucesso!"
            )

        except:

            messagebox.showerror(
                "Erro",
                "Usuário já existe."
            )

    # Login

    def entrar():

        usuario = validate_user(
            entry_usuario.get().strip(),
            entry_senha.get().strip()
        )

        if usuario:

            from usuario import abrir_area_usuario

            abrir_area_usuario(
                root,
                limpar_tela,
                tela_inicial,
                usuario[0]
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
        command=entrar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Cadastrar",
        width=25,
        height=2,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 8, "bold"),
        command=cadastrar
    ).pack(pady=5)

    def abrir_funcionario():

        from funcionario_login import abrir_login_funcionario

        abrir_login_funcionario(
            root,
            limpar_tela,
            tela_inicial
        )

    tk.Button(
        root,
        text="Voltar",
        width=25,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 7, "bold"),
        command=tela_inicial
    ).pack(pady=5)