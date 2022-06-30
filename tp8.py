#%% Ejercicio 2 Tuplas

def dias(tup):
    dia = tup[0]
    mes = tup[1]
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    year = tup[2]
    
    if (dia != 0) or (mes!=0):
        return f'Es el {dia} de {meses[(mes-1)]} del año 20{year}'
    else:
        return f'Fecha no válida'
    

fecha = (1,2,13)

print(dias(fecha))


#%% Ejercicio 5 Tuplas

def versor(a,b):
    p_escalar = (a[0] * b[0]) + (a[1] * b[1])
    if p_escalar == 0:
        return 'Son ortogonales'
    else:
        return 'No son ortogonales'

versor1 =(2,3)
versor2 = (-3,2)

print(versor(versor1,versor2))


#%% Ejercicio 8

dic = {}
for i in range(20):
    dic[i+1] = (i+1)**2
print(dic)
