import tkinter as tk
from tkinter import messagebox

#Principais funções:
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa != "":
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa antes de adicionar!")

def remover_tarefa():
    try:
        selecionada = lista_tarefas.curselection()[0]
        lista_tarefas.delete(selecionada)
    except:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def limpar_tarefas():
    lista_tarefas.delete(0, tk.END)

#Principal janela:
janela = tk.Tk()
janela.title("To-Do List 📝")
janela.geometry("400x400")
janela.config(bg="#EAF6FF")

#Título:
titulo = tk.Label(janela, text="To-Do List", font=("Arial", 16, "bold"), bg="#EAF6FF")
titulo.pack(pady=10)

#Entradas:
entrada_tarefa = tk.Entry(janela, width=30, font=("Arial", 12))
entrada_tarefa.pack(pady=5)

#Botões:
frame_botoes = tk.Frame(janela, bg="#EAF6FF")
frame_botoes.pack(pady=10)

btn_add = tk.Button(frame_botoes, text="Adicionar", width=10, command=adicionar_tarefa, bg="#A2D2FF")
btn_add.grid(row=0, column=0, padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover", width=10, command=remover_tarefa, bg="#FFC8DD")
btn_remover.grid(row=0, column=1, padx=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar Tudo", width=10, command=limpar_tarefas, bg="#BDE0FE")
btn_limpar.grid(row=0, column=2, padx=5)

#Tarefas:
lista_tarefas = tk.Listbox(janela, width=45, height=15, font=("Arial", 10))
lista_tarefas.pack(pady=10)

#Executar janela:
janela.mainloop()
