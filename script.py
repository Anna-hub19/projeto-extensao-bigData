# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
# Suponha que os dados estejam em um arquivo CSV chamado "dados_socioeconomicos.csv"
# O CSV contém colunas como: 'Nome', 'Idade', 'Gênero', 'Renda', 'Escolaridade', 'Bairro'
dados = pd.read_csv('dados_socioeconomicos.csv')

# 2. Tratar os dados
# Verificar se há valores ausentes
print("Dados ausentes por coluna:")
print(dados.isnull().sum())

# Preencher valores ausentes ou remover linhas/colunas dependendo do caso
dados.dropna(inplace=True)  # Remove linhas com valores ausentes

# Corrigir possíveis inconsistências, como espaços extras ou capitalização inconsistente
dados['Bairro'] = dados['Bairro'].str.strip().str.title()  # Remove espaços e padroniza

# 3. Análise e visualizações
# Exemplo 1: Distribuição da Renda
plt.figure(figsize=(10, 6))
sns.histplot(dados['Renda'], kde=True, bins=20)
plt.title('Distribuição da Renda na Comunidade')
plt.xlabel('Renda (R$)')
plt.ylabel('Frequência')
plt.savefig('distribuicao_renda.png')  # Salva o gráfico como arquivo
plt.show()

# Exemplo 2: Renda média por escolaridade
plt.figure(figsize=(10, 6))
renda_por_escolaridade = dados.groupby('Escolaridade')['Renda'].mean().sort_values()
renda_por_escolaridade.plot(kind='bar', color='skyblue')
plt.title('Renda Média por Nível de Escolaridade')
plt.xlabel('Escolaridade')
plt.ylabel('Renda Média (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('renda_escolaridade.png')
plt.show()

# Exemplo 3: Distribuição de Gênero
plt.figure(figsize=(8, 6))
sns.countplot(x='Gênero', data=dados, palette='Set2')
plt.title('Distribuição de Gênero na Comunidade')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.savefig('distribuicao_genero.png')
plt.show()

# Exemplo 4: Renda por Bairro
plt.figure(figsize=(12, 6))
renda_por_bairro = dados.groupby('Bairro')['Renda'].mean().sort_values()
renda_por_bairro.plot(kind='barh', color='lightgreen')
plt.title('Renda Média por Bairro')
plt.xlabel('Renda Média (R$)')
plt.ylabel('Bairro')
plt.tight_layout()
plt.savefig('renda_bairro.png')
plt.show()

# 4. Salvar o dataset tratado
dados.to_csv('dados_socioeconomicos_tratados.csv', index=False)

print("Análise completa. Arquivos e gráficos gerados com sucesso!")