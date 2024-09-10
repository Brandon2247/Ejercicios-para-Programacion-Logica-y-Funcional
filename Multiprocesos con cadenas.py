from multiprocessing import parent_process

def c1():
    cadena1 = input("Ingrese la cadena de caracteres: \n")
    x = cadena1
    print(x[0:2])

def c2():
    cadena2 = input("Ingrese una segunda cadena de caracteres: \n")
    x = cadena2
    print(x[8:11])

#Escribir funciones que dada una cadena de caracteres:
cad= input("Cadena: ")

#A) Imprime los dos primeros caracteres.
def pricad(): #funcion para primera cadena
    return cad[:2]
print("a :\n", pricad())

#B) Imprime los tres ultimos caracteres
def segcad():
    return cad[-3:]
print("b: \n", segcad())

#C) Imprime dicha cadena cada dos caracteres. Ejemplo: palabra "recta" deberia de imprimir rca
def tercad():
    return cad[::2]
print("c :\n", tercad())

#D) Dicha cadena en sentido inverso. Ejemplo: la impresion de "Hola mundo!" deberia de ser "!odnum aloh"
def cuacad():
    return cad[::-1]
print("d :\n", cuacad())

#E) Se imprime la cadena en un sentido y en sentido inverso. Ejemplo: la impresion de "reflejo" deberia de dar como resultado "reflejoojelfer"
def quicad():
    return cad+cad[::-1]
print("e :\n", quicad())

#Funciones que en cada cadena y un caracter:

#A) Se inserte un caracter entre cada letra de la cadena. Ejemplo: Al ingresar "Separar" deberia de retornar "S,e,p,a,r,a,r"
