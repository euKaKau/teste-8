from carro import Carro
from trem import Trem
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista de objetos cadastrados
lista = []

# Função de criação de objetos
def CadastrodeVeiculo():
    marca = entryMarca.get()
    modelo = entryModelo.get()
    ano = entryAno.get()
    tipo = varTipo.get()
    portas = entryNportas.get()

    if modelo == "":
        messagebox.showinfo("Erro", "Modelo deve ser preenchido")
        return
    if not ano.isdigit():
        messagebox.showinfo("Erro", "Ano deve conter apenas números")
        return

    if tipo == "Carro":
        c = Carro(modelo, marca, ano, portas)
        salvar(c)
    else:
        t = Trem(modelo, marca, ano, portas)
        salvar(t)
    
    messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso")
    atualizaListabox()

def salvar(obj):
    lista.append(obj)

def atualizaListabox():
    listbox.delete(0, tk.END)
    for obj in lista:
        if hasattr(obj, "mostrar"):
            listbox.insert(tk.END, obj.mostrar())
        else:
            listbox.insert(tk.END, str(obj))

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de veículos")
janela.geometry("500x300")

# Notebook
janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

# Abas
tab1 = ttk.Frame(janelinha)
tab2 = ttk.Frame(janelinha)
janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista")

# Widgets da aba 1 (Cadastro)
labels_text = ["Marca:", "Modelo:", "Ano:", "N de Portas/Vagões:"]
entries = []
for i, text in enumerate(labels_text):
    tk.Label(tab1, text=text, font=("", 15)).grid(row=i, column=0, sticky="w", padx=10)
    entry = tk.Entry(tab1, font=("", 15))
    entry.grid(row=i, column=1, sticky="nsew", padx=10, pady=5)
    entries.append(entry)

entryMarca, entryModelo, entryAno, entryNportas = entries

tk.Label(tab1, text="Tipo:", font=("", 15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Carro")
tk.Radiobutton(tab1, text="Carro", font=("", 15), variable=varTipo, value="Carro").grid(row=4, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Trem", font=("", 15), variable=varTipo, value="Trem").grid(row=4, column=1, sticky="e", padx=10)

tk.Button(tab1, text="Cadastrar", font=("", 15), command=CadastrodeVeiculo).grid(row=5, columnspan=2)

# Widgets da aba 2 (Lista)
listbox = tk.Listbox(tab2, font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizaListabox).grid(row=1, column=0)

janela.mainloop()
