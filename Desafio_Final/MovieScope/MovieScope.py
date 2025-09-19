'''
Etapa 1 - Realizar a leitura através do Pandas



'''

import pandas as pd #pandas
import os #Lidar com caminhos da os

pastadatasets = "Desafios_Plano_De_Ensino\MovieScope\Dataset"
movies_dataset = "tmdb_5000_movies.csv"
credits_dataset = "tmdb_5000_credits.csv"

movies = os.path.join(pastadatasets, movies_dataset)
credits = os.path.join(pastadatasets, credits_dataset)

# Lendo o movies

print(f"\nTentando ler: {movies}")

if os.path.exists(movies):
    df_movies = pd.read_csv(movies)
    print("Sucesso, primeiras 5 linhas abaixo:","\n")
    print(df_movies.head())
else:
    print(f"O arquivo '{movies}' não foi encontrado na pasta '{pastadatasets}'.")

# Lendo o credits

print(f"\nTentando ler: {credits}")

if os.path.exists(credits):
    df_credits = pd.read_csv(credits)
    print("Sucesso, primeiras 5 linhas abaixo:","\n")
    print(df_credits.head())
else:
    print(f"O arquivo '{credits}' não foi encontrado na pasta '{pastadatasets}'.")