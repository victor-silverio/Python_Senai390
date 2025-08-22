'''
Nome: Victor Augusto de Aquino Silvério
Atividade: Exploração e Análise Inicial de Dados Reais

Dataset escolhido: https://www.kaggle.com/datasets/poushal02/student-academic-stress-real-world-dataset

O dataset consiste em 9 colunas, e cada uma delas armazena um tipo de dado, sendo eles:

1. Timestamp
    Salva data e hora, no formato:
        DD/MM/YYYY HH:MM:SS

2. Your Academic Stage
    Armazena o nível acadêmico atual do participante, variando de:
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
        *há 1 valor em branco (Precisa de tratamento)

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
    Armazena o valor relatado da competição acadêmica na vida dele
        Varia de 1 até 5

9. Rate your academic stress index
    Armazena o índice de estresse relatado pelo estudante
        Varia de 1 até 5

-----------------------------------
--- Plano de Ação --- 

1. Carregar Arquivos (✅)
    Baixei através de outro script e minha apikey, o scrip está disponível na mesma pasta nomeado como "Download.py", mas, para sua execução é necessário uma apikey valida.

2. Visualização inicial dos dados (✅)
    Usei o "df.head"

3. Avaliar informações e variações (✅)
    Através do comando "df.info", pude notar que há uma inconsistência nos dados (Em somente uma linha). Então para isso, irei deletar ela para uma maior uniformidade.
    
4. Tratamento dos dados (✅)
    1. Apaguei o registro incompleto para uniformidade de dados, usando o "df.dropna", e ficando com 139 registros íntegros. (✅)
    2. Além disso, notei que os nomes das colunas apresentam espaços, aspas, e outras incongruências e são grandes demais, para melhorar isso, irei renomear as colunas. (✅)
        (Para facilitar minha vida, vou manter em inglês)
    3. Irei excluir as colunas inutilizadas para as minhas analises. (De certa forma é economia de recursos, mas, na escala atual é só para melhor organização msm) (✅)
    4. Realizar a conversão de valores na coluna "study_environment" de valores textuais (objects) para valores numéricos (int). (✅)
        Motivo: O texto que define o ambiente de estudos impede a criação de um gráfico de dispersão, que irei realizar na analise 3, então para isso irei converter para uma escala de 1 a 3, representando 1 o ambiente Peaceful, 2 o ambiente Noisy e 3 o ambiente disrupted.
        
5. Análise dos dados (EM ANDAMENTO)
    Como o meu dataset escolhido tem várias colunas, para uma melhor precisão irei focar em 3 visualizações dos dados, sendo elas:
        1. Avaliar nível de estresse acadêmico relatado, por nível acadêmico, através de análise analítica (✅)
            Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível acadêmico e sua distribuição, e além disso um gráfico mostrando a média de cada área.
        
        2. Avaliar se o stress acadêmico relatado tem relação com a competição acadêmica relatada. (✅)
            Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
            
        3. Avaliar se o ambiente de estudo é diretamente relatado ao nível de estresse (❌)
            Pré processamento: Para uma melhor avaliação, vou converter o ambiente de texto (object), para um variável escalar (Inteira, de 1 a 3), pois só há 3 variações. (✅ - Realizado no tratamento de dados)
            Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacíficos são ligados á estresses relatados como baixo (1 ou 2, na escala), e se, ambientes ruins geram níveis de estresse maiores. 

    Com essas 3 abordagens, espero trazer uma ampla visão do dataset, abordando ele de diversas maneiras.

Emojis: ✅ & ❌
-----------------------------------
Observações:

* Desculpe pela demora na entrega prof, estive ocupado essa semana pelas aulas.

* To tentando mudar a minha organização de código para scripts maiores, essa vai ser a minha primeira vez fazendo isso em python, então pode ficar meio cheio de comentários. Em c++/cpp que é onde programo com mais frequência, a estrutura é diferente. 

* Se tiver faltando acentos nas palavras é porque o vscode não corrige acentuação nos comentários ainda (eu não tenho uma extensão para isso, nem sei se existe) edit: Consegui uma extensão, e arrumei todos os acentos.

* Talvez eu tenha excedido o conteúdo e o nível ensinado em sala de aula até o momento, pois aprendi algumas manipulações novas e outras maneiras de se analisar um conjunto de dados por conta própria. 

* Programei todo o código como uma analise pontual do dataset, então, ele segue uma sequencia de funcionamento direta, sem "retornos" ou "avanços"

'''
# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

# Trocando os valores textuais (object), para valores numéricos:

mapeamento_novo_ambiente = {
    'Peaceful': 1,
    'Noisy': 2,
    'disrupted': 3   
}

