import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega a base de dados
titanic_df = pd.read_csv('../../database/train.csv')

# Mostra as primeiras infos
print("Amostra dos Dados:") 
print(titanic_df.head())

# Dados faltantes
print("\nInformações e Dados Faltantes:")
print(titanic_df.info())

# Configurar a figura para plotar múltiplos gráficos (2 linhas, 4 colunas)
fig, axes = plt.subplots(2, 4, figsize=(24, 12))
fig.suptitle('Análise Univariada dos Atributos do Titanic', fontsize=20)

# Gráfico 1: Survived (Sobreviveu)
sns.countplot(ax=axes[0, 0], x='Survived', data=titanic_df)
axes[0, 0].set_title('Distribuição de Sobreviventes')
axes[0, 0].set_xticklabels(['Não (0)', 'Sim (1)'])

# Gráfico 2: Pclass (Classe do Passageiro)
sns.countplot(ax=axes[0, 1], x='Pclass', data=titanic_df)
axes[0, 1].set_title('Distribuição por Classe')

# Gráfico 3: Sex (Sexo)
sns.countplot(ax=axes[0, 2], x='Sex', data=titanic_df)
axes[0, 2].set_title('Distribuição por Sexo')

# Gráfico 4: Embarked (Porto de Embarque)
sns.countplot(ax=axes[0, 3], x='Embarked', data=titanic_df)
axes[0, 3].set_title('Distribuição por Porto de Embarque')

# Gráfico 5: Age (Idade)
sns.histplot(ax=axes[1, 0], x='Age', data=titanic_df, kde=True, bins=30)
axes[1, 0].set_title('Distribuição de Idade')

# Gráfico 6: Fare (Tarifa)
sns.histplot(ax=axes[1, 1], x='Fare', data=titanic_df, bins=40)
axes[1, 1].set_title('Distribuição de Tarifa Paga')
axes[1, 1].set_xlim(0, 300) # Limitar o eixo X para melhor visualização

# Gráfico 7: SibSp (Irmãos/Cônjuges a Bordo)
sns.countplot(ax=axes[1, 2], x='SibSp', data=titanic_df)
axes[1, 2].set_title('Nº de Irmãos/Cônjuges')

# Gráfico 8: Parch (Pais/Filhos a Bordo)
sns.countplot(ax=axes[1, 3], x='Parch', data=titanic_df)
axes[1, 3].set_title('Nº de Pais/Filhos')

# Ajustar o layout para não haver sobreposição
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()