lista =[]

while True:
    dato = str(input("Ingresa un valor entero para la lista: "))
    if dato != 'hecho':
        lista.append(int(dato))
        lista.sort()
    if dato =='hecho':
        print("Elementos ordenados de la lista:", lista)
        minimo = lista.pop(0)
        maximo = lista.pop(len(lista)-1)
        print("Valor minimo en la lista: ", minimo)
        print("Valor maximo en la lista: ", maximo)