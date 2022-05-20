# Importar pandas 
from tokenize import group
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/user_modify.csv')

dff = pd.read_csv('mineriadatos/user_modify.csv')

dfu = pd.read_csv('mineriadatos/usuarios_completo.csv')

dfuu = pd.read_csv('mineriadatos/usuarios_completo.csv')

# Seleccionar columnas para analisis
df = df[['company', 'lenguage']]
print(df.head(6))

# Agrupar  gender y role en dt
group = df.groupby(["company", "lenguage"])
print(group.size().reset_index(name='counts'))


# Seleccionar columnas para analisis ['gender', 'role', 'country']
dff = dff[['gender', 'role', 'country']]

print(dff.head(6))

# Agrupar  gender y role en dt
group = dff.groupby(["gender", "role", "country"])
print(group.size().reset_index(name='counts'))


# Seleccionar columnas para analisis ['car', 'active']
dfu = dfu[['car', 'active']]
print(dfu.head(6))

# Agrupar  gender y role en dt
group = dfu.groupby(["car", "active"])
print(group.size().reset_index(name='counts'))


# Seleccionar columnas para analisis ['avatar', 'car']
dfuu = dfuu [['avatar', 'car']]
print(dfuu.head(6))

# Agrupar  gender y role en dt
group = dfuu.groupby(["avatar", "car"])
print(group.size().reset_index(name='counts'))