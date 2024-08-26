import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('caminho/para/dados_alunos.csv')

# Gráfico 1: Frequência total por aluno
frequencia_total = df.groupby('nome_completo')['frequencia'].sum()
plt.figure(figsize=(12, 6))
frequencia_total.plot(kind='bar', color='skyblue')
plt.title('Frequência Total por Aluno')
plt.xlabel('Nome Completo')
plt.ylabel('Frequência (nº de dias)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico 2: Distribuição dos Minutos de Cardio
plt.figure(figsize=(10, 6))
plt.hist(df['minutos_cardio'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribuição dos Minutos de Cardio')
plt.xlabel('Minutos de Cardio')
plt.ylabel('Frequência')
plt.show()

# Gráfico 3: Boxplot da Velocidade Máxima de Cardio por Aluno
plt.figure(figsize=(12, 6))
df.boxplot(column='velocidade_max_cardio', by='nome_completo', grid=False, patch_artist=True)
plt.title('Boxplot da Velocidade Máxima de Cardio por Aluno')
plt.suptitle('')
plt.xlabel('Nome Completo')
plt.ylabel('Velocidade Máxima (m/s)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico 4: Média de Peso em Musculação por Aluno
peso_medio = df.groupby('nome_completo')['peso_musculacao'].mean()
plt.figure(figsize=(12, 6))
peso_medio.plot(kind='barh', color='coral')
plt.title('Média de Peso em Musculação por Aluno')
plt.xlabel('Peso Médio (kg)')
plt.ylabel('Nome Completo')
plt.tight_layout()
plt.show()

# Gráfico 5: Dispersão - Distância Percorrida vs Minutos de Cardio
plt.figure(figsize=(10, 6))
plt.scatter(df['minutos_cardio'], df['distancia_cardio'], color='purple')
plt.title('Dispersão: Distância Percorrida vs Minutos de Cardio')
plt.xlabel('Minutos de Cardio')
plt.ylabel('Distância Percorrida (metros)')
plt.show()