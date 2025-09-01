import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pickle

# Importando database a ser utilizada
base = pd.read_csv('../../database/restaurante.csv', sep=';')

# Selecionando os campos desejados
cols_label_encode = ['Alternativo', 'Bar', 'SexSab','fome', 'Cliente','Preco', 'Chuva', 'Res','Tempo']
base[cols_label_encode] = base[cols_label_encode].apply(LabelEncoder().fit_transform)

# Campo Tipo que é nominal
cols_onehot_encode = ['Tipo']
onehot = OneHotEncoder(sparse_output=False)
df_onehot = onehot.fit_transform(base[cols_onehot_encode]) # Só em colunas categóricas
nomes_das_colunas = onehot.get_feature_names_out(cols_onehot_encode)
df_onehot = pd.DataFrame(df_onehot, columns=nomes_das_colunas)
base_encoded= pd.concat([df_onehot, base.drop(columns=cols_onehot_encode)], axis=1)

# Supondo que a última coluna seja o target
X_prev= base_encoded.iloc[:, :-1]
y_classe = base_encoded.iloc[:, -1]

# Criando as variáveis a serem rodadas como teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X_prev, y_classe, test_size = 0.20, random_state = 42)

# Salvando objetos  
with open('./restaurante_modified.pkl', mode = 'wb') as f:
  pickle.dump([X_treino, X_teste, y_treino, y_teste], f)

print("Arquivo 'restaurante_modified.pkl' criado com sucesso!")
