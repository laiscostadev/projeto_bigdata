import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('caminho/para/dados_alunos.csv')

# Visualizar as primeiras linhas do DataFrame
print("Visualizando as primeiras linhas do DataFrame:")
print(df.head())

# Verificar informações gerais sobre os dados
print("\nInformações gerais sobre os dados:")
print(df.info())

# Descrever as estatísticas básicas das colunas numéricas
print("\nEstatísticas descritivas das colunas numéricas:")
print(df.describe())

# Agrupar os dados por nome e somar os minutos de exercício de cardio
print("\nTotal de minutos de exercício de cardio por aluno:")
cardio_total = df.groupby('nome_completo')['minutos_cardio'].sum()
print(cardio_total)

# Agrupar os dados por nome e somar a quantidade de dias de frequência
print("\nFrequência total por aluno:")
frequencia_total = df.groupby('nome_completo')['frequencia'].sum()
print(frequencia_total)

# Agrupar os dados por nome e calcular a média de peso em musculação
print("\nMédia de peso em musculação por aluno:")
peso_medio = df.groupby('nome_completo')['peso_musculacao'].mean()
print(peso_medio)

# Filtrar alunos que percorreram mais de 5 km em algum dia
print("\nAlunos que percorreram mais de 5 km em algum dia de cardio:")
alunos_mais_5km = df[df['distancia_cardio'] > 5000]
print(alunos_mais_5km[['nome_completo', 'distancia_cardio']])

# Salvar o resultado de agrupamentos em um novo arquivo CSV
agrupamento = df.groupby('nome_completo').agg({
    'frequencia': 'sum',
    'minutos_cardio': 'sum',
    'peso_musculacao': 'mean'
}).reset_index()

agrupamento.to_csv('caminho/para/agrupamento_alunos.csv', index=False)
print("\nAgrupamento de dados salvo em 'agrupamento_alunos.csv'")