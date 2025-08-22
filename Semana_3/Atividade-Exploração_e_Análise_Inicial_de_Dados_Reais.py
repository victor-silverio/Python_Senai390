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
    1. Apaguei o registro incompleto para uniformidade de dados, usando o "df.dropna", e ficando com 139 registros integros. (✅)
    2. Além disso, notei que os nomes das colunas apresentam espaços, aspas, e outras incongruencias e são grandes demais, para melhorar isso, irei renomear as colunas. (✅)
        (Para facilitar minha vida, vou manter em inglês)
    3. Irei excluir as colunas inutilizadas para as minhas analises. (De certa forma é economia de recursos, mas, na escala atual é só para melhor organização msm) (✅)
        
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
import matplotlib.pyplot as plt

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

df_tratado = df.dropna() # Limpa valores nulos

df_tratado_1 = df_tratado.rename(columns={ # Renomeia colunas

    'Timestamp': 'timestamp',
    'Your Academic Stage': 'academic_stage', # Em uso
    'Peer pressure': 'pressure_schoolmates', 
    'Academic pressure from your home': 'pressure_family',
    'Study Environment': 'study_environment', # Em uso
    'What coping strategy you use as a student?': 'coping_strategy', 
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'bad_habits',
    'What would you rate the academic  competition in your student life': 'academic_competition', # Em uso
    'Rate your academic stress index ': 'stress' # Em uso
    #'': '',
})

# Removendo as colunas inutilizadas na minha analise.

df_final = df_tratado_1.drop(['timestamp', 'pressure_schoolmates', 'pressure_family', 'coping_strategy', 'bad_habits'], axis=1)

# Confirmação do tratamento:

print("\n", "---"*15, "\n")
print(df_final.info())
print("\n", "---"*15, "\n")

# Seção 5:
# Seção 5.1:
# Análise 1:
# 1. Avaliar nivel de estresse academico relatado, por nivel academico, através de análise análitica
# Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível academico e sua distribuição, e além disso um gráfico mostrando a média de cada área.

# Seção 5.1.1 - Analises de tendencia central e dispersão
# Inicialmente, iremos realizar somente os calculos filtrados por niveis academicos:

media_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].mean()
moda_estresse_nivel_academico = df_final.groupby('academic_stage')['stress'].apply(lambda x: x.mode()[0])
mediana_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].median()
variancia_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].var()
desvio_padrao_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].std()
amplitude_estresse_nivel_academico = ( df_final.groupby('academic_stage')[['stress']].max() - df_final.groupby('academic_stage')[['stress']].min() )

# Exibindo os dados:

print("\n", "---"*15, "\n")
print(f"A média de estresse por nível academico é: \n\n{media_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A moda de estresse por nível academico é: \n\n{moda_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A mediana de estresse por nível academico é: \n\n{mediana_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A variancia de estresse por nível academico é: \n\n{variancia_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"O desvio padrão de estresse por nível academico é: \n\n{desvio_padrao_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A amplitude de estresse por nível academico é: \n\n{amplitude_estresse_nivel_academico}")
print("\n", "---"*15, "\n")

# Agora com os calculos realizados, vamos fazer uns graficos através do matplotlib. Inicialmente os de dispersão de dados via grafico de colunas de cada nivel academico, depois a media dos 3.

# Os demais dados serão tratados de forma escrita no relatório

# Seção 5.1.2 - Graficos por nivel academico

# Seção 5.1.2.1 - HIGH-SCHOOL

# Filtramos pelo ensino medio
estresse_highschool = df_final[df_final['academic_stage'] == 'high school']['stress'].value_counts().sort_index()

# Grafico
plt.bar(estresse_highschool.index, estresse_highschool.values)

#Embelezamento do grafico:
plt.title("Distribuição do nível de estresse - Ensino Médio")
plt.xlabel("Nivel de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y') # Aqui mostro a linha do grid no eixo y para melhor visualizacao do grafico
plt.xticks([0, 1, 2, 3, 4, 5]) # Aqui defino a separação do eixo x; Não da pra definir um unico para o y pois os a qtd de dados variam pelo nivel academico, mas a escala no eixo x sempre é a mesma. obs: não há nenhum dado com valor 0, porém, listei ele para ficar mais bonito o grafico.
plt.tight_layout()
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_ensino_medio.png') # Como vou fazer vários graficos, não da pra mostrar todos ao mesmo tempo, tenho que salvar um por um, depois vou só adicionar as imagens no relatório em markdown
plt.clf() #Limpando para o proximo grafico

# Seção 5.1.2.2 - undergraduate

estresse_undergraduate = df_final[df_final['academic_stage'] == 'undergraduate']['stress'].value_counts().sort_index()

# Grafico
plt.bar(estresse_undergraduate.index, estresse_undergraduate.values)

#Embelezamento do grafico:
plt.title("Distribuição do nível de estresse - Graduação")
plt.xlabel("Nivel de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_graduação.png')
plt.clf()

# Seção 5.1.2.3 - post-graduate

estresse_postgraduate = df_final[df_final['academic_stage'] == 'post-graduate']['stress'].value_counts().sort_index()

# Grafico
plt.bar(estresse_postgraduate.index, estresse_postgraduate.values)

#Embelezamento do grafico:
plt.title("Distribuição do nível de estresse - Pós Graduação")
plt.xlabel("Nivel de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_pos_graduação.png')
plt.clf()

# Seção 5.1.3.1 - Grafico geral dos 3 niveis academicos
media_estresse_niveis = df_final.groupby('academic_stage')['stress'].mean().sort_values(ascending=False)

'''

DEVIDO A MÉDIA ENTRE OS 3 SEREM PROXIMAS, UM GRAFICO NORMAL FICA DIFICIL A VISUALIZAÇÃO DA DIFERENÇA, POR ISSO FIZ UM "SEM ZOOM", E UM "COM ZOOM"

'''

# Seção 5.1.3.1.1 - Grafico sem zoom
plt.bar(media_estresse_niveis.index, media_estresse_niveis.values)

#Embelezamento do grafico:
plt.title("Média de Nível de estresse por estágio academico")
plt.xlabel("Estagio Academico")
plt.ylabel("Média de estresse")
plt.grid(axis='y')
plt.ylim(0, 5)
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\media_estresse_niveis.png')
plt.clf()

# Seção 5.1.3.1.2 - Grafico sem zoom
plt.bar(media_estresse_niveis.index, media_estresse_niveis.values)

#Embelezamento do grafico:
plt.title("Média de Nível de estresse por estágio academico")
plt.xlabel("Estagio Academico")
plt.ylabel("Média de estresse")
plt.grid(axis='y')
plt.ylim(3, 4)
plt.yticks([3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0])
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\media_estresse_niveis_zoom.png')
plt.clf()