# Relatório
# Atividade: Exploração e Análise Inicial de Dados Reais
---

## Sumário:

1. [Dataset Escolhido](#dataset)
2. [Plano de Análise/Ação](#plano-de-Ação)
3. [Tratamento](#tratamento) 
4. [Resultados & Análise](#resultados-e-análise)
3.1 [Análise 1](#análise-1)




---

## Dataset:

Para a minha análise, resolvi escolher um dataset na plataforma Kaggle, para ser mais específico, um dataset que trata sobre o estresse no ambiente acadêmico, em 3 áreas: Ensino Médio (high school), Graduação (undergraduate) e Pós Graduação (pos-graduate). 

Ele está disponível para download na seguinte url:

https://www.kaggle.com/datasets/poushal02/student-academic-stress-real-world-dataset

### Estrutura dos dados:

Os dados se encontram salvos em csv, separados por 9 colunas, sendo elas:

1. Timestamp
    * Salva data e hora, no formato:
        * DD/MM/YYYY HH:MM:SS

2. Your Academic Stage
    * Armazena o nível acadêmico atual do participante, variando de:
        1. undergraduate
        2. high school
        3. post-graduate

3. Peer pressure
    * Armazena a escala relatada de pressão pelos colegas
        * Varia de 1 até 5

4. Academic pressure from your home
    * Armazena a escala relatada de pressão vinda de casa
        * Varia de 1 até 5

5. Study Environment
    * Armazena a avaliação do ambiente de estudo, variando de:
        1. Noisy
        2. Peaceful
        3. disrupted
        * há 1 valor em branco (Precisa de tratamento)

6. What coping strategy you use as a student?
    * Armazena o relato do estudante de como lida com o estresse, variando de:
        1. "Analyze the situation and handle it with intellect"
        2. "Social support (friends, family)"
        3. "Emotional breakdown (crying a lot)"

7. Do you have any bad habits like smoking, drinking on a daily basis?
    * Armazena os hábitos ruins relatados pelos estudantes, variando de:
        1. "No"
        2. "prefer not to say"
        3. "Yes"

8. What would you rate the academic  competition in your student life
    * Armazena o valor relatado da competição acadêmica na vida dele
        * Varia de 1 até 5

9. Rate your academic stress index
    * Armazena o índice de estresse relatado pelo estudante
        * Varia de 1 até 5

---

## Plano de Ação

--- Plano de Ação --- 

#### 1. Baixar e Carregar Arquivos:
> Realizei o download do dataset via script pré pronto disponível no kaggle, e após isso movi ele manualmente para a pasta de uso final. O script utilizado está disponível em: [Download.py](https://github.com/victor-silverio/Python_Senai390/blob/main/Semana_3/Download.py)

#### 2. Visualização inicial dos dados:
> Através do comando " .head" para uma visualização inicial da estrutura

#### 3. Avaliar informações e variações
> Através do comando " .info", pude notar que há uma inconsistência nos dados (Em somente uma linha). E irei tratar ela na proxima etapa.
    
#### 4. Tratamento dos dados
> Para realizar o tratamento adequado, dividi ele em 3 etapas, sendo elas:

> 1. Apaguei o registro incompleto para uniformidade de dados, usando o " .dropna", e ficando com 139 registros íntegros.

> 2. Após notar que os nomes das colunas apresentam espaços, aspas, e outras incongruências, e para melhorar isso, realizei o renomeando via " .rename", para nomes mais curtos e de entendimento rápido.

> 3. Exclui as colunas desnecessárias da minha análise. 
    >> De  certa forme é uma economia de recursos, mas para á escala deste dataset, se trata de uma ferramenta para melhor organização.
    >>> Poderia ter somente selecionado as colunas que iria utilizar, mas optei por apagar.

#### 5. Análise dos dados
> O dataset escolhido possui 9 colunas, dentre elas, escolhi realizar 3 vistas do dataset, focando principalmente sobre o nível de estresse.

> 1. Avaliar nível de estresse acadêmico relatado, por nível acadêmico, através de análise analítica e visualização gráfica.
    >> Análises de tendencia central e de dispersão, além de 5 gráficos de colunas, sendo eles:
        >>> Distribuição do estresse no Ensino Médio (high school).
        >>> Distribuição do estresse na Graduação (undergraduate).
        >>> Distribuição do estresse na Pós Graduação (pos-graduate).
        >>> Distribuição média do estresse entre os 3 níveis de ensino 
        >>>> * São 2, "com zoom" & "sem zoom", e isso será explicado mais a frente.
        
> 2. Avaliar se o stress acadêmico relatado tem relação com a competição acadêmica relatada.
    >> Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
            
> 3. Avaliar se o ambiente de estudo é diretamente relatado ao nível de estresse
    >> Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacíficos são ligados á estresses relatados como baixo, e se, ambientes ruins geram níveis de estresse maiores. 

Com essas 3 abordagens, espero trazer uma ampla visão do dataset, abordando ele de diversas maneiras.

## Tratamento:

Realizei o tratamento em 3 etapas, sendo a primeira o descarte de linhas com valores nulos

```python
# Seção 4:
# Tratamento dos dados:

df_tratado = df.dropna() # Limpa valores nulos
```
A segunda etapa foi renomear as colunas:
```python
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
```
E a ultima etapa, a remoção das colunas não utilizadas na análise.
```python
# Removendo as colunas inutilizadas na minha analise.

df_final = df_tratado_1.drop(['timestamp', 'pressure_schoolmates', 'pressure_family', 'coping_strategy', 'bad_habits'], axis=1)
```
Como parte final, confirmei o sucesso do tratamento:

```python
print("\n", "---"*15, "\n")
print("APÓS A REALIZAÇÃO DO TRATAMENTO: ")
print("\n", "---"*15, "\n")
print(df_final.info())
print("\n", "---"*15, "\n")
```

### Confirmação do tratamento:
Para fins de exibição, a saída foi:

```bash
 --------------------------------------------- 

APÓS A REALIZAÇÃO DO TRATAMENTO: 

 --------------------------------------------- 

<class 'pandas.core.frame.DataFrame'>
Index: 139 entries, 0 to 139
Data columns (total 4 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   academic_stage        139 non-null    object
 1   study_environment     139 non-null    object
 2   academic_competition  139 non-null    int64 
 3   stress                139 non-null    int64 
dtypes: int64(2), object(2)
memory usage: 5.4+ KB
None

 --------------------------------------------- 
```

## Resultados e Análise:

Nessa etapa irei exibir os resultados brutos das análises, além de exibição de gráficos e discussão sobre os resultados.

---

### Análise 1

> Calculo das medidas de tendencia central e de dispersão

---

Para realizar a parte das contas, foi utilizada a biblioteca pandas, com os seguintes comandos:

```python
media_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].mean()
moda_estresse_nivel_academico = df_final.groupby('academic_stage')['stress'].apply(lambda x: x.mode()[0])
mediana_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].median()
variancia_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].var()
desvio_padrao_estresse_nivel_academico = df_final.groupby('academic_stage')[['stress']].std()
amplitude_estresse_nivel_academico = ( df_final.groupby('academic_stage')[['stress']].max() - df_final.groupby('academic_stage')[['stress']].min() )

```

#### Resultados:

Os resultados de tendência central e dispersão do nível de estresse por estágio acadêmico foram:

**Medidas de Tendência Central**

* **Média:**
    * Ensino Médio: 3.827586
    * Pós-graduação: 3.727273
    * Graduação: 3.686869

* **Moda:**
    * Ensino Médio: 4
    * Pós-graduação: 4
    * Graduação: 4

* **Mediana:**
    * Ensino Médio: 4.0
    * Pós-graduação: 4.0
    * Graduação: 4.0

---

**Medidas de Dispersão**

* **Variância:**
    * Ensino Médio: 1.290640
    * Pós-graduação: 0.418182
    * Graduação: 1.094826

* **Desvio Padrão:**
    * Ensino Médio: 1.136064
    * Pós-graduação: 0.646670
    * Graduação: 1.046339

* **Amplitude:**
    * Ensino Médio: 4
    * Pós-graduação: 2
    * Graduação: 4

---

## Comentários:

Através dos dados adquiridos, é possível notar que os estudantes do ensino médio relataram maior estresse, com uma média de 3,83. 

Além disso, a mediana e a moda de todos os estágios foi 4, ou seja, a maior parte dos dados apontam um nível de estresse 4, de uma escala de 0 a 5.

Os dados de estresse da pós graduação são mais uniformes, indicando que o estresse relatado é parecido. Ainda que o espectro de dados deste nível escolar seja menor, oque pode causar essa falsa impressão. 

Já a graduação e o ensino médio apresentam maior dispersão dos dados, oque indica experiencias sobre os estresse serem mais diversas

Como generalização, podemos notar que todos os estudantes relataram que a vida acadêmica é estressante, e principalmente os do ensino médio, que relataram um estresse mais alto.

> Tadinhos, vão sofrer mais na graduação. Ensino médio foi muito tranquilo em comparação com a minha vida atual. 

## Gráficos:

Inicialmente, temos 3 gráficos, mostrando o nivel de estresse relatado por estágio de ensino:

![Ensino Médio](https://github.com/victor-silverio/Python_Senai390/blob/05c6828a62925e56d64865c4c644f662e36bdfce/Semana_3/graficos/distribuicao_estresse_ensino_medio.png) 
![Graduação](https://github.com/victor-silverio/Python_Senai390/blob/05c6828a62925e56d64865c4c644f662e36bdfce/Semana_3/graficos/distribuicao_estresse_gradua%C3%A7%C3%A3o.png)
![Pós Graduação](https://github.com/victor-silverio/Python_Senai390/blob/05c6828a62925e56d64865c4c644f662e36bdfce/Semana_3/graficos/distribuicao_estresse_pos_gradua%C3%A7%C3%A3o.png) 

E o gráfico mostrando a média entre os 3 estágios, que pode ser visualizado em 2 versões, a na escala normal:

![Geral](https://github.com/victor-silverio/Python_Senai390/blob/f8fb594e83f2600c56c94cd12b117a75a8adefe1/Semana_3/graficos/media_estresse_niveis.png)

E uma com uma escala menor, facilitando a visualização da diferença entre os 3. 

![Geral - Zoom](https://github.com/victor-silverio/Python_Senai390/blob/f8fb594e83f2600c56c94cd12b117a75a8adefe1/Semana_3/graficos/media_estresse_niveis_zoom.png)