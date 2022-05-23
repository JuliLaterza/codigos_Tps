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

#%% Ejercicio 2

#2.a    
def rellenar(matrix):
    cont = 1
    for f in range(len(matrix)):
        for c in range(len(matrix[0])):
            if f == c:
                matrix[f][c] = cont
                cont += 1
    return matrix

#2.b


#2.d
def rellenard(matrix):
    num:int = 8
    for f in range(len(matriz)):
        if f !=0:
            num = int(num/2)
        for c in range(len(matriz[0])):
            matriz[f][c] = num
    return matrix


n = int(input("ingrese número de matriz NxN: "))
matriz = [[0] * n for i in range(n)]

print(*rellenard(matriz),sep='\n')
#%% Ejercicio 3
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

#%% Ejercicio 4
import random

def llenar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz[f][c] = random.randint(0, 150)
    return matriz


def suma_bicis(matriz):
    bici_fabricas = []
    for i in range(len(matriz)):
        bici_fabricas.append(sum(matriz[i]))
    return bici_fabricas, bici_fabricas.index(max(bici_fabricas))

def mejor_dia(matriz):
    mejor_dia = []
    for i in range(len(matriz)):
        mejor_dia.append(max(matriz[i]))
    return max(mejor_dia)


n = int(input("ingresar cantidad de fábricas: "))
matriz = [[0]* 7 for i in range(n)]

print(*llenar_matriz(matriz),sep='\n')

print(suma_bicis(matriz))
print(mejor_dia(matriz))