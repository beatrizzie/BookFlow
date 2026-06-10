import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import messagebox
from datetime import datetime
import requests

from database import (
    listar_usuarios,
    cadastrar_emprestimo,
    listar_todos_emprestimos,
    registrar_devolucao
)


def abrir_area_funcionario(root, limpar_tela, tela_inicial):

    limpar_tela()


    COR_FUNDO = "#FFFFFF"  
    COR_BOTAO = "#000000"  
    COR_TEXTO = "#000000"  
    COR_TEXTO_BOTAO = "#FFFFFF"  

    tk.Label(
        root,
        text="📚 Painel do Funcionário",
        font=("Arial", 20, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO_BOTAO
    ).pack(pady=20)



    tk.Label(
        root,
        text="Buscar Livros",
        font=("Arial", 15, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack()

    entry_busca = tk.Entry(
        root,
        width=40
    )

    entry_busca.pack(pady=5)

    lista_busca = tk.Listbox(
        root,
        width=100,
        height=6,
        bg="white",
        fg=COR_TEXTO
    )
    lista_busca.pack(pady=5)

    livros_encontrados = []
    livro_selecionado = {}

    def buscar_livros():

        lista_busca.delete(0, tk.END)
        livros_encontrados.clear()

        termo = entry_busca.get().strip()

        if not termo:
            return

        try:

            url = f"https://openlibrary.org/search.json?q={termo}"

            resposta = requests.get(url)
            dados = resposta.json()

            livros = dados.get("docs", [])[:10]

            for livro in livros:

                titulo = livro.get(
                    "title",
                    "Sem título"
                )

                autor = "Desconhecido"

                if "author_name" in livro:
                    autor = livro["author_name"][0]

                ano = livro.get(
                    "first_publish_year",
                    "N/A"
                )

                livros_encontrados.append({
                    "titulo": titulo,
                    "autor": autor,
                    "ano": ano
                })

                lista_busca.insert(
                    tk.END,
                    f"{titulo} | {autor} | {ano}"
                )

        except:

            messagebox.showerror(
                "Erro",
                "Falha ao buscar livros."
            )

    tk.Button(
        root,
        text="Pesquisar",
        width=25,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=("Arial", 12, "bold"),
        command=buscar_livros
    ).pack(pady=5)


    tk.Label(
        root,
        text="Livro Selecionado",
        font=("Arial", 15, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(pady=10)

    label_livro = tk.Label(
        root,
        text="Nenhum livro selecionado",
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 12, "bold")
    )
    label_livro.pack()

    label_autor = tk.Label(
        root,
        text="",
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 11)
    )
    label_autor.pack()

    label_ano = tk.Label(
        root,
        text="",
        bg=COR_FUNDO,
        fg=COR_TEXTO,
        font=("Arial", 11)
    )
    label_ano.pack()

    def selecionar_livro(event):

        if not lista_busca.curselection():
            return

        indice = lista_busca.curselection()[0]

        livro = livros_encontrados[indice]

        livro_selecionado.clear()
        livro_selecionado.update(livro)

        label_livro.config(
            text=livro["titulo"]
        )

        label_autor.config(
            text=f"Autor: {livro['autor']}"
        )

        label_ano.config(
            text=f"Ano: {livro['ano']}"
        )

    lista_busca.bind(
        "<<ListboxSelect>>",
        selecionar_livro
    )


    tk.Label(
        root,
        text="Usuário",
        font=("Arial", 10, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(pady=5)

    usuarios = listar_usuarios()

    combo_usuario = ttk.Combobox(
        root,
        values=[u[1] for u in usuarios],
        state="readonly",
        width=40
    )

    combo_usuario.pack()

    entry_entrega = tk.Entry(
        root,
        width=25,
        state="readonly"
    )

    entry_entrega.pack()

    data_entrega = (
            datetime.now() + timedelta(days=30)
    ).strftime("%Y-%m-%d")

    entry_entrega.config(state="normal")
    entry_entrega.insert(0, data_entrega)
    entry_entrega.config(state="readonly")

    def cadastrar():
        print("BOTAO CADASTRADO")

        if not livro_selecionado:

            messagebox.showerror(
                "Erro",
                "Selecione um livro."
            )

            return

        usuario_nome = combo_usuario.get()

        usuario_id = None

        for usuario in usuarios:

            if usuario[1] == usuario_nome:
                usuario_id = usuario[0]
                break

        if usuario_id is None:

            messagebox.showerror(
                "Erro",
                "Selecione um usuário."
            )

            return

        cadastrar_emprestimo(
            usuario_id,
            livro_selecionado["titulo"],
            livro_selecionado["autor"],
            str(livro_selecionado["ano"]),
            datetime.now().strftime("%Y-%m-%d"),
            data_entrega
        )

        messagebox.showinfo(
            "Sucesso",
            "Empréstimo cadastrado!"
        )

        atualizar_lista()

    tk.Button(
        root,
        text="Cadastrar Empréstimo",
        width=25,
        height=2,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=("Arial", 8, "bold"),
        command=cadastrar
    ).pack(pady=10)


    lista = tk.Listbox(
        root,
        width=120,
        height=8,
        bg="white",
        fg=COR_TEXTO
    )

    lista.pack(pady=10)

    def atualizar_lista():

        lista.delete(0, tk.END)

        dados = listar_todos_emprestimos()

        for item in dados:

            lista.insert(
                tk.END,
                f"ID:{item[0]} | {item[1]} | {item[2]} | {item[3]} | Entrega:{item[4]} | {item[5]}"
            )

    atualizar_lista()


    tk.Label(
        root,
        text="ID do empréstimo"
    ).pack()

    entry_id = tk.Entry(root)
    entry_id.pack()

    def devolver():

        try:

            registrar_devolucao(
                int(entry_id.get())
            )

            atualizar_lista()

            messagebox.showinfo(
                "Sucesso",
                "Devolução registrada."
            )

        except:

            messagebox.showerror(
                "Erro",
                "ID inválido."
            )

    tk.Button(
        root,
        text="Registrar Devolução",
        width=25,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=("Arial", 10, "bold"),
        command=devolver
    ).pack(pady=5)

    tk.Button(
        root,
        text="⬅ Voltar",
        width=25,
        bg=COR_BOTAO,
        fg=COR_TEXTO_BOTAO,
        font=("Arial", 10, "bold"),
        command=tela_inicial
    ).pack(pady=5)