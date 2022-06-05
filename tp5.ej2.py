# -*- coding: utf-8 -*-

def sumanums(a,b):
    try:
        num1 = float(a)
        num2 = float(b)
        operacion = num1 + num2
        return round(operacion,2)
    except ValueError:
        return -1

print(sumanums('5','-2'))