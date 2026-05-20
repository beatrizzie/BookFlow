import requests
import tkinter as tk
from tkinter import messagebox

def abrir_busca():

    def buscar_livros():
        termo = entrada.get()

        if not termo.strip():
            messagebox.showwarning("Aviso", "Digite algo para buscar.")
            return

        try:
            response = requests.get(
                "https://openlibrary.org/search.json",
                params={"q": termo},
                timeout=15
            )

            dados = response.json()

            resultado_texto.delete(1.0, tk.END)

            if "docs" not in dados:
                resultado_texto.insert(tk.END, "❌ Nenhum livro encontrado.")
                return

            for item in dados["docs"][:10]:

                titulo = item.get("title", "Sem título")

                autores = ", ".join(
                    item.get("author_name", ["Desconhecido"])
                )

                ano = item.get("first_publish_year", "Ano desconhecido")

                resultado_texto.insert(tk.END, f"📖 {titulo}\n")
                resultado_texto.insert(tk.END, f"✍️ Autor: {autores}\n")
                resultado_texto.insert(tk.END, f"📅 Ano: {ano}\n")
                resultado_texto.insert(tk.END, "-" * 40 + "\n")

        except Exception as e:
            resultado_texto.delete(1.0, tk.END)
            resultado_texto.insert(tk.END, f"❌ Erro: {e}")



    janela = tk.Tk()
    janela.title("📚 BookFlow - Busca de Livros")
    janela.geometry("600x500")


    titulo = tk.Label(
        janela,
        text="BookFlow 📚",
        font=("Arial", 18)
    )
    titulo.pack(pady=10)

    entrada = tk.Entry(
        janela,
        width=50,
        font=("Arial", 12)
    )
    entrada.pack(pady=10)

    botao = tk.Button(
        janela,
        text="🔍 Buscar Livro",
        command=buscar_livros
    )
    botao.pack(pady=5)

    resultado_texto = tk.Text(
        janela,
        height=20,
        width=70
    )
    resultado_texto.pack(pady=10)

    janela.mainloop()