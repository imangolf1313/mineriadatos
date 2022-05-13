# Importar pandas 
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_incompleto.csv')

# # Dimension del dataset/ dataframe
# print(df.shape)

# # Nombre de tipo o dictado de columna
# print(df.dtypes)

# # Conocer la cantidad de datos faltantes por cada columna
# print(df.count())

# # Conocer si hay datos duplicados
# print(df.duplicated().sum())

# col_names =df.columns.tolist()
# #print(col_names)

# # Iterar sobre la listas
# for column in col_names :
#     # Conocer valores nulos
#     print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))

# llenar la columan de company con una url por Desconocido
df['company'] = df['company'].fillna('desconocida')

# llenar la columan de car con una Desconocido
df['car'] = df['car'].fillna('desconocido')

# llenar la columan de favorite_app   con Desconocido
df['favorite_app'] = df['favorite_app'].fillna('desconocido')

# llenar la columan de avatar con una url por default
df['avatar'] = df['avatar'].fillna('default.png')

# llenar la columan de active con una indefinido
df['active'] = df['active'].fillna('indefinido')

# llenar la columan de is_admin con false
df['is_admin'] = df['is_admin'].fillna('false')

# llenar la columan de department con una url por indefinido
df['department'] = df['department'].fillna('indefinido')

# llenar la columan de genero con una D
df['gender'] = df['gender'].fillna('D')


df.to_csv('mineriadatos/usuarios_completo.csv', index=False)