import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier

# Importando a base de dados modificada
import pickle
with open('./restaurante_modified.pkl', 'rb') as f:
  X_treino, X_teste, y_treino, y_teste = pickle.load(f)
  
# Indica que está usando entropia
modelo = DecisionTreeClassifier(criterion='entropy')
Y = modelo.fit(X_treino, y_treino)

# Testando - Gerando previsões para ver se está certo
previsoes = modelo.predict(X_teste)

# Como sabemos que essa base já foi validada vamos partir para a execução, sem teste

# Visualização da árvore de decisão
from sklearn import tree
previsores = X_treino.columns
figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(13,13))
tree.plot_tree(modelo, feature_names=previsores, class_names = modelo.classes_, filled=True);

# Printando a árvore
plt.show()
