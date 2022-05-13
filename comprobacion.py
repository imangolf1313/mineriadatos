# Importar pandas 
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_completo.csv')

# Conocer la cantidad de datos faltantes por cada columna
print(df.count())