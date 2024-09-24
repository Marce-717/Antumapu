# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:22:21 2024

@author: marce
"""

import pandas as pd
import os
import matplotlib.pyplot as plt



nuevo_directorio = "C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/tesis flores"

# Cambiar al nuevo directorio
os.chdir(nuevo_directorio)

# Verificar que el cambio se haya realizado
nuevo_directorio_actual = os.getcwd()
print("Nuevo directorio actual:", nuevo_directorio_actual)

# Como experto en programación Phyton 3 quiero quiero hacer un analsisi exploratorio con ciclo FOR para cada una de las listas (variables y variables numericas)

# Valores únicos unique(), cantidad de valores unicos len(), 
ruta = 'C:/Users/marce/OneDrive/Documentos/OneDrive/Documentos/tesis flores/Tesis_Estudio_flores_Diego.xlsx'
data = pd.read_excel(ruta)

filtered_data = data[['AÑO','EXPORTADOR','PAIS DE DESTINO','CANTIDAD','PARTIDA ARANCELARIA','US$ FOB','US$ FOB UNIT']].copy()

lista_variables_categoricas = ['AÑO','EXPORTADOR','PAIS DE DESTINO']
lista_variable_numericas = ['CANTIDAD','US$ FOB','US$ FOB UNIT']



# # Realizar análisis exploratorio para cada columna
# for column in filtered_data.columns:
#     unique_values = filtered_data[column].unique()
#     num_unique_values = len(unique_values)
    
#     print(f"Columna: {column}")
#     print(f"Valores únicos: {unique_values}")
#     print(f"Cantidad de valores únicos: {num_unique_values}")
#     print("-" * 40)
    
############################################################


# # Análisis exploratorio para variables categóricas
# print("Análisis de variables categóricas:")
# for var in lista_variables_categoricas:
#     unique_values = filtered_data[var].unique()
#     num_unique_values = len(unique_values)
#     print(f"Variable: {var}")
#     print(f"Valores únicos: {unique_values}")
#     print(f"Cantidad de valores únicos: {num_unique_values}\n")

# # Análisis exploratorio para variables numéricas
# print("Análisis de variables numéricas:")
# for var in lista_variable_numericas:
#     unique_values = filtered_data[var].unique()
#     num_unique_values = len(unique_values)
#     print(f"Variable: {var}")
#     print(f"Valores únicos: {var}")
#     print(f"Cantidad de valores únicos: {num_unique_values}\n")

# print(filtered_data['CANTIDAD'].hist())
# print(filtered_data['CANTIDAD'].describe())
# print(filtered_data['CANTIDAD'].plot())


#############################################################



# Análisis exploratorio para variables categóricas
print("Análisis de variables categóricas:")
for var in lista_variables_categoricas:
    unique_values = filtered_data[var].unique()
    num_unique_values = len(unique_values)
    print(f"Variable: {var}")
    print(f"Valores únicos: {unique_values}")
    print(f"Cantidad de valores únicos: {num_unique_values}\n")

# Análisis exploratorio para variables numéricas con histogramas
print("Análisis de variables numéricas:")
for var in lista_variable_numericas:
    unique_values = filtered_data[var].unique()
    num_unique_values = len(unique_values)
    print(f"Variable: {var}")
    #print(f"Valores únicos: {unique_values}")
    print(f"Cantidad de valores únicos: {num_unique_values}\n")
    
    # Crear histograma
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data[var], bins=30, edgecolor='k', alpha=0.7)
    plt.title(f'Histograma de {var}')
    plt.xlabel(var)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()
