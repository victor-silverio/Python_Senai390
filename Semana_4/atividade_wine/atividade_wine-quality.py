#Nome: Victor Augusto de Aquino Silvério
# atividade wine quality

# Bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# carrega o dataset e muda o separador do csv (padrão ",", mas o wine é ";")
path = r'Semana_4\atividade_wine\data\winequality-red.csv'
df_vinhos = pd.read_csv(path, sep=';')
#Pergunta 1: Usei o pandas pois ele é adequado para dados tabulares, numpy é melhor só para operações matematicas e arrays 'puros'

# Visualização do cabeçalho:

print("\n" + "---"*15 + "\n")
print("cabecalho: \n")
print(df_vinhos.head())
print("\n" + "---"*15 + "\n")

# dimensão do dataset

num_linhas, num_colunas = df_vinhos.shape # fica melhor, e dá pra usar mais tarde as variaveis

print("\n" + "---"*15 + "\n")
print(f"O dataset possui {num_linhas} linhas e {num_colunas} colunas")
print("\n" + "---"*15 + "\n")

#colunas no dataset
print("\n" + "---"*15 + "\n")
print("As colunas do dataset são:")
for coluna in df_vinhos.columns: #aprendi na unifei
    print(f"- {coluna}")
print("\n" + "---"*15 + "\n")

#pergunta 2: Mostra as composições quimicas/fisicas dos vinhos, além de uma 'nota', a coluna quality

print("\n" + "---"*15 + "\n")
media_alcool_pandas = df_vinhos['alcohol'].mean()
print(f"A média do teor alcoólico com Pandas é: {media_alcool_pandas:.2f}")
print("\n" + "---"*15 + "\n")

print("\n" + "---"*15 + "\n")
media_alcool_numpy = np.mean(df_vinhos['alcohol'])
print(f"A média do teor alcoólico com Numpy é: {media_alcool_numpy:.2f}")
print("\n" + "---"*15 + "\n")

print("\n" + "---"*15 + "\n")
print("Os resultados são idênticos.") #vi no terminal e escrevi aqui, preguiça de fazer if & else
print("\n" + "---"*15 + "\n")

#pergunta 3: usaria o pandas, pois ele já está sendo como principal nesse caso de uso. Mas em estruturas completamente de números, o numpy seria mais efetivo (e tem mais funções nesse ambito)

# valores nulos/faltantes:
valores_faltantes = df_vinhos.isnull().sum()

print("\n" + "---"*15 + "\n")
if valores_faltantes.sum() == 0:
    print("Não há valores nulos no dataset.")
else:
    print("Valores faltantes por coluna:")
    print(valores_faltantes)
print("\n" + "---"*15 + "\n")

# pergunta 4: eu prefiro a '.dropna', mas a função de preencher também é util. 

# Graficos solicitados:

#distribuição de "alcohol"
sns.histplot(df_vinhos['alcohol'], kde=True, bins=20)
plt.title('Distribuição do Teor Alcoólico')
plt.xlabel('Teor Alcoólico (em %)')
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.savefig(r'Semana_4\atividade_wine\graficos\distribuicao_alcool.png')
plt.clf()

#relação entre álcool e qualidade do vinho
sns.barplot(x='quality', y='alcohol', data=df_vinhos)
plt.title('Relação entre Qualidade e Teor Alcoólico')
plt.xlabel('Qualidade do Vinho')
plt.ylabel('Média de Teor Alcoólico (em %)')
plt.grid(axis='y')
plt.savefig(r'Semana_4\atividade_wine\graficos\relacao_qualidade_alcool.png')
plt.clf()

#boxplot para verificar outliers no pH
sns.boxplot(y=df_vinhos['pH'])
plt.title('Boxplot do pH')
plt.ylabel('pH')
plt.grid(axis='y')
plt.savefig(r'Semana_4\atividade_wine\graficos\boxplot_ph.png')
plt.clf()

# pergunta 5: sobre os graficos:
'''
O histograma mostra que a maioria dos vinhos tem teor alcoólico de 9% á 11%.
O gráfico de barras mostra que quanto maior o nível de alcool, maior a qualidade.
O boxplot do pH facilita visualizar a mediana, os quartis e identificar os outliers. no caso especifico, deu pra ver 2 outliers, um superior e um inferior.
'''

print("\n" + "---"*15 + "\n")
print("Frequência da variável Qualidade\n")
frequencia_qualidade = df_vinhos['quality'].value_counts().sort_index()
print(frequencia_qualidade)
print("\n" + "---"*15 + "\n")

print("\n" + "---"*15 + "\n")
print("Matriz de Correlação\n")
matriz_correlacao = df_vinhos.corr()
print(matriz_correlacao)
print("\n" + "---"*15 + "\n")

# plotando a matriz de correlação
sns.heatmap(matriz_correlacao, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.savefig(r'Semana_4\atividade_wine\graficos\matriz_correlacao.png')
plt.clf()

# Conclusão

print("como visto anteriormente, um vinho com mais alcool, tem uma qualidade reportada maior.\n")
print("As variaveis que mais impactam positivamente são o alcool, os sulfatos e o acido citrico\n")
print("as variaveis que impactam negativamente são a volatilidade da acides, o total de dioxido de sulfur e a densidade\n")

print("\n" + "---"*15 + "\n")

print("Faz mais sentido usar o numpy para dados puramente numericos e calculos mais complexos\n")
print("O pandas é melhor para dados tambulares (como csv), para limpar dados e explorar e visualizar eles indivualmente pelo dataframe (selecionando colunas). ")
