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

Obs: Desenvolvi em .py, mas irei postar em notebook .ipynb também, pois aí dá pra ver o output sem executar.
'''

import pandas as pd

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
'''
Aqui, separei as impressões, e adicionei mais algumas, por isso o output geral vai ser um pouco maior que o esperado.
'''

print("Iniciando analises: ")

print ("\n", "=+=+=+="*10, "\n") #Separador bonitinho que aprendi a fazer

print("Cabeçalho do database: ")
print(df.head())

print ("\n", "=+=+=+="*10, "\n")

print("Informações gerais do database: ")
print(df.info())

print("\n", "=+=+=+="*10, "\n")

print("Análises específicas: \n")

print("---- Análise 1 ----")
print("Média por espécie de cada uma das medidas:")

print(media_especies)

print("\n", "---"*15, "\n")

print("Através dessa análise, podemos extrair que, a média de tamanho (comprimento) sepal das espécies varia de ~5 até ~6,6, e sua largura varia de ~2,7 até ~3,4. Já o comprimeinto petal, varia de ~1,4 até 5,5, e sua largura de 0,2 até 2,0. Descobrindo assim, que existe uma variação entre espécies, e ela não é mínima.")

print("\n", "=+=+=+="*10, "\n")

print("---- Análise 2 ----")
print("Desvio padrão por espécie:")

print(desvio_especies)

print("\n", "---"*15, "\n")

print("O desvio padrão, mostra a dispersão dos dados em relação à média, e através da análise, podemos notar que: A espécie setosa, apresenta a menor variação na largura/comprimento de suas pétalas, sendo mais uniforme. a espécie virginica, possui uma maior variação que a setosa, e assim podemos extrair que, ela possui uma maior diversidade de tamanho que as setosas.")

print("\n", "=+=+=+="*10, "\n")

print("---- Análise 3 ----")
print("Contagem de observações por espécie:")

print(contagem_especies)

print("\n", "---"*15, "\n")

print("")

print("\n", "=+=+=+="*10, "\n")

print("---- Análise 4 ----")
print("Valores Mínimos e Máximos por Espécie:")

print(Min_especies)
print("---"*25)
print(Max_especies)

print("\n", "---"*15, "\n")

print("")

print("\n", "=+=+=+="*10, "\n")

print("---- Análise 5 ----")
print("Média geral das variáveis:")

print(media_geral)

print("\n", "---"*15, "\n")

print("")

print("\n", "=+=+=+="*10, "\n")