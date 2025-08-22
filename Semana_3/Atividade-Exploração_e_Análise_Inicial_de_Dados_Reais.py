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
        *há 1 valor em branco

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
    Apaguei o registro incompleto para uniformidade de dados, usando o "df.dropna", e ficando com 139 registros integros
    
5. Análise dos dados (❌)
    Como o meu dataset escolhido tem várias colunas, para uma melhor precisão irei focar em 3 visualizações dos dados, sendo elas:
        1. Avaliar nivel de estresse, por nivel, através de análise analitica
        

Emojis: ✅ & ❌
-----------------------------------

* Desculpe pela demora na entrega prof, estive ocupado essa semana pelas aulas.

'''
# Bibliotecas
import pandas as pd

# Seção de Importação Inicial

path = r'C:\Users\victo\Python_Senai390\Semana_3\academic_stress_level-maintainance_1.csv'
df = pd.read_csv(path)

# Visualização inicial dos dados:

print("\n", "---"*15, "\n")
print(df.head())
print("\n", "---"*15, "\n")


# Seção de Análise Preliminar:

print("\n", "---"*15, "\n")
print(df.info())
print("\n", "---"*15, "\n")

# Seção Tratamento dos dados:

df_tratado = df.dropna()

# Confirmação do tratamento:

print("\n", "---"*15, "\n")
print(df_tratado.info())
print("\n", "---"*15, "\n")


