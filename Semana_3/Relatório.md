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
        1. Avaliar nivel de estresse academico relatado, por nivel academico, através de análise análitica (❌)
            Saida esperada: Vou montar um gráfico de colunas sobre o nível de estresse relatado por cada nível academico e sua distribuição, e além disso um gráfico mostrando a média de cada área.
        
        2. Avaliar se o stress academico relatado tem relação com a competição academica relatada. (❌)
            Saida esperada: Vou montar um gráfico de dispersão para analisar se há alguma relação entre os 2
            
        3. Avaliar se o ambiente de estudo é diretamente relatado ao nivel de estresse (❌)
            Pré processamento: Para uma melhor avaliação, vou converter o ambiente de texto (object), para um variavel escalar (Inteira, de 1 a 3), pois só há 3 variações.
            Saida esperado: Através disso, quero descobrir se, ambientes relatados como pacificos são ligados á estresses relatados como baixo (1 ou 2, na escala), e se, ambientes ruins geram nivéis de estresse maiores. 

    Com essas 3 abordagens, espero trazer uma ampla visão do dataset, abordando ele de diversas maneiras.