df_tratado_1['study_environment'] = df_tratado_1['study_environment'].map(mapeamento_novo_ambiente)

# Removendo as colunas inutilizadas na minha analise.

df_final = df_tratado_1.drop(['timestamp', 'pressure_schoolmates', 'pressure_family', 'coping_strategy', 'bad_habits'], axis=1)

# Confirmação do tratamento:

print("\n", "---"*15, "\n")
print("APÓS A REALIZAÇÃO DO TRATAMENTO: ")
print("\n", "---"*15, "\n")
print(df_final.info())
print("\n", "---"*15, "\n")

# Seção 5:
# Seção 5.1:
# Análise 1:
# Objetivo: Avaliar nível de estresse acadêmico relatado, por nível acadêmico, através de análise analítica
# Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível acadêmico e sua distribuição, e além disso um gráfico mostrando a média de cada área.

# Seção 5.1.1 - Analises de tendencia central e dispersão
# Inicialmente, iremos realizar somente os cálculos filtrados por níveis acadêmicos:

media_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].mean()
moda_estresse_nivel_academico = df_final.groupby('academic_stage')['stress'].apply(lambda x: x.mode()[0])
mediana_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].median()
variancia_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].var()
desvio_padrao_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].std()
amplitude_estresse_nivel_academico = ( df_final.groupby('academic_stage')[['stress']].max() - df_final.groupby('academic_stage')[['stress']].min() )

# Exibindo os dados:

