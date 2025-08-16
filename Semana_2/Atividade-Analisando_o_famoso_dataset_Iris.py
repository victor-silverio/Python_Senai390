'''
Nome: Victor Augusto

Atividade: Analisando o famoso dataset Iris
Data Ínicio: 16/08 - 02:12

Objetivos: 

Qual é a média (por espécie) de cada medida (sepal/petal, comprimento/largura)?
Qual é o desvio padrão de cada variável por espécie?
Quantas observações existem por espécie? (contagem de instâncias)
Qual é o valor mínimo e máximo (amplitude) das medidas por espécie para saber a dispersão?
Qual é a média geral (sem agrupamento) das variáveis — comparando contexto geral e por espécie?

'''

import pandas as pd

path = r'C:\Users\victo\Python_Senai390\Semana_2\iris.csv'

df = pd.read_csv(path)

print(df.head())