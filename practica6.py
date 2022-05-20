# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_completo.csv')

# Imprimir 5 registros


df = df[['active', 'department']]
#print(df.head(6))

pd.crosstab(df['active'],df['department']).plot(kind='bar')
plt.title("Grafica active - department", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})

plt.xlabel("Active", size = 16)
plt.ylabel("Department", size = 16)
plt.show()