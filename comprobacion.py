# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_completo.csv')

# Conocer la cantidad de datos faltantes por cada columna
#print(df.count())

df['active'].value_counts().plot(kind='bar')

plt.show()

