def actividad2():
    diccionario2 = dict()
    fname = input('Ingresa el nombre del archivo: ')
    correo = open(fname)
    for linea in correo:
        palabras = linea.split()
        for cont in palabras:
            if palabras[0] == 'From' and palabras[5] == cont:
                hora,minutos,segundos = cont.split(':')
                if hora not in diccionario2:
                    diccionario2[hora] = 1
                else:
                    diccionario2[hora] += 1
    lista = list()
    for clave, valor in list(diccionario2.items()):
        lista.append((valor,clave))
    for clave, valor in lista:
        print(valor,clave)

actividad2()