# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#crosstab 
# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/titanic.csv')

#Conexion con dataset
# print(df.head(6))

#Dimension
# print("Dimension")
# print(df.shape)

# #Duplicados
# print("Duplicados")
# print(df.duplicated().sum())

# #Info
# print("Info")
# print(df.info())

# #Descripcion del dataset
# print("Descripcion")
# print(df.describe())

#Contar
# print("Contar")
# print(df.count())

#Cambiar datos null por un 2 para desconocido
df['Survived'] = df['Survived'].fillna(2)

#Cambiar datos null por S/C en columna cabin
df['Cabin'] = df['Cabin'].fillna('S/C')
print(df.count())

#Cambiar un diccionario con los valores originales por valores
# de reemplazo
d = {'male' : 'M', 'female': 'F' }

#Utilizamos un lambda para el reemplazo en una sola linea
df['Sex'] = df['Sex'].apply(lambda x:d[x])
#for x in df['Sex']:
#    df['Sex'] = df['Sex'].apply(d[x])

#Conocer el dataset con valores cambiados
#print(df['Sex'])

#Obtener los nombres de las columnas en una lista
col_names = df.columns.tolist()

#Iterar sobre la lista
#for column in col_names:
    #print("Valores nulos en <" + column + ">": + str(df[column].isnull))

#Cruce de tabla de informacion
ct = pd.crosstab(df['Survived'],df['Sex']).plot(kind='bar')
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad de sobrevivientes por genero")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()