#%% Ejercicio 8

def sep_texto(texto):
    lista = texto.split()
    lista.sort()
    return " ".join(lista)

frase = input('Ingrese texto: ')

print(sep_texto(frase))

#%% Ejercicio 1

def capicua(palabra: str):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

texto = input('Ingrese palabra para ver si es capicua: ')

print(capicua(texto))