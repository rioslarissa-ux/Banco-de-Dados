import tkinter as tk
from tkinter import messagebox
import sqlite3

# =====================================
# CONEXÃO COM O BANCO DE DADOS SQLITE
# =====================================

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criar tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
""")

conexao.commit()


# =====================================
# FUNÇÃO PARA SALVAR CLIENTE
# =====================================

def salvar_cliente():

    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validar preenchimento dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar!"
        )
        return

    # Validar formato básico do e-mail
    if "@" not in email or "." not in email:
        messagebox.showwarning(
            "Atenção",
            "Digite um e-mail válido!"
        )
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao cadastrar cliente: {erro}"
        )


# ==========================
import tkinter as tk
from tkinter import messagebox
import sqlite3

# =====================================
# CONEXÃO COM O BANCO DE DADOS SQLITE
# =====================================

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criar tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
""")

conexao.commit()


# =====================================
# FUNÇÃO PARA SALVAR CLIENTE
# =====================================

def salvar_cliente():

    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validar preenchimento dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar!"
        )
        return

    # Validar formato básico do e-mail
    if "@" not in email or "." not in email:
        messagebox.showwarning(
            "Atenção",
            "Digite um e-mail válido!"
        )
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao cadastrar cliente: {erro}"
        )


# =====================================
# FUNÇÃO PARA LIMPAR FORMULÁRIO
# =====================================

def limpar_formulario():

    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# =====================================
# CRIAÇÃO DA INTERFACE GRÁFICA
# =====================================

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("450x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="FORMULÁRIO DE CADASTRO",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Frame do formulário
frame = tk.Frame(janela)
frame.pack(pady=10)

# Campo Nome
tk.Label(
    frame,
    text="Nome:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=10, sticky="e")

entrada_nome = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

# Campo E-mail
tk.Label(
    frame,
    text="E-mail:",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=10, sticky="e")

entrada_email = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_email.grid(row=1, column=1, padx=10, pady=10)

# Campo Telefone
tk.Label(
    frame,
    text="Telefone:",
    font=("Arial", 11)
).grid(row=2, column=0, padx=10, pady=10, sticky="e")

entrada_telefone = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_telefone.grid(row=2, column=1, padx=10, pady=10)

# =====================================
# BOTÕES
# =====================================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
botao_salvar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_formulario,
    bg="gray",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
botao_limpar.grid(row=0, column=1, padx=10)

# Foco inicial
entrada_nome.focus()

# Executar interface
janela.mainloop()

# Fechar conexão ao encerrar
conexao.close()
===========
# FUNÇÃO PARA LIMPAR FORMULÁRIO
# =====================================

def limpar_formulario():

    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# =====================================
# CRIAÇÃO DA INTERFACE GRÁFICA
# =====================================

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("450x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="FORMULÁRIO DE CADASTRO",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Frame do formulário
frame = tk.Frame(janela)
frame.pack(pady=10)

# Campo Nome
tk.Label(
    frame,
    text="Nome:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=10, sticky="e")

entrada_nome = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

# Campo E-mail
tk.Label(
    frame,
    text="E-mail:",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=10, sticky="e")

entrada_email = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_email.grid(row=1, column=1, padx=10, pady=10)

# Campo Telefone
tk.Label(
    frame,
    text="Telefone:",
    font=("Arial", 11)
).grid(row=2, column=0, padx=10, pady=10, sticky="e")

entrada_telefone = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
entrada_telefone.grid(row=2, column=1, padx=10, pady=10)

# =====================================
# BOTÕES
# =====================================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
botao_salvar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_formulario,
    bg="gray",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
botao_limpar.grid(row=0, column=1, padx=10)

# Foco inicial
entrada_nome.focus()

# Executar interface
janela.mainloop()

# Fechar conexão ao encerrar
conexao.close()
