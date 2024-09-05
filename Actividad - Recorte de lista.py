lista_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def recortar(lista_1):
    print("Lista original",lista_1)
    penultimo = (len(lista_1)-1) #Se resta uno para convertir el tamano de la lista en la penultima posicion.
    lista_1 = lista_1[1:penultimo]
    print("Lista modificada", lista_1)

print("funcion recortar")
recortar(lista_1)
print("Funcion medio")

def medio(lista_1):
    print("Lista original",lista_1)
    penultimo = (len(lista_1)-1) #Se resta uno para convertir el tamano de la lista en la penultima posicion.
    nueva_Lista = lista_1[1:penultimo]
    print("Lista modificada", nueva_Lista)

medio(lista_1)