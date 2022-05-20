# Importar pandas 
from tokenize import group
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/user_modify.csv')

# Seleccionar aolumnas para analisis
df = df[['gender', 'role']]

print(df.head(6))

# Agrupar  gender y role en dt
group = df.groupby(["gender", "role"])
print(group.size().reset_index(name='counts'))
