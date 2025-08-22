# Relatório
# Atividade: Exploração e Análise Inicial de Dados Reais
---

## Sumário:

1. [Dataset Escolhido](#dataset)
2. [Plano de Análise/Ação](#plano-de-Ação)
---

## Dataset:

Para a minha análise, resolvi escolher um dataset na plataforma Kaggle, para ser mais específico, um dataset que trata sobre o estresse no ambiente acadêmico, em 3 aréas: Ensino Médio (high school), Graduação (undergraduate) e Pós Graduação (pos-graduate). 

Ele está disponivél para download na seguinte url:

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

#### 1. Baixar e Carregar Arquivos
Realizei o download do dataset via script pré pronto disponivel no kaggle, e após isso movi ele manualmente para a pasta de uso final. O script utilizado está disponivel em: 



Baixei através de outro script e minha apikey, o scrip está disponível na mesma pasta nomeado como "Download.py", mas, para sua execução é necessário uma apikey valida.

#### 2. Visualização inicial dos dados (✅)
    Usei o "df.head"

3. Avaliar informações e variações (✅)
    Através do comando "df.info", pude notar que há uma inconsistência nos dados (Em somente uma linha). Então para isso, irei deletar ela para uma maior uniformidade.
    
4. Tratamento dos dados (✅)
    1. Apaguei o registro incompleto para uniformidade de dados, usando o "df.dropna", e ficando com 139 registros íntegros. (✅)
    2. Além disso, notei que os nomes das colunas apresentam espaços, aspas, e outras incongruências e são grandes demais, para melhorar isso, irei renomear as colunas. (✅)
        (Para facilitar minha vida, vou manter em inglês)
    3. Irei excluir as colunas inutilizadas para as minhas analises. (De certa forma é economia de recursos, mas, na escala atual é só para melhor organização msm) (✅)
         
5. Análise dos dados (EM ANDAMENTO)
    Como o meu dataset escolhido tem várias colunas, para uma melhor precisão irei focar em 3 visualizações dos dados, sendo elas:
        1. Avaliar nível de estresse acadêmico relatado, por nível acadêmico, através de análise analítica (✅)
            Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível acadêmico e sua distribuição, e além disso um gráfico mostrando a média de cada área.
        
        2. Avaliar se o stress acadêmico relatado tem relação com a competição acadêmica relatada. (✅)
            Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
            
        3. Avaliar se o ambiente de estudo é diretamente relatado ao nível de estresse (❌)
            Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacíficos são ligados á estresses relatados como baixo, e se, ambientes ruins geram níveis de estresse maiores. 

    Com essas 3 abordagens, espero trazer uma ampla visão do dataset, abordando ele de diversas maneiras.
