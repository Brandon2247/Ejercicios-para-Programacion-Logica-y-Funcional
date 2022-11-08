#Ejercicio 8.1 - Mostrar clasificacion cada mensaje de correo dependiendo del día de la semana en que se recibió

fname = input('Ingresa un nombre de archivo: ')

fhand = open(fname)
def analizador(linea):
    if linea.startswith('From ') == True:
       c=((linea.split())[2])
       cou[c] = cou.get(c, 0)+1
cou = dict()
list(map(analizador,fhand))
print(cou)