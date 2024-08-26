import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime
import pandas as pd

#Página de Login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Aqui você pode adicionar a lógica de autenticação
    if username == "user" and password == "pass":  # Exemplo de validação simples
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos")

def open_signup():
    messagebox.showinfo("Cadastro", "Redirecionando para a página de cadastro...")
    # Aqui você pode adicionar o código para redirecionar para a página de cadastro

# Criação da janela principal
root = tk.Tk()
root.title("Tela de Login")

# Label e campo de entrada para nome de usuário
label_username = tk.Label(root, text="Nome de usuário:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Label e campo de entrada para senha
label_password = tk.Label(root, text="Senha:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botão de login
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=20)

# Mensagem de cadastro
signup_message = tk.Label(root, text="Não possui login? ")
signup_message.pack(side=tk.LEFT, padx=10)

signup_link = tk.Label(root, text="Clique aqui para realizar o seu cadastro", fg="blue", cursor="hand2")
signup_link.pack(side=tk.LEFT, padx=10)

# Associa o clique ao redirecionamento para o cadastro
signup_link.bind("<Button-1>", lambda e: open_signup())


# Página de Cadastro

def validate_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validate_matricula(matricula):
    return matricula.isdigit() and len(matricula) == 6

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def register():
    name = entry_name.get()
    cpf = entry_cpf.get()
    matricula = entry_matricula.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    terms_accepted = var_terms.get()

    if not name:
        messagebox.showerror("Erro", "O nome completo é obrigatório.")
        return
    if not validate_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido. Insira 11 dígitos numéricos.")
        return
    if not validate_matricula(matricula):
        messagebox.showerror("Erro", "Matrícula inválida. Insira exatamente 6 dígitos numéricos.")
        return
    if not validate_password(password):
        messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres, incluindo 1 letra maiúscula, 1 número e 1 caractere especial.")
        return
    if password != confirm_password:
        messagebox.showerror("Erro", "As senhas não coincidem.")
        return
    if not terms_accepted:
        messagebox.showerror("Erro", "Você deve aceitar os termos de uso para se cadastrar.")
        return

    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    # Aqui você pode adicionar o código para salvar as informações do cadastro

# Criação da janela principal
root = tk.Tk()
root.title("Página de Cadastro")

# Campo Nome Completo
label_name = tk.Label(root, text="Nome Completo:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Campo CPF
label_cpf = tk.Label(root, text="CPF:")
label_cpf.pack(pady=5)
entry_cpf = tk.Entry(root)
entry_cpf.pack(pady=5)

# Campo Matrícula AXM Fit
label_matricula = tk.Label(root, text="Matrícula AXM Fit:")
label_matricula.pack(pady=5)
entry_matricula = tk.Entry(root)
entry_matricula.pack(pady=5)

# Campo Senha
label_password = tk.Label(root, text="Senha:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Campo Confirmar Senha
label_confirm_password = tk.Label(root, text="Confirmar Senha:")
label_confirm_password.pack(pady=5)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.pack(pady=5)

# Checkbox para aceitar termos de uso
var_terms = tk.IntVar()
checkbox_terms = tk.Checkbutton(root, text="Aceito os termos de uso", variable=var_terms)
checkbox_terms.pack(pady=10)

# Botão para cadastrar
btn_register = tk.Button(root, text="Cadastrar", command=register)
btn_register.pack(pady=20)

import tkinter as tk
from tkinter import messagebox

# Páginas Iniciais
def open_frequencia():
    messagebox.showinfo("Frequência", "Redirecionando para a página de Frequência.")
    # Aqui você pode adicionar o código para abrir a página de Frequência

def open_cardio():
    messagebox.showinfo("Desempenho Cardio", "Redirecionando para a página de Desempenho Cardio.")
    # Aqui você pode adicionar o código para abrir a página de Desempenho Cardio

def open_musculacao():
    messagebox.showinfo("Desempenho Musculação", "Redirecionando para a página de Desempenho Musculação.")
    # Aqui você pode adicionar o código para abrir a página de Desempenho Musculação

def open_relatorios():
    messagebox.showinfo("Relatórios", "Redirecionando para a página de Relatórios.")
    # Aqui você pode adicionar o código para abrir a página de Relatórios

# Criação da janela principal
root = tk.Tk()
root.title("Página Inicial")

# Botão para Visualizar Frequência
btn_frequencia = tk.Button(root, text="Visualizar Frequência", command=open_frequencia)
btn_frequencia.pack(pady=10)

# Botão para Visualizar Desempenho Cardio
btn_cardio = tk.Button(root, text="Visualizar Desempenho Cardio", command=open_cardio)
btn_cardio.pack(pady=10)

# Botão para Visualizar Desempenho Musculação
btn_musculacao = tk.Button(root, text="Visualizar Desempenho Musculação", command=open_musculacao)
btn_musculacao.pack(pady=10)

# Botão para Gerar Relatórios
btn_relatorios = tk.Button(root, text="Gerar Relatórios", command=open_relatorios)
btn_relatorios.pack(pady=10)

# Página Visualizar Frequência
dados_frequencia = pd.DataFrame({
    'Aluno': ['Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4'],
    'Frequencia Geral': [50, 45, 60, 30],
    'Frequencia Mês Atual': [10, 12, 15, 8]
})

def listar_frequencia(modo):
    # Limpa a listagem anterior
    for widget in listagem_frame.winfo_children():
        widget.destroy()

    if modo == 'mes':
        df_filtrado = dados_frequencia.sort_values(by='Frequencia Mês Atual', ascending=False)
        label_title = tk.Label(listagem_frame, text="Listagem de Frequência - Mês Atual")
    else:
        df_filtrado = dados_frequencia.sort_values(by='Frequencia Geral', ascending=False)
        label_title = tk.Label(listagem_frame, text="Listagem de Frequência - Geral")
    
    label_title.pack()

    for idx, row in df_filtrado.iterrows():
        label = tk.Label(listagem_frame, text=f"{row['Aluno']}: {row[f'Frequencia {modo.capitalize()}']}")
        label.pack()

def listar_mes_atual():
    listar_frequencia('mes')

def listar_geral():
    listar_frequencia('geral')

# Criação da janela principal
root = tk.Tk()
root.title("Visualizar Frequência")

# Botão para listar por mês atual
btn_mes_atual = tk.Button(root, text="Mês Atual", command=listar_mes_atual)
btn_mes_atual.pack(pady=10)

# Botão para listar por geral
btn_geral = tk.Button(root, text="Geral", command=listar_geral)
btn_geral.pack(pady=10)

# Frame para listagem dos alunos
listagem_frame = tk.Frame(root)
listagem_frame.pack(pady=20)

#Página Desempenho Cardio

dados_cardio = pd.DataFrame({
    'Aluno': [''],
    'Distância Geral (km)': [''],
    'Velocidade Geral (km/h)': [''],
    'BPM Geral': [''],
    'Duração Geral (min)': [''],
    'Distância Mês Atual (km)': [''],
    'Velocidade Mês Atual (km/h)': [''],
    'BPM Mês Atual': [''],
    'Duração Mês Atual (min)': ['']
})

def listar_cardio(modo, metrica):
    # Limpa a listagem anterior
    for widget in listagem_frame.winfo_children():
        widget.destroy()

    # Seleção do DataFrame baseado no modo e métrica
    df_filtrado = dados_cardio.sort_values(by=f'{metrica} {modo.capitalize()}', ascending=False)
    
    label_title = tk.Label(listagem_frame, text=f"Listagem de Desempenho Cardio - {modo.capitalize()} ({metrica})")
    label_title.pack()

    for idx, row in df_filtrado.iterrows():
        label = tk.Label(listagem_frame, text=f"{row['Aluno']}: {row[f'{metrica} {modo.capitalize()}']}")
        label.pack()

def listar_mes_atual(metrica):
    listar_cardio('Mês Atual', metrica)

def listar_geral(metrica):
    listar_cardio('Geral', metrica)

def listar_distancia():
    if modo_var.get() == 'mes':
        listar_mes_atual('Distância')
    else:
        listar_geral('Distância')

def listar_velocidade():
    if modo_var.get() == 'mes':
        listar_mes_atual('Velocidade')
    else:
        listar_geral('Velocidade')

def listar_bpm():
    if modo_var.get() == 'mes':
        listar_mes_atual('BPM')
    else:
        listar_geral('BPM')

def listar_duracao():
    if modo_var.get() == 'mes':
        listar_mes_atual('Duração')
    else:
        listar_geral('Duração')

# Criação da janela principal
root = tk.Tk()
root.title("Visualizar Desempenho Cardio")

# Variável para armazenar o modo (Mês Atual ou Geral)
modo_var = tk.StringVar(value='mes')

# Botões de filtro de Modo
btn_mes_atual = tk.Radiobutton(root, text="Mês Atual", variable=modo_var, value='mes')
btn_mes_atual.pack(pady=10)

btn_geral = tk.Radiobutton(root, text="Geral", variable=modo_var, value='geral')
btn_geral.pack(pady=10)

# Botões de filtro de Métrica
btn_distancia = tk.Button(root, text="Distância", command=listar_distancia)
btn_distancia.pack(pady=10)

btn_velocidade = tk.Button(root, text="Velocidade", command=listar_velocidade)
btn_velocidade.pack(pady=10)

btn_bpm = tk.Button(root, text="BPM", command=listar_bpm)
btn_bpm.pack(pady=10)

btn_duracao = tk.Button(root, text="Duração", command=listar_duracao)
btn_duracao.pack(pady=10)

# Frame para listagem dos alunos
listagem_frame = tk.Frame(root)
listagem_frame.pack(pady=20)

# Página Desempenho Musculação
dados_musculacao = pd.DataFrame({
    'Aluno': [''],
    'Exercício': ['Leg Press', 'Cadeira Extensora', 'Rosca Direta', 'Mesa Flexora'],
    'Peso Geral (kg)': [ ],
    'Repetições Geral': [ ],
    'Séries Geral': [ ],
    'Peso Mês Atual (kg)': [ ],
    'Repetições Mês Atual': [ ],
    'Séries Mês Atual': [ ]
})

def listar_musculacao(modo, metrica, exercicio_selecionado):
    # Limpa a listagem anterior
    for widget in listagem_frame.winfo_children():
        widget.destroy()

    # Filtra os dados pelo exercício selecionado
    df_filtrado = dados_musculacao[dados_musculacao['Exercício'] == exercicio_selecionado]

    # Ordena os dados pela métrica selecionada
    df_filtrado = df_filtrado.sort_values(by=f'{metrica} {modo.capitalize()}', ascending=False)

    label_title = tk.Label(listagem_frame, text=f"Listagem de Desempenho Musculação - {modo.capitalize()} ({metrica}) - {exercicio_selecionado}")
    label_title.pack()

    for idx, row in df_filtrado.iterrows():
        label = tk.Label(listagem_frame, text=f"{row['Aluno']}: {row[f'{metrica} {modo.capitalize()}']}")
        label.pack()

def listar_mes_atual(metrica):
    exercicio_selecionado = exercicio_var.get()
    listar_musculacao('Mês Atual', metrica, exercicio_selecionado)

def listar_geral(metrica):
    exercicio_selecionado = exercicio_var.get()
    listar_musculacao('Geral', metrica, exercicio_selecionado)

def listar_peso():
    if modo_var.get() == 'mes':
        listar_mes_atual('Peso')
    else:
        listar_geral('Peso')

def listar_repeticoes():
    if modo_var.get() == 'mes':
        listar_mes_atual('Repetições')
    else:
        listar_geral('Repetições')

def listar_series():
    if modo_var.get() == 'mes':
        listar_mes_atual('Séries')
    else:
        listar_geral('Séries')

# Criação da janela principal
root = tk.Tk()
root.title("Visualizar Desempenho Musculação")

# Variável para armazenar o modo (Mês Atual ou Geral)
modo_var = tk.StringVar(value='mes')

# Botões de filtro de Modo
btn_mes_atual = tk.Radiobutton(root, text="Mês Atual", variable=modo_var, value='mes')
btn_mes_atual.pack(pady=10)

btn_geral = tk.Radiobutton(root, text="Geral", variable=modo_var, value='geral')
btn_geral.pack(pady=10)

# Variável para armazenar o exercício selecionado
exercicio_var = tk.StringVar(value='Leg Press')

# Checkbox para seleção de exercício
frame_exercicios = tk.Frame(root)
frame_exercicios.pack(pady=10)

exercicios = ['Cadeira Extensora', 'Leg Press', 'Polia', 'Mesa Flexora', 'Hammer', 'Rosca Direta']
for exercicio in exercicios:
    tk.Radiobutton(frame_exercicios, text=exercicio, variable=exercicio_var, value=exercicio).pack(anchor='w')

# Botões de filtro de Métrica
btn_peso = tk.Button(root, text="Peso", command=listar_peso)
btn_peso.pack(pady=10)

btn_repeticoes = tk.Button(root, text="Repetições", command=listar_repeticoes)
btn_repeticoes.pack(pady=10)

btn_series = tk.Button(root, text="Séries", command(listar_series))
btn_series.pack(pady=10)

# Frame para listagem dos alunos
listagem_frame = tk.Frame(root)
listagem_frame.pack(pady=20)

# Página Gerar Relatórios

def aplicar_filtros():
    # Coleta as seleções dos filtros
    considerar_frequencia = frequencia_var.get()
    cardio_selecionados = [key for key, var in cardio_vars.items() if var.get()]
    musculacao_selecionados = [key for key, var in musculacao_vars.items() if var.get()]

    # Monta o relatório
    relatorio = "Relatório Gerado:\n\n"
    relatorio += f"Considerar Frequência: {'Sim' if considerar_frequencia else 'Não'}\n"
    if considerar_frequencia:
        relatorio += "Informações de frequência serão consideradas.\n"
    relatorio += "\nCardio Selecionado:\n"
    relatorio += ", ".join(cardio_selecionados) if cardio_selecionados else "Nenhum"
    relatorio += "\n\nMusculação Selecionado:\n"
    relatorio += ", ".join(musculacao_selecionados) if musculacao_selecionados else "Nenhum"

    # Exibe o relatório em uma janela de diálogo
    messagebox.showinfo("Relatório", relatorio)

def limpar_filtros():
    # Reseta todas as seleções
    frequencia_var.set(0)
    for var in cardio_vars.values():
        var.set(False)
    for var in musculacao_vars.values():
        var.set(False)

# Criação da janela principal
root = tk.Tk()
root.title("Gerar Relatórios")

# Pergunta: "Considerar frequência?"
frequencia_label = tk.Label(root, text="Considerar frequência?")
frequencia_label.pack(pady=10)

frequencia_var = tk.IntVar(value=0)
radio_sim = tk.Radiobutton(root, text="Sim", variable=frequencia_var, value=1)
radio_sim.pack(anchor='w')
radio_nao = tk.Radiobutton(root, text="Não", variable=frequencia_var, value=0)
radio_nao.pack(anchor='w')

# Checkbox para "Cardio"
cardio_label = tk.Label(root, text="Cardio")
cardio_label.pack(pady=10)

cardio_vars = {
    "Distância": tk.BooleanVar(),
    "Velocidade": tk.BooleanVar(),
    "BPM": tk.BooleanVar(),
    "Duração": tk.BooleanVar(),
}

for key in cardio_vars:
    tk.Checkbutton(root, text=key, variable=cardio_vars[key]).pack(anchor='w')

# Checkbox para "Musculação"
musculacao_label = tk.Label(root, text="Musculação")
musculacao_label.pack(pady=10)

musculacao_vars = {
    "Peso": tk.BooleanVar(),
    "Repetição": tk.BooleanVar(),
    "Séries": tk.BooleanVar(),
}

for key in musculacao_vars:
    tk.Checkbutton(root, text=key, variable=musculacao_vars[key]).pack(anchor='w')

# Botões de "Aplicar Filtro" e "Limpar"
btn_aplicar = tk.Button(root, text="Aplicar Filtro", command=aplicar_filtros)
btn_aplicar.pack(pady=10)

btn_limpar = tk.Button(root, text="Limpar", command=limpar_filtros)
btn_limpar.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()








