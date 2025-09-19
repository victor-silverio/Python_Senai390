"""
nome: Victor Augusto de Aquino Silvério
atividade: Análise de Dados de Web Scraping com Pandas

Este script carrega os dados dos livros extraídos com o scrapy, e realiza uma análise 
"""

# bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o csv
path = r'Semana_6\livraria\livros.csv'
df_livros = pd.read_csv(path)

print("\n" + "---"*15 + "\n")
print("cabeçalho do dataset\n")
print(df_livros.head())
print("\n" + "---"*15 + "\n")

# como o preço tem o simbolo do euro, vou apagar para tratar eles como numero (float)
df_livros['preco'] = df_livros['preco'].str.replace('£', '').astype(float)

print("\n" + "---"*15 + "\n")
print("informações do dataset\n")
df_livros.info()
print("\n" + "---"*15 + "\n")


# preço médio
preco_medio = df_livros['preco'].mean()
print("\n" + "---"*15 + "\n")
print(f"O preço médio dos livros é de £{preco_medio:.2f}")
print("\n" + "---"*15 + "\n")

# livro mais caro:
livro_mais_caro = df_livros.loc[df_livros['preco'].idxmax()]
print("\n" + "---"*15 + "\n")
print("As informações do livro mais caro são:\n")
print(livro_mais_caro)
print("\n" + "---"*15 + "\n")

# livros em estoque e fora de estoque
contagem_disponibilidade = df_livros['disponibilidade'].value_counts()

print("disponibilidade\n")
print(contagem_disponibilidade)
print("\n" + "---"*15 + "\n")

# histograma dos preços
sns.histplot(df_livros['preco'], bins=20, kde=True)
plt.title('Distribuição dos Preços dos Livros')
plt.xlabel('Preço (em £(euro))')
plt.ylabel('Frequência (Qtd)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(r'Semana_6\graficos\distribuicao_precos.png')
plt.clf()

print("\n" + "---"*15 + "\n")
print("Na visualização do grafico, podemos notar que os preços são bem diversos, e que o preço mais comum é 25 euros, e a faixa é de 10 euros até 55 euros ")
print("\n" + "---"*15 + "\n")