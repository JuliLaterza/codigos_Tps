# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:09:05 2022

@author: Usuario
"""

#Practicas

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
    
print(f'Factorial: {fact(3)}')


def potencia (a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)
    
#print(potencia(2, 5))

# Imprimir números

def imprimir(n):
    if n>0:
        imprimir(n-1)
        print(n, end = " ")

#imprimir(100)


#listas
def buscarmayor(lista, inicio = 0):
    if inicio<len(lista)-1:
        actual = lista[inicio]
        mayor = buscarmayor(lista, inicio+1)
        return actual if actual>mayor else mayor
    else:
        return lista[-1] #último elemento

def imprimirlista(lista, inicio=0):
    if inicio <len(lista):
        print(lista[inicio], end = " ")
        imprimirlista(lista, inicio+1)
        

lista = [2,7,5,4,6,0,8,9]

#imprimirlista(lista)
#print()

maximo = buscarmayor(lista)
#print(f'El mayor elemento de la lista es {maximo}')
#%% Ejercicio 3 de TP9

def sumaNum(n):
    if n == 0:
        return 0
    else:
        suma = n + sumaNum(n-1)
        return suma

print(sumaNum(100))


#%% Ejercicio 4


'''
Sumas sucesivas

2 * 3 = 2 + 2 + 2
'''

def sumaSucesivas(a,b):
    if b == 1:
        return a
    else:
        return a + sumaSucesivas(a, b-1)


print(sumaSucesivas(2, 3))

#%%


arr = [2,3,4,6,5,6]

maximo = max(arr)

arr.remove(maximo)
cond = True
while cond:
    if max(arr) == maximo:
        arr.remove(maximo)
        cond = True
    else:
        cond = False
        maximo = max(arr)

print(maximo)
#%%

def print_full_name(first, last):
    # Write your code here
    texto = f'Hello {first} {last}! You just delved into python.'
    return texto

print(print_full_name("julian","laterza"))
