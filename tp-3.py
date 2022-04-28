# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:42:59 2022

@author: Usuario
"""
#%% Ejercicio 2.e
fila = 6
columnas = 6
matriz = []

for f in range(fila):
    matriz.append([]) #Le agrego una fila QUE NO TIENE ELEMENTOS
    for c in range(columnas):
        matriz[f].append(0)

#trabajamos la matriz

filas = len(matriz)
columnas = len(matriz)
contador = 1

for f in range(filas):
    for c in range(columnas):
        if (f%2)==0 and (c%2)!=0:
            matriz[f][c] = contador
            contador +=1
        elif (f%2)!=0 and (c%2)==0:
            matriz[f][c] = contador
            contador += 1
    
print(matriz)

#%%
import random


def matriz_nxn(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) #cuantas columnas tiene la fila 1 (tamaño total de columnas)
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, n**2)
    return matriz


n = int(input("ingrese número de NxN: "))
arrays = []

for f in range(n):
    arrays.append([]) #Le agrego una fila QUE NO TIENE ELEMENTOS
    for c in range(n):
        arrays[f].append(0)

print(matriz_nxn(arrays))