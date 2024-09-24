# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:36:40 2024

@author: marce
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


nuevo_directorio = "C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/tesis flores"

# Cambiar al nuevo directorio
os.chdir(nuevo_directorio)

# Verificar que el cambio se haya realizado
nuevo_directorio_actual = os.getcwd()
print("Nuevo directorio actual:", nuevo_directorio_actual)

# Valores únicos unique(), cantidad de valores unicos len(), 
ruta = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/tesis flores/estudio_final_flores_20240906.xlsx'


data = pd.read_excel(ruta, usecols=lambda x: x not in [0])

filtered_data = data[['ANO','EXPORTADOR','PAIS DE DESTINO','CANTIDAD','PRODUCTO','PARTIDA ARANCELARIA','DESCRIPCION','US_FOB','US_FOB_ UNIT']].copy()

lista_variables_categoricas = ['EXPORTADOR','PAIS DE DESTINO','DESCRIPCION']
lista_variable_numericas = ['CANTIDAD','US_FOB','US_FOB_ UNIT']


filtered_data['Punit'] = filtered_data['US_FOB'] / filtered_data['CANTIDAD']


###################### Ciclos ###########################################


# Análisis de variables categóricas
for var in lista_variables_categoricas:
    print(f"Análisis de la variable categórica en número de registros: {var}")
    print(filtered_data[var].value_counts())
    print("\n")

# Análisis de variables numéricas
for var in lista_variable_numericas:
    print(f"Análisis de la variable numérica: {var}")
    print(filtered_data[var].describe())
    print("\n")

# Visualización de variables categóricas
for var in lista_variables_categoricas:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=filtered_data, x=var)
    plt.title(f"Distribución de {var}")
    plt.xticks(rotation=45)
    plt.show()

# Visualización de variables numéricas
for var in lista_variable_numericas:
    plt.figure(figsize=(8, 5))
    sns.histplot(filtered_data[var], kde=True)
    plt.title(f"Distribución de {var}")
    plt.show()


#######################################################

print("Cantidad de numeros na de variable CANTIDAD: ",filtered_data['CANTIDAD'].isna().sum())
print(filtered_data['CANTIDAD'].describe()*0.1)
print("---------------------------------------------------------")
print("Cantidada de valores nulos: ",filtered_data['DESCRIPCION'].isna().sum())
print("Cantidada de valores unicos para la variables DESCRIPCION: ",len(filtered_data['DESCRIPCION'].unique()))
print(filtered_data['DESCRIPCION'].unique())
print("---------------------------------------------------------")
print("Cantidada de valores nulos: ",filtered_data['PRODUCTO'].isna().sum())
print("Cantidad de valores únicos para variable PRODUCTO: \t", len(filtered_data['PRODUCTO'].unique()))
print("Detalle de valores únicos variable PRODUCTO: \t", filtered_data['PRODUCTO'].unique())
print("")
result = filtered_data.groupby('PARTIDA ARANCELARIA')['CANTIDAD'].agg(['max','min','mean', 'sum', 'count'])
print(result)
print("")
re = filtered_data.groupby(['PARTIDA ARANCELARIA','PAIS DE DESTINO'])['CANTIDAD'].agg(['sum','max','min','mean']).reset_index()
print(re)

print("")
# # Asumiendo que filtered_data es tu DataFrame y 'US_FOB_UNIT' es la columna de interés
# plt.figure(figsize=(10, 6))
# plt.hist(re['PAIS DE DESTINO'])
# plt.title('Paises de destino')
# plt.ylabel('Valor')
# plt.show()



import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear un gráfico de barras para comparar las cantidades por país de destino y partida arancelaria
plt.figure(figsize=(14, 7))
sns.barplot(data=filtered_data, x='PAIS DE DESTINO', y='CANTIDAD', hue='PARTIDA ARANCELARIA')
plt.title('Comparación de Cantidades por País de Destino y Partida Arancelaria')
plt.xticks(rotation=45)
plt.show()

# Crear un gráfico de barras para comparar los precios por país de destino y partida arancelaria
plt.figure(figsize=(14, 7))
sns.barplot(data=filtered_data, x='PAIS DE DESTINO', y='US_FOB', hue='PARTIDA ARANCELARIA')
plt.title('Comparación de Precios por País de Destino y Partida Arancelaria')
plt.xticks(rotation=45)
plt.show()

####################################
#Quiero hacer un grafico de barras con la libreria matplotlib y seaborn

# Supongamos que 'data' es tu DataFrame original
filtered_data_grupo = filtered_data[filtered_data['PAIS DE DESTINO'].isin(['HOLANDA', 'U.S.A'])]

fdg = filtered_data_grupo.groupby(['ANO','PAIS DE DESTINO'])['CANTIDAD'].agg(['count','sum','max','min']).reset_index()
#print(fdg)

|# Crear un gráfico de barras para la cantidad total por año y país de destino
plt.figure(figsize=(14, 7))
sns.barplot(data=fdg, x='ANO', y='sum', hue='PAIS DE DESTINO')
plt.title('Cantidad Total por Año y País de Destino')
plt.xlabel('Año')
plt.ylabel('Cantidad Total')
plt.legend(title='País de Destino')
plt.show()



