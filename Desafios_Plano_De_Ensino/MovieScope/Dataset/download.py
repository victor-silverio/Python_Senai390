'''
Nome: Victor Augusto
Uso: Download dataset movies
'''


import kaggle as kg
import os #Somente para o unzip

download_pasta = "Desafios_Plano_De_Ensino\MovieScope\Dataset"

#Baixar dataset

print("baixando o dataset")

try:
    
    kg.api.authenticate()
    kg.api.dataset_download_files(
    dataset="tmdb/tmdb-movie-metadata",
    path=download_pasta,
    unzip=True
    )
    print("Download realizado  & extraido")
        
except Exception as e:
    print(f"Erro ao baixar o dataset: {e}")
    print("garanta que você tenha a chave de API")
    exit()
    
