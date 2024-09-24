# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:03:05 2024

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

filtered_data = data[['AÑO','EXPORTADOR','PAIS DE DESTINO','CANTIDAD','PRODUCTO','PARTIDA ARANCELARIA','DESCRIPCION','US$ FOB','US$ FOB UNIT']].copy()

lista_variables_categoricas = ['AÑO','EXPORTADOR','PAIS DE DESTINO','DESCRIPCION']
lista_variable_numericas = ['CANTIDAD','US$ FOB','US$ FOB UNIT']
print(data.info())

df = filtered_data[(filtered_data['PARTIDA ARANCELARIA'] == 6031930) | (filtered_data['PARTIDA ARANCELARIA'] == 6031999)]
print(df)


######################## AGRUPAMIENTOS ############################################################

grupo_pais_ano = filtered_data.groupby(['AÑO','DESCRIPCION'])['CANTIDAD'].sum().reset_index()
print(grupo_pais_ano)
print("")

grupo_pais = filtered_data.groupby(['AÑO'])['CANTIDAD'].sum().reset_index()
print(grupo_pais)
print("")

grupo_pais_producto = filtered_data.groupby(['AÑO'])['PRODUCTO'].sum().reset_index()
print("Cantidada de ITEM para la variable PRODUCTO : \t", grupo_pais_producto['PRODUCTO'].unique())
print("Cantidada de ITEM para la variable PRODUCTO : \t", len(grupo_pais_producto['PRODUCTO'].unique()))
#print(grupo_pais_producto)
print("")

dfg = filtered_data.groupby(['AÑO','PARTIDA ARANCELARIA'])['PRODUCTO'].count().sort_values(ascending=False).reset_index()
print(dfg)

################################### ANALISIS EXPLORATORIO ######################################




