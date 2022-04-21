# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:32:20 2022

@author: Usuario

TP 2: LISTAS
"""

#%% Ejercicio 1
import random

def funA(arr):
    lista = []
    for i in range(arr):
        lista.append(random.randint(1000,9999))
    return lista
    
def sumatoria(lista):
    total = sum(lista)
    return total

def dupli(valor,lista):
    
    if valor in lista:
        print("se encontró el num")
        lista.remove(valor)
    else:
        print("El número no se encuentra en la lista")

def capicua(lista):
    if lista == lista[::-1]:
        print("es capicua")
    else:
        print("no es capicua")


lista = [50,17,91,17,50]

resultado = funA(random.randint(10,99))
print(resultado)
print(sumatoria(resultado))
print(capicua(lista))
num = int(input("Ingresar número a eliminar: "))
dupli(num,resultado)
print(resultado)

#%% ejercicio 3

def cuadrados(array):
    for i in array:
        array[i] = array[i]**2
    return array


lista = []
n = int(input("ingresar número n: "))
i = 1
for i in range(n):
    lista.append(i)    
print(cuadrados(lista))



#%% Ej 2
import random

def ej2(lista
        
#%%
