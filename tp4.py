#%% Ejercicio 8

def sep_texto(texto):
    lista = texto.split()
    lista.sort()
    return " ".join(lista)

frase = input('Ingrese texto: ')

print(sep_texto(frase))

#%% Ejercicio 7

