'''
Nome: Victor Augusto

Atividade: Analisando o famoso dataset Iris
Data Ínicio: 16/08 - 02:12

Objetivos: 

1. Qual é a média (por espécie) de cada medida (sepal/petal, comprimento/largura)? ✅
2. Qual é o desvio padrão de cada variável por espécie? ✅
3. Quantas observações existem por espécie? (contagem de instâncias) ✅
4. Qual é o valor mínimo e máximo (amplitude) das medidas por espécie para saber a dispersão? ✅
5. Qual é a média geral (sem agrupamento) das variáveis — comparando contexto geral e por espécie? ✅

"✅" / "❌" (To salvando aqui pra usar como demarcação de progresso)
'''

import pandas as pd
import io

path = r'C:\Users\victo\Python_Senai390\Semana_2\iris.csv' #path só pra ficar bonitinho

df = pd.read_csv(path)

# Analises:

agrupado_especies = df.groupby('species') #Aqui, eu agrupo por especies

# Média por espécie (1)

media_especies = agrupado_especies.mean()

# Desvio padrão (2)

desvio_especies = agrupado_especies.std()

# Contagem por especie (3)

contagem_especies = agrupado_especies.size()

# Valor Min & Max (4)

Min_especies = agrupado_especies.min()
Max_especies = agrupado_especies.max()

# Media geral (5)

#Como é a visão geral das variaveis, precisamos separar por elas

colunas_variaveis = df.select_dtypes(include=['number'])

# E após isso, fazemos a média geral:

media_geral = colunas_variaveis.mean()

# Impressões:

print("Iniciando analises: ")

print ("\n", "=+=+=+="*10, "\n") #Separador bonitinho que aprendi a fazer

print("Cabeçalho do database: ")
print(df.head())

print ("\n", "=+=+=+="*10, "\n")

print("Informações gerais do database: ")
print(df.info())

print("\n", "=+=+=+="*10, "\n")

print("Análises específicas: ")

print("Analise 1: ")

print(media_especies)

print("\n", "=+=+=+="*10, "\n")

print("Analise 2: ")

print(desvio_especies)

print("\n", "=+=+=+="*10, "\n")

print("Analise 3: ")

print(contagem_especies)

print("\n", "=+=+=+="*10, "\n")

print("Analise 4: ")

print(Min_especies)
print(Max_especies)

print("\n", "=+=+=+="*10, "\n")

print("Analise 5: ")

print(media_geral)

print("\n", "=+=+=+="*10, "\n")