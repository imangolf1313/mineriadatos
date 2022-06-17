import pandas as pd
import matplotlib.pyplot as plt
# Consulta rápida para ver si está conectando al dataset

df = pd.read_csv('mineriadatos/train.csv')
print(df.head(5))

# Conocer la dimensión
print(df.shape)
# Conocer la info del dataset
print(df.info())
# Conocer el número de registros por columna
print(df.count())
# Conocer registros duplicados
print(df.duplicated().sum())
# Llenar los campos nulos
    # Conocer valores nulos
col_names =df.columns.tolist()
for column in col_names :
    print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))
  # Llenar valores nulos de columnas
df['Age'] = df['Age'].fillna(0)  #Para que haya consistencia en el tipo de dato
df['Cabin'] = df['Cabin'].fillna("Unknown") #Desconocida
df['Embarked'] = df['Embarked'].fillna("U") #Unknown    

print("---------------COMPROBACION----------------------")
df.to_csv('mineriadatos/train_completo.csv', index=False)
df_completo = pd.read_csv('mineriadatos/train_completo.csv')
print(df_completo.count())
# Crear 3 crosstab para conocer más del dataset con tablas.
    #Grafica 1
df_completo1 = df_completo[['Sex', 'Age']]
ct = pd.crosstab(df['Sex'],df['Age']).plot(kind='bar')
plt.legend(title = "Edad") 
plt.title("Grafica 1. Sexo y Edad")
plt.xlabel("Genero")
plt.xticks([0, 1], ['Femenino', 'Masculino'])
plt.show()
    #Grafica 2
df_completo2 = df_completo[['Survived', 'Sex']]
ct2 = pd.crosstab(df_completo2['Survived'],df_completo2['Sex']).plot(kind='bar')
plt.legend(title = "Genero") 
plt.title("Grafica 2. Sobrevivio y Sexo")
plt.xlabel("Sobrevivio")
plt.xticks([0, 1], ['No', 'Si'])
plt.show()
    #Grafica 3
df_completo3 = df_completo[['Survived', 'Pclass']]
ct3 = pd.crosstab(df_completo3['Survived'],df_completo3['Pclass']).plot(kind='bar')
plt.legend(title = "Pclass") 
plt.title("Grafica 3. Sobrevivio y Pclass")
plt.xlabel("Sobrevivio")
plt.xticks([0, 1], ['No', 'Si'])
plt.show()