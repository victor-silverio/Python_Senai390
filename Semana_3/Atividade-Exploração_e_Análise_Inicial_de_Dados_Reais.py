'''
Nome: Victor Augusto de Aquino Silvério
Atividade: Exploração e Análise Inicial de Dados Reais

Dataset escolhido: https://www.kaggle.com/datasets/poushal02/student-academic-stress-real-world-dataset

O dataset consiste em 9 colunas, e cada uma delas armazena um tipo de dado, sendo eles:

1. Timestamp
    Salva data e hora, no formato:
        DD/MM/YYYY HH:MM:SS

2. Your Academic Stage
    Armazena o nível academico atual do participante, variando de:
        undergraduate
        high school
        post-graduate

3. Peer pressure
    Armazena a escala relatada de pressão pelos colegas
        Varia de 1 até 5

4. Academic pressure from your home
    Armazena a escala relatada de pressão vinda de casa
        Varia de 1 até 5

5. Study Environment
    Armazena a avaliação do ambiente de estudo, variando de:
        Noisy
        Peaceful
        disrupted
        *há 1 valor em branco (Necessita de tratamento)

6. What coping strategy you use as a student?
    Armazena o relato do estudante de como lida com o estresse, variando de:
        Analyze the situation and handle it with intellect
        Social support (friends, family)
        Emotional breakdown (crying a lot)

7. Do you have any bad habits like smoking, drinking on a daily basis?
    Armazena os hábitos ruins relatados pelos estudantes, variando de:
        No
        prefer not to say
        Yes

8. What would you rate the academic  competition in your student life
    Armazena o valor relatado da competição academica na vida dele
        Varia de 1 até 5

9. Rate your academic stress index
    Armazena o indice de estresse relatado pelo estudante
        Varia de 1 até 5

-----------------------------------
--- Plano de Ação --- 

1. Carregar Arquivos (✅)
    Baixei através de outro script e minha apikey, o scrip está disponivel na mesma pasta nomeado como "Download.py", mas, para sua execução é necessário uma apikey valida.

2. Visualização inicial dos dados (✅)
    Usei o "df.head"

3. Avaliar informações e variações (✅)
    Através do comando "df.info", pude notar que há uma inconsistencia nos dados (Em somente uma linha). Então para isso, irei deletar ela para uma maior uniformidade.
    
4. Tratamento dos dados (✅)
    1. Apaguei o registro incompleto para uniformidade de dados, usando o "df.dropna", e ficando com 139 registros integros.
    2. Além disso, notei que os nomes das colunas apresentam espaços e são grandes demais, para melhorar isso, irei renomear as colunas. (Para facilitar minha vida, vou manter em inglês)
    3. Irei excluir as colunas inutilizadas para as minhas analises. (De certa forma é economia de recursos, mas, na escala atual é só para melhor organização msm)
        
5. Análise dos dados (❌)
    Como o meu dataset escolhido tem várias colunas, para uma melhor precisão irei focar em 3 visualizações dos dados, sendo elas:
        1. Avaliar nivel de estresse academico relatado, por nivel academico, através de análise análitica (❌)
            Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível academico e sua distribuição, e além disso um gráfico mostrando a média de cada área.
        
        2. Avaliar se o stress academico relatado tem relação com a competição academica relatada. (❌)
            Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
            
        3. Avaliar se o ambiente de estudo é diretamente relatado ao nivel de estresse (❌)
            Pré processamento: Para uma melhor avaliação, vou converter o ambiente de texto (object), para um variavel escalar (Inteira, de 1 a 3), pois só há 3 variações.
            Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacificos são ligados á estresses relatados como baixo (1 ou 2, na escala), e se, ambientes ruins geram nivéis de estresse maiores. 

    Com essas 3 abordagens, espero trazer uma ampla visão do dataset, abordando ele de diversas maneiras.

Emojis: ✅ & ❌
-----------------------------------
Observações:

* Desculpe pela demora na entrega prof, estive ocupado essa semana pelas aulas.

* To tentando mudar a minha organização de código para scripts maiores, essa vai ser a minha primeira vez fazendo isso em python, então pode ficar meio cheio de comentarios.

* Se tiver faltando acentos nas palavras é porque o vscode não corrige acentuação ainda (eu não tenho uma extensão para isso, nem sei se existe)

'''
# Bibliotecas
import pandas as pd

# Seção 1:
# Seção de Importação Inicial

path = r'C:\Users\victo\Python_Senai390\Semana_3\academic_stress_level-maintainance_1.csv'
df = pd.read_csv(path)

# Seção 2:
# Visualização inicial dos dados:

print("\n", "---"*15, "\n")
print(df.head())
print("\n", "---"*15, "\n")

# Seção 3:
# Análise Preliminar:

print("\n", "---"*15, "\n")
print(df.info())
print("\n", "---"*15, "\n")

# Seção 4:
# Tratamento dos dados:

df_tratado = df.dropna()
df_tratado_1 = df_tratado.rename(colums={
    'Your Academic Stage': 'academic_stage',
    'Peer pressure': 'pressure_schoolmates',
    ''
    
    
})

# Confirmação do tratamento:

print("\n", "---"*15, "\n")
print(df_tratado.info())
print("\n", "---"*15, "\n")

# Seção 5:
# Análise 1:
# 1. Avaliar nivel de estresse academico relatado, por nivel academico, através de análise análitica
# Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível academico e sua distribuição, e além disso um gráfico mostrando a média de cada área.

media_estresse_ensino_medio = df_tratado.groupby('')