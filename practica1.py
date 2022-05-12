# Importar pandas 
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/users_data2.csv')

# Imprimir 5 registros
#print(df.head())

# Dimencion del dataset/ dataframe
#print(df.shape)

# Nombre de tipo o dictado de columna
#print(df.dtypes)

# Consideraciones de rendimiento (columnas,datos nulos, dtypes, peso, etc)
#print(df.info())

# Describir dataframe

# Muestra el numero de datos de cada columna, datos unicos, es que mas se repite, asi como la frecuencia 
#(df.describe())

# Conocer la cantidad de datos faltantes por cada columna
#print(df.count())

# Conocer si hay datos duplicados
#print(df.duplicated().sum())


col_names =df.columns.tolist()
#print(col_names)

# Iterar sobre la listas
for column in col_names :
    # Conocer valores nulos
    print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))
    #conocer tipo de daro
    print( "Tipo de valor  <"+ column + ">: "  + str (df[column].dtypes))

# llenar la columan de avatar con una url por default
df['avatar'] = df['avatar'].fillna('default.png')

# llenar la columan de genero con una D
df['gender'] = df['gender'].fillna('D')

# llenar la columan de lenguage con Desconocido
df['lenguage'] = df['lenguage'].fillna('Desconocido')


df.to_csv('mineriadatos/user_modify.csv', index=False)