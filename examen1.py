# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:31:33 2021

@author: BazanJuanCarlos
"""
#importando librerias
import pandas as pd
#network para grafos
import networkx as nx
#mostrar imagenes
import matplotlib.pyplot as plt

#%matplotlib inline
plt.rcParams['figure.figsize']=(20.0,10.0)

#lectura de datos
datos=pd.read_csv('datos.csv',sep=';',header=0)
#impresion de datos
print(datos)
#mostrar una columna especifica
print("________________________________________")
#print("imprime una columna especifica")
#print("columna origen")
#print(datos['origen'])
#separacion en columnas
print("________________________________________")
#creando un directorio grafo
dg=nx.DiGraph()
for row in datos.iterrows():
    dg.add_edge(row[1]["origen"],
                row[1]["destino"],
                duration=row[1]["peso"])
print(dg.nodes(data=True))
#dibujar el grafo
nx.draw(dg,
        node_color="lightblue",
        edge_color="gray",
        font_size=27,
        width=2,with_labels=True,node_size=3500)

print("________________________________________")
#muestra el camino mas cortos 
print("camino mas corto")
print(list(nx.all_shortest_paths(dg,source="a", target="e", weight=None)))
#campo mas corto usando dikstra
print("________________________________________")
print("camino mas corto con dijkstra")
print(list(nx.dijkstra_path(dg,source="a", target="e", weight="peso")))
print("________________________________________")
print("________________________________________")

#lectura de filas del dataset
print(datos.iloc[0]["origen"])
print(datos.iloc[0]["destino"])
print(datos.iloc[0:4]["peso"])
filas_conteo=len(datos.axes[0])
print(filas_conteo)
print("________________________________________")
print("________________________________________")

vector_distancia=[]
vector_destino=[]
peso_total=100
dato_menor=""
a=1
i=0
dato=""
peso=0
if a==1:
    vector_destino.append(datos.iloc[i]["origen"])
    a=2
    i=1
    for j in range(filas_conteo):
        if vector_destino[i-1] == datos.iloc[j]["origen"]:
            dato=datos.iloc[j]["destino"]
            peso=datos.iloc[j]["peso"]
        if peso_total > peso:
            peso_total=peso
            dato_menor=dato
    vector_destino.append(dato_menor)
    i=2
peso_total=100
peso=100
for j in range(filas_conteo):
        if vector_destino[i-2]!=datos.iloc[j]["origen"]:
            if vector_destino[i-1] == datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["destino"] :
                dato=datos.iloc[j]["destino"]
                peso=datos.iloc[j]["peso"]
        if peso_total > peso:
            peso_total=peso
            dato_menor=dato
vector_destino.append(dato_menor)
i=3
peso_total=100
peso=100
for j in range(filas_conteo):
        if vector_destino[i-3]!=datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["origen"] :
            if vector_destino[i-1]==datos.iloc[j]["origen"] :
                if vector_destino[i-3]!=datos.iloc[j]["destino"] and vector_destino[i-2]!=datos.iloc[j]["destino"] and vector_destino[i-1]!=datos.iloc[j]["destino"]:
                    dato=datos.iloc[j]["destino"]
                    peso=datos.iloc[j]["peso"]
                    
            
            if peso_total > peso:
                peso_total=peso
                dato_menor=dato
            
vector_destino.append(dato_menor)
i=4
peso_total=100
peso=100                   
for j in range(filas_conteo):
        if vector_destino[i-4]!=datos.iloc[j]["origen"] and vector_destino[i-3]!=datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["origen"] :
            if vector_destino[i-1]==datos.iloc[j]["origen"] :
                if vector_destino[i-4]!=datos.iloc[j]["destino"] and vector_destino[i-3]!=datos.iloc[j]["destino"] and vector_destino[i-2]!=datos.iloc[j]["destino"] and vector_destino[i-1]!=datos.iloc[j]["destino"]:
                    dato=datos.iloc[j]["destino"]
                    peso=datos.iloc[j]["peso"]
                    
           
            if peso_total > peso:
                peso_total=peso
                dato_menor=dato     
vector_destino.append(dato_menor)           
print("________________________________________")
print("________________________________________")
print("dimencion del vector")
print(len( vector_destino ))
print("la ruta mas corta es :")
for i in vector_destino:
    print(i)
print("________________________________________")
print("________________________________________")  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    