print("\n", "---"*15, "\n")
print(f"A média de estresse por nível acadêmico é: \n\n{media_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A moda de estresse por nível acadêmico é: \n\n{moda_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A mediana de estresse por nível acadêmico é: \n\n{mediana_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A variância de estresse por nível acadêmico é: \n\n{variancia_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"O desvio padrão de estresse por nível acadêmico é: \n\n{desvio_padrao_estresse_nivel_academico}")
print("\n", "---"*15, "\n")
print(f"A amplitude de estresse por nível acadêmico é: \n\n{amplitude_estresse_nivel_academico}")
print("\n", "---"*15, "\n")

# Agora com os cálculos realizados, vamos fazer uns gráficos através do matplotlib. Inicialmente os de dispersão de dados via gráfico de colunas de cada nível acadêmico, depois a media dos 3.

# Os demais dados serão tratados de forma escrita no relatório

# Seção 5.1.2 - Gráficos por nível acadêmico

# Seção 5.1.2.1 - HIGH-SCHOOL

# Filtramos pelo ensino médio
estresse_highschool = df_final[df_final['academic_stage'] == 'high school']['stress'].value_counts().sort_index()

# Gráfico
plt.bar(estresse_highschool.index, estresse_highschool.values)

#Embelezamento do gráfico:
plt.title("Distribuição do nível de estresse - Ensino Médio")
plt.xlabel("Nível de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y') # Aqui mostro a linha do grid no eixo y para melhor visualização do gráfico
plt.xticks([0, 1, 2, 3, 4, 5]) # Aqui defino a separação do eixo x; Não da pra definir um único para o y pois os a qtd de dados variam pelo nível acadêmico, mas a escala no eixo x sempre é a mesma. obs: não há nenhum dado com valor 0, porém, listei ele para ficar mais bonito o grafico.
plt.tight_layout()
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_ensino_medio.png') # Como vou fazer vários gráficos, não da pra mostrar todos ao mesmo tempo, tenho que salvar um por um, depois vou só adicionar as imagens no relatório em markdown
plt.clf() #Limpando para o proximo gráfico

# Seção 5.1.2.2 - undergraduate

estresse_undergraduate = df_final[df_final['academic_stage'] == 'undergraduate']['stress'].value_counts().sort_index()

# Grafico
plt.bar(estresse_undergraduate.index, estresse_undergraduate.values)

#Embelezamento do gráfico:
plt.title("Distribuição do nível de estresse - Graduação")
plt.xlabel("Nível de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_graduação.png')
plt.clf()

# Seção 5.1.2.3 - post-graduate

estresse_postgraduate = df_final[df_final['academic_stage'] == 'post-graduate']['stress'].value_counts().sort_index()

# Gráfico
plt.bar(estresse_postgraduate.index, estresse_postgraduate.values)

#Embelezamento do grafico:
plt.title("Distribuição do nível de estresse - Pós Graduação")
plt.xlabel("Nível de estresse relatado")
plt.ylabel("Quantidade de estudantes")
plt.grid(axis='y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\distribuicao_estresse_pos_graduação.png')
plt.clf()

# Seção 5.1.3.1 - Gráfico geral dos 3 níveis acadêmicos
media_estresse_niveis = df_final.groupby('academic_stage')['stress'].mean().sort_values(ascending=True)

'''

DEVIDO A MÉDIA ENTRE OS 3 SEREM PRÓXIMAS, UM GRÁFICO NORMAL FICA DIFÍCIL A VISUALIZAÇÃO DA DIFERENÇA, POR ISSO FIZ UM "SEM ZOOM", E UM "COM ZOOM"

'''

# Seção 5.1.3.1.1 - Gráfico sem zoom
plt.bar(media_estresse_niveis.index, media_estresse_niveis.values)

#Embelezamento do gráfico:
plt.title("Média de Nível de estresse por estágio acadêmico")
plt.xlabel("Estagio Acadêmico")
plt.ylabel("Média de estresse")
plt.grid(axis='y')
plt.ylim(0, 5)
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\media_estresse_niveis.png')
plt.clf()

# Seção 5.1.3.1.2 - Gráfico com zoom
plt.bar(media_estresse_niveis.index, media_estresse_niveis.values)

#Embelezamento do gráfico:
plt.title("Média de Nível de estresse por estágio acadêmico")
plt.xlabel("Estagio Acadêmico")
plt.ylabel("Média de estresse")
plt.grid(axis='y')
plt.ylim(3, 4)
plt.yticks([3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0])
plt.tight_layout() 
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\media_estresse_niveis_zoom.png')
plt.clf()

# Seção 5.2:
# Análise 2:
# Objetivo: Avaliar se o stress acadêmico relatado tem relação com a competição acadêmica relatada.
# Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
# Explicações do motivo dos gráficos abaixo:
#   Ao utilizar o gráfico de dispersão padrão, a visualização era ruim, pois, devido a muitos pontos se sobreporem, não era possível uma optima visualização dos dados e a busca de uma correlação.
#   Para encontrar uma maneira de visualização ótima, pesquisei e testei várias plotagens de gráficos, e após muitos testes acabei escolhendo um "heat map", com o kde do seaborn, junto á um grafico de dispersão do matplotlib com alguns parametros modificados. Junto á uma personalização para melhor visualização e visual mais agradavel. 
#   Abaixo, vou explicar o porque de cada coisa, e oque significa cada parâmetro. (Isto é, para eu justificar o uso de cada parâmetro)

sns.kdeplot( # O kde plot faz uma plotagem do que se parece um mapa de altitude, utilizei esse no cenário atual como um "heat map" de onde tinha mais frequência de dados.
    x=df_final['academic_competition'], #Seleciona o eixo X como a escala de competição acadêmica
    y=df_final['stress'], #Seleciona o eixo y como a escala de estresse relatado
    fill=True, #Preenche os campos, para não ficar só o contorno
    cmap="Blues", #Um estilo que achei adequado, e bonito
    alpha=0.5, #Define a transparência (Para que a sobreposição fique mais mesclada)
    levels=10, # Define a "qualidade" do gráfico, após testes, 10 é o suficiente para uma boa visualização
    zorder=1 # Define a posição do gráfico (em profundidade). Dividi em 3 levels, 0, 1, e 2)
)
plt.scatter(
    x=df_final['academic_competition'], #Mesma coisa do de cima
    y=df_final['stress'],
    color='black', # Escolhi a cor preta para uma melhor visualização
    alpha=0.3, # Novamente, a transparência para uma melhor visualização da concentração de dados
    zorder=2 # Posição entre as camadas de profundidades já previamente definidas
)

# Embelezamento
plt.title('Relação entre Estresse e Competição Acadêmica') #Defino os Títulos
plt.xlabel('Nível de Competição Relatado')
plt.ylabel('Nível de Estresse Relatado')
plt.grid(zorder=0) #Defino a camada que o grid aparece
plt.xticks([0, 1, 2, 3, 4, 5, 6]) # Os dados são de 1 a 5, mas para que a visualização fique mais centralizada no gráfico, coloquei uma posição a mais de ambos os lados
plt.yticks([0, 1, 2, 3, 4, 5, 6])
plt.tight_layout() #Ajusta o layout automaticamente
plt.savefig(r'C:\Users\victo\Python_Senai390\Semana_3\dispersao_estresse_competitividade.png')
plt.clf()

# Seção 5.3:
# Análise 3:
# Objetivo: Avaliar se o ambiente de estudo é diretamente relatado ao nível de estresse
# Pré processamento: Para uma melhor avaliação, vou converter o ambiente de texto (object), para um variável escalar (Inteira, de 1 a 3), pois só há 3 variações.
# Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacíficos são ligados á estresses relatados como baixo (1 ou 2, na escala), e se, ambientes ruins geram nivéis de estresse maiores. 

# To cansado, vou parar por aqui nesse momento, assim que eu acordar eu termino essa ultima analise e o relatório. 