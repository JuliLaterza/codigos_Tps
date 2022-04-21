# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:00:28 2022

@author: Usuario
"""

#Ejercicio 1
'''
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres
'''
def mayor(a,b,c):
    mayor = 0
    if b > a and b>c and (b!=c or b!=a):
        mayor = b
    elif c > a and c > b and (c!=a or c!=b):
        mayor = c
    elif a > b and a > c and (a!=c or a!=b):
        mayor = a
    else:
        mayor = -1
    return mayor
    #return mayor

print("El mayor número es: ",mayor(int(input("Ingrese número a: ")),int(input("Ingresar número b: ")),int(input("Ingresar número c: "))))


#%% Ejercicio 2

def fecha(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if b % 2 == 0 or b == 5:
            if 1<=a<=31:
                return True
        elif b==1:
            if 1<=a<=28:
                return True
        else:
            if 1<=a<=30:
                return True
    else:
        return False

print(fecha(31,5,2000))
#%% Ejercicio 3 REHACER

def viajes(cantViajes):
    if 1<=cantViajes<=20:
        print('Valor del pasaje actualizado')
    elif 21<=cantViajes<=30:
        print('20% sobre el valor del pasaje')
    elif 31<=cantViajes<=40:
        print('30% sobre el valor del pasaje')
    elif cantViajes>40:
        print('40% sobre el valor del pasaje')
    else:
        print("Número no valido")

viajes(int(input("Ingrese cantidad de viajes: ")))

#%% Ejercicio 4
def venta(total,recibido):
    cantQuin = 0
    cantCien = 0
    cantCin = 0
    cantVein = 0
    cantDiez = 0
    cantCinco = 0
    cantUno = 0
    resultante = recibido%total
    cond = True
    
    while cond == True:
        if ((resultante)//500)!=0:
            cantQuin +=1
            resultante = resultante % 500
            print('resultante de 500= ',resultante)
            cond = True
        elif ((resultante)//100) !=0:
            cantCien = resultante // 100 
            resultante = resultante % 100
            print("resultante de 100", resultante)
            cond = True
        elif ((resultante)//50) !=0:
            cantCin = resultante//50
            resultante = resultante % 50
            print("resultante de 50= ",resultante)
            cond = True
        elif ((resultante)//20) !=0:
            cantVein = resultante//20 
            resultante = resultante % 20
            print('resultante de 20= ', resultante)
            cond = True
        elif ((resultante)//10) !=0:
            cantDiez += 1
            resultante = resultante % 10
            print('resultante de 10= ', resultante)
            cond = True
        elif ((resultante)//5) !=0:
            cantCinco += 1
            resultante = resultante % 5
            print('resultante de 5= ', resultante)
            cond = True
        elif ((resultante)//1) !=0:
            cantUno = resultante // 1
            resultante = resultante % 1
            print('resultante de 1= ', resultante)
            cond = True
        else:
            cond = False
            print('Entró al False')
    print(cantQuin,cantCien,cantCin,cantVein,cantDiez,cantCinco,cantUno)
venta(450,1000)


#%% Ejercicio 4 - juan
def cambio(total, pago):
    if total>pago:
        error="El pago no es suficiente"
        return error
    elif total<=pago:
        vuelto=pago-total
        billete500=vuelto//500
        vuelto=vuelto-(billete500*500)
        billete100=vuelto//100
        vuelto=vuelto-(billete100*100)
        billete50=vuelto//50
        vuelto=vuelto-(billete50*50)
        billete20=vuelto//20
        vuelto=vuelto-(billete20*20)
        billete10=vuelto//10
        vuelto=vuelto-(billete10*10)
        billete5=vuelto//5
        vuelto=vuelto-(billete5*5)
        billete1=vuelto//1
    respuesta= "La cantidad de billetes es de 1:"+str(billete1)+", de 5:"+ str(billete5)+", de 10:"+ str(billete10)+", de 20:"+ str(billete20)+", de 50:"+ str(billete50)+", de 100:"+ str(billete100)+", de 500:"+ str(billete500)
    return respuesta

totalProductos= int(input("El precio total de la compra es:"))
pagoIngresado=int(input("El cliente pago con: "))

totalCambio=cambio(totalProductos, pagoIngresado)
print (totalCambio)


#%% Ejercicio 5

def asteriscosCua(a):
    fila = "*" * a
    for i in range(a):
        print(fila)
    print(' ')
    cont = 1
    if a>0:
        while cont <= a:
            print('*' * cont)
            cont += 1
    else:
        print("Número no válido")
asteriscosCua(5)

# print("--------o-------")
# def asteriscosEsc(n):
#     cont = 1
#     if n>0:
#         while cont <= n:
#             print('*' * cont)
#             cont += 1
#     else:
#         print("Número no válido")

# asteriscosEsc(5)
#%% Ejercicio 6

num1 = input('num1: ')
num2 = input('num2: ')

concat = num1 + num2

print(concat)
#%% Ejercicio 9
import random

def cantNaranjas(naranjas):
    cadaNaranja = []
    paraJugo = 0
    paraCajon = 0
    peso = 0
    camionDespachado = 0
    
    for i in range(naranjas): # Carga de naranjas x peso en el array.
        cadaNaranja.append(random.randint(150, 350))
        if 200<=cadaNaranja[i]<=300: # Verificación del peso para determinar destino.
            if peso<500000: # Verificación del lugar para en el Camión
                peso = peso + cadaNaranja[i]
                print(peso)
            if peso>=500000*0.8: #Verificación de si el camión se despacha o no.
                camionDespachado += 1
                if peso >= 500000:
                    peso = 0
            else:
                peso = 0
            paraCajon += 1
        else:
            paraJugo +=1
    
    print("Para jugo:", paraJugo)
    print("Para cajón:", paraCajon)
    print("Camiones a despachar:", camionDespachado)
cantNaranjas(5000)
        
#%% Ejercicio 3 de Lu

def controlarGastos(valorViaje: int, cantViajes: int):
    
    valor: int  = 0
    
    if (cantViajes > 1 and cantViajes <= 20):
        valor = valorViaje * cantViajes
        
    elif (cantViajes >= 21 and cantViajes <= 30):
        valor = cantViajes * (valorViaje * (80/100))
        
    elif (cantViajes >= 31 and cantViajes <= 40):
       valor = cantViajes * (valorViaje * (70/100))
       
    elif (cantViajes > 40):
       valor = cantViajes * (valorViaje * (60/100))
        
    return valor


#programa principal
valorViaje = int(input("Ingrese valor de viajes:"))
cantViajes = int(input("Ingrese cantidad de viajes:"))

vResultado = controlarGastos(valorViaje, cantViajes)
print(vResultado)