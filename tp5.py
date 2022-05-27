# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:08:03 2022

@author: Usuario
"""
#%% Ejercicio 2
def sumanums(a,b):
    
    try:
        if (a != True and a != False and b != True and b != False):
            num1 = float(a)
            num2 = float(b)
            suma = num1 + num2
            formateo = round(suma,2)
            print(f'La suma es {formateo}')
        else:
            print("Los valores deben ser números. No pueden ser False o True.")
    except ValueError:
        print('Valores incorrectos, deben ser números.')

sumanums('5','-2.2')
#%% Ejercicio 2 modificado

def sumanums(a,b):
    try:
        if (a != True and a != False and b != True and b != False):
            num1 = float(a)
            num2 = float(b)
            operacion = num1 + num2
            #print(f'El resultado es: {round(operacion,2)}')
            return round(operacion,2)
        else:
            #print("Los valores deben ser números. No pueden ser False o True.")
            return -1
    except ValueError:
        #print('Valores incorrectos, deben ser números.')
        return -1

print(sumanums('hola','-2'))



#%% Ejercicio 5
import math
def raiz(num):
    try:
        if (num != False and num != True):
            rcuadrada = math.sqrt(num)
            print(rcuadrada)
        else:
            print("El valor ingresado debe ser un número. No puede ser False o True.")
    except TypeError:
        print('Debe ser un valor de tipo INT o FLOAT y además debe ser mayor a 0.')

raiz(4)
