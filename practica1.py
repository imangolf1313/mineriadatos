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
print(df.describe())
