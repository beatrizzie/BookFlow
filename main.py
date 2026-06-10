import tkinter as tk

from funcionario_login import COR_TEXTO_BOTAO

COR_FUNDO = "#FFFFFF"      # fundo branco
COR_BOTAO = "#000000"      # botão preto
COR_TEXTO = "#000000"      # textos normais pretos
COR_TEXTO_BOTAO = "#FFFFFF"  # texto dos botões branco

# ==========================
# JANELA PRINCIPAL
# ==========================

root = tk.Tk()
root.configure(bg=COR_FUNDO)
root.title("BOOKFLOW")
root.geometry("1200x800")
root.resizable(False, False)


# ==========================
# LIMPAR TELA
# ==========================

def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()


# ==========================
# ABRIR LOGIN USUÁRIO
# ==========================

def abrir_login_usuario_tela():
    print("Botao usuario clicado")

    from usuario_login import abrir_login_usuario

    abrir_login_usuario(
        root,
        limpar_tela,
        tela_inicial
    )


# ==========================
# ABRIR LOGIN FUNCIONÁRIO
# ==========================

def abrir_login_funcionario():

    from funcionario_login import abrir_login_funcionario

    abrir_login_funcionario(
        root,
        limpar_tela,
        tela_inicial
    )


# ==========================
# TELA DE LOGIN PRINCIPAL
# ==========================

def tela_login():

    limpar_tela()

    tk.Label(
        root,
        text="📚 BOOKFLOW",
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    tk.Label(
        root,
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        text="Faça seu login",
        font=("Arial", 14)
    ).pack(pady=10)

    tk.Button(
        root,
        text="Entrar como Usuário",
        width=25,
        height=2,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=('Arial', 11, 'bold'),
        bd=0,
        cursor='hand2',
        command=abrir_login_usuario_tela
    ).pack(pady=10)

    tk.Button(
        root,
        text="Sou Funcionário",
        width=25,
        height=2,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=('Arial', 11, 'bold'),
        bd=0,
        cursor='hand2',
        command=abrir_login_funcionario
    ).pack(pady=5)


# ==========================
# SPLASH BOOKFLOW
# ==========================

def tela_inicial():

    limpar_tela()
    root.configure(bg=COR_FUNDO)

    tk.Label(
        root,
        text="📚 BOOKFLOW",
        font=("Arial", 30, "bold")
    ).pack(expand=True)

    root.after(
        2000,
        tela_login
    )


# ==========================
# INICIAR
# ==========================

tela_inicial()

root.mainloop()