def actividad3():
    diccionario2 = dict()
    fname = input('Ingresa el nombre del archivo: ')
    correo = open(fname)
    for linea in correo:
        linea = linea.lower()
        palabras = linea.split()
        for cont in palabras:
            for contador in cont:
                if contador.isalpha():
                    if contador not in diccionario2:
                        diccionario2[contador] = 1
                    else:
                        diccionario2[contador] += 1
    
    print(sorted(diccionario2.items()))

actividad3()