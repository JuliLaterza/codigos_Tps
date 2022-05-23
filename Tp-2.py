# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:13:35 2022

@author: Usuario
"""

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
print("lista generada \n",resultado)
print("la sumatoria es ",sumatoria(resultado))
print(capicua(lista))
num = int(input("Ingresar número a eliminar: "))
dupli(num,resultado)
print(resultado)


#%%  Ejercicio 2
import random

def generar_lista(lista:list):
    for i in range(50):
        lista.append(random.randint(1,100))
    return lista

def repetidos(arr:list):
    if len(arr) == len(set(arr)):
        repetidos = False
    else:
        repetidos = True
    
    lista_sin_repetidos = set(arr)
    return repetidos, lista_sin_repetidos

array = []
generar_lista(array)
repet = repetidos(generar_lista(array))
print(repet)


#%% Ejercicio 3

def cuadrados(array:list):
    for i in range(len(array)):
        array[i] = array[i]**2
    return array, array[-10:]

lista = []
n = int(input("ingresar número n: "))
i = 0
for i in range(n):
    #print(i+1)
    lista.append(i+1)

print(cuadrados(lista))
#%% Ejercicio 4

def lista_palabras(lista1:list,lista2: list,eliminados:list,resultante:list):
    for i in lista1:
        if i in lista2:
            eliminados.append(i)
        else:
            resultante.append(i)
    return lista1,eliminados,resultante


lista1 = ["gato","perro","pato"]
lista2 = ["perro","ballena","mariposa"]
lista_resultante = []
lista_eliminados = []
print(lista_palabras(lista1,lista2,lista_eliminados,lista_resultante))


#%% Ejercicio 5
def ordenada (lista):
    for i in range(len(lista)):
        if lista[i] > lista[i+1]:
            return False
        else:
            return True

lista1 = ["b","a"]

print(ordenada(lista1))

#%% Ejercicio 6

def normalizar(lista):
    sumatoria=sum(lista)
    listanormalizada=[]
    for i in lista:
        porcentaje=round(i/sumatoria,2)
        listanormalizada.append(porcentaje)
    return listanormalizada

lista1=[1,2,3,4,5]
lista2=normalizar(lista1)
print(lista2)

#%% Ejercicio 8

def numImpares(numimp:list):
    impares = [i for i in numimp if (i%2) != 0]
    return impares

numeros = []
for i in range(100,201): #Generar los números del 100-200
    numeros.append(i)

print(numImpares(numeros))

#%% Ejercicio 9

def multiplos(nums:list):
    multi = [i for i in nums if ((i%7) == 0) and not (i%5) == 0]
    return multi
numeros = []


print("Ingresar 2 valores entre A y B para definir un rango.")
for i in range(int(input("Ingresar valor de A: ")),int(input("Ingresar número B"))):
    numeros.append(i)

print(multiplos(numeros))

#%% Ejercicio 10
import random

def impares(lista):
    impares = [i for i in lista if (i%2)!=0]
    return impares


array = []
for i in range(random.randint(1,99)):
    array.append(i)

print(impares(array))

#%% Ejercicio 12

def informe(array:list):
    pass

socios = []
num_socio = int(input('ingrese numero de socio'))
while num_socio!=0:
     if 10000<=num_socio<=99999:
        socios.append(num_socio)

informe(socios)