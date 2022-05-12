# Importar pandas 
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/user_modify.csv')

# Imprimir 5 registros
#print(df.head(15))

col_names =df.columns.tolist()
#print(col_names)
# Iterar sobre la listas
for column in col_names :
    # Conocer valores nulos
    print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))
    #conocer tipo de daro
    print( "Tipo de valor  <"+ column + ">: "  + str (df[column].dtypes))


# Conocer si hay datos duplicados
#quitar datos duplicados quitando el ultimo
df = df.drop_duplicates(keep='last', subset=['first_name'])
print(df.duplicated().sum())

print(df.shape)

df.to_csv('mineriadatos/user_modify.csv', index=False)