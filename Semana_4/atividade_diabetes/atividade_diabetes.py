#Nome: Victor Augusto de Aquino Silvério
# atividade diabetes

# Bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Passo 1:
# carrega o dataset de diabetes (separador é o tab, li como se fosse um csv)
path = r'Semana_4\atividade_diabetes\data\data_original.txt'
df_diabetes = pd.read_csv(path, sep='\\t')

print("\n" + "---"*15 + "\n")
print("Cabeçalho dataset \n")
print(df_diabetes.head())
print("\n" + "---"*15 + "\n")

# A variável alvo (target) é a 'Y', que representa a progressão da doença
# As outras colunas são as características
X = df_diabetes.drop('Y', axis=1)
y = df_diabetes['Y']

# Passo 2:
# Dividindo os dados em 80% para treino e 20% para teste
# O random_state garante que a divisão seja a mesma em todas as execuções
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Passo 3:
# O problema é de regressão, pois queremos prever um valor contínuo (a progressão da doença).
# escolhi a Regressão Linear por ser um modelo simples e rápido
modelo = LinearRegression()

# Treinando

print("\n" + "---"*15 + "\n")
modelo.fit(X_treino, y_treino)
print("Modelo treinado")
print("\n" + "---"*15 + "\n")

# Fazendo previsões com o modelo treinado
print("Passo 4:\n")
previsoes = modelo.predict(X_teste)

# Passo 5:

erro_quadratico_medio = mean_squared_error(y_teste, previsoes)
r_quadrado = r2_score(y_teste, previsoes)

print("\n" + "---"*15 + "\n")
print("avaliacao modelo: \n")
print(f"Erro Quadrático Médio (MSE): {erro_quadratico_medio:.2f}")
print(f"Coeficiente de Determinação (R²): {r_quadrado:.2f}")
print("\n" + "---"*15 + "\n")


# Passo 6:

print("1. Qual modelo você escolheu? Por quê?")
print("escolhi a Regressão Linear por ser um modelo simples e rápido, e o objetivo é prever a progressão da doença, que é um valor numérico contínuo, caracterizando um problema de regressão. \n")

print("2. Qual foi a qualidade obtida?")
print(f"A qualidade do modelo, medida pelo coeficiente de determinação (R²), foi de {r_quadrado:.2f}. Isso significa que cerca de 45% da variabilidade na progressão da doença pode ser explicada pelas variáveis do modelo. O MSE foi de {erro_quadratico_medio:.2f}.\n")

print("3. O modelo se ajustou bem aos dados?")
print("Um R² de 0.45 indica um ajuste moderado. Ele consegue capturar algumas tendencias\n")

print("4. Você testaria outro modelo para tentar melhorar os resultados?")
print("Sim, com certeza. Modelos mais complexos como RandomForest ou Gradient Boosting podem melhorar o r²\n")