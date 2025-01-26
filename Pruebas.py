import pandas as pd
import numpy as np

# Valores únicos unique(), cantidad de valores unicos len(), 
ruta = 'Tesis_Estudio_flores_Diego.xlsx'
data = pd.read_excel(ruta)

filtered_data = data[['AÑO','EXPORTADOR','PAIS DE DESTINO','CANTIDAD','PRODUCTO','PARTIDA ARANCELARIA','DESCRIPCION','US$ FOB','US$ FOB UNIT']].copy()

lista_variables_categoricas = ['AÑO','EXPORTADOR','PAIS DE DESTINO','DESCRIPCION']
lista_variable_numericas = ['CANTIDAD','US$ FOB','US$ FOB UNIT']

# Como experto en programación Phyton 3 quiero saber el porcentaje para las clases de la variable "PARTIDA ARANCELARIA"
df = filtered_data[(filtered_data['PARTIDA ARANCELARIA'] == 6031930) | (filtered_data['PARTIDA ARANCELARIA'] == 6031999)]

cantidad_registros = len(df)
print(f"La cantidad de registros de las partidas arancelarias 6031930 y 6031999 es: {cantidad_registros}")

total_registros = len(df)
print(f"El total de registros en la data es: {total_registros}")

clases_unicas = df['PARTIDA ARANCELARIA'].unique()
print(f"Las clases únicas de la variable 'PARTIDA ARANCELARIA' son: {clases_unicas}")

for clase in clases_unicas:
    cantidad_clase = len(df[df['PARTIDA ARANCELARIA'] == clase])
    porcentaje_clase = (cantidad_clase / total_registros) * 100
    print(f"El porcentaje de la clase {clase} es: {porcentaje_clase:.2f}%")

print("")
print(df.columns)
print(df['US$ FOB UNIT'].describe())
print(df['US$ FOB UNIT'].hist())

