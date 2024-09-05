import math

# Actividad 7.1 
def recortar(p):
    t = p.remove('Lunes')
    t = p.remove('Domingo')
    return t

def medio(o):
    del o[0]
    del o[-1]
    return o
# // Actividad 7.1

# Actividad 7.2
def act2():
    manejador = open('romeo.txt')
    for linea in manejador:
        palabras = linea.split()
        if len(palabras) == 0 or palabras[0] != 'Pero':
            print(palabras[2])
# // Actividad 7.2

# Actividad 7.3
def act3():
    lista_palabras = []
    man_a = open('romeo.txt')
    for linea in man_a:
        linea = linea.rstrip()
        palabras = linea.split()
        for i in palabras:
            if i not in lista_palabras:
                lista_palabras.append(i)
                           
    lista_palabras.sort(key= str.lower)
    print(lista_palabras)
# // Actividad 7.3

# Actividad 7.4
def act4():
    listad = []
    numeros = input("Ingresa un numero: ")
    listad.append(numeros)
    while numeros != "hecho":
        numeros = input("Ingresa un numero: ")
        listad.append(numeros)
    listad.remove('hecho')
    print("Minimo: ",min(listad,key=int))
    print("Maximo: ",max(listad,key=int))
    print(listad)
# //Actividad 7.4

# Recursos
lista = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
lista1 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

# Impresiones
print(recortar(lista))
print(medio(lista1))

# Llamada a funciones
act2()
act3()
act4()