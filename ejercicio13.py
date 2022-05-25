# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:07:45 2022

@author: Usuario
"""

def numeroString(num:int):
    unidades = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince"]
    decenas = ["","diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
    centenas = ["","cien","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
    if num < 0:
        print("El número debe ser mayor a cero.")
    else:
        #manejo de unidades
        unid = num % 10
        ultDos = num % 100
        dec = (num//10)%10
        cen = num // 100
        
        if cen != 0: #verificar que el número sea mayor que 100
            if cen == 1: # es un número entre 100 y 199
                if ultDos == 0:
                    print("Cien",end="")
                else:
                    print("Ciento",end="")
            else:
                print(centenas[cen],end="")
        
        if ultDos != 0:
            
                    
                    
                
        
        
