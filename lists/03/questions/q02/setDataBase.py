import pandas as pd
import numpy as np

# Carrega a base de dados
df_proc = pd.read_csv('../../database/train.csv')

## AGE
median_age = df_proc['Age'].median() # Calcula a mediana
df_proc['Age'].fillna(median_age, inplace=True) ## Verifica se está preenchido e preenche com mediana
print(f"Valores faltantes em 'Age' preenchidos com a mediana: {median_age}") # Printa a mediana

## EMBARKED
mode_embarked = df_proc['Embarked'].mode()[0] # Calcula a moda da colun `Embarked`
df_proc['Embarked'].fillna(mode_embarked, inplace=True) # Verifica se está preenchido e preenche com o valor da moda
print(f"Valores faltantes em 'Embarked' preenchidos com a moda: '{mode_embarked}'") # Printa a moda

# Retirando colunas inúteis
df_proc.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True) # Cabin = valores faltantes / # Name | Ticket | Passanger ID | são identificadores
print("Colunas 'Cabin', 'Name', 'Ticket', 'PassengerId' foram removidas.")

# As únicas colunas que são texto são `sex` e `embarked`, tranformando elas em números
df_encoded = pd.get_dummies(df_proc, columns=['Sex', 'Embarked'], drop_first=True)

print(df_encoded.head()) # Exemplo
print(f"Data base gerada...")
df_encoded.to_csv('titanic_modified.csv', index=False) # Data base gerada


