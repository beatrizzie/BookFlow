import tkinter as tk
from tkinter import ttk
from datetime import datetime

from database import listar_emprestimos_usuario


COR_FUNDO = "#FFFFFF"
COR_BOTAO = "#000000"
COR_TEXTO = "#000000"
COR_TEXTO_BOTAO = "#FFFFFF"


def abrir_area_usuario(
    root,
    limpar_tela,
    tela_inicial,
    usuario_id
):

    limpar_tela()

    root.configure(bg=COR_FUNDO)


    tk.Label(
        root,
        text="📚 Área do Usuário",
        font=("Arial", 18, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(pady=15)

    tk.Label(
        root,
        text="Meus Empréstimos",
        font=("Arial", 14, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack()


    colunas = (
        "Livro",
        "Autor",
        "Entrega",
        "Status"
    )

    tabela = ttk.Treeview(
        root,
        columns=colunas,
        show="headings",
        height=12
    )

    tabela.heading("Livro", text="Livro")
    tabela.heading("Autor", text="Autor")
    tabela.heading("Entrega", text="Data Entrega")
    tabela.heading("Status", text="Status")

    tabela.column("Livro", width=250)
    tabela.column("Autor", width=180)
    tabela.column("Entrega", width=120)
    tabela.column("Status", width=120)

    tabela.pack(
        pady=15,
        padx=10,
        fill="both",
        expand=True
    )

    tabela.tag_configure(
        "atrasado",
        foreground="red"
    )

    tabela.tag_configure(
        "emdeia",
        foreground="green"
    )


    emprestimos = listar_emprestimos_usuario(
        usuario_id
    )

    hoje = datetime.now().date()

    if not emprestimos:

        tabela.insert(
            "",
            tk.END,
            values=(
                "Nenhum empréstimo encontrado",
                "",
                "",
                ""
            )
        )

    for emp in emprestimos:

        livro = emp[0]
        autor = emp[1]
        ano = emp[2]
        data_emprestimo = emp[3]
        data_entrega = emp[4]
        status = emp[5]

        status_exibicao = status
        tag = "emdeia"

        if status == "ATIVO":

            try:

                entrega = datetime.strptime(
                    data_entrega,
                    "%Y-%m-%d"
                ).date()

                if entrega < hoje:

                    status_exibicao = "ATRASADO"
                    tag = "atrasado"

            except:
                pass

        tabela.insert(
            "",
            tk.END,
            values=(
                livro,
                autor,
                data_entrega,
                status_exibicao
            ),
            tags=(tag,)
        )


    tk.Button(
        root,
        text="⬅ Voltar",
        width=25,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=("Arial", 10, "bold"),
        command=tela_inicial
    ).pack(pady=15)