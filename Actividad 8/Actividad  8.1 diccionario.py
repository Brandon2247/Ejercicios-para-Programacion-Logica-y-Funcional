


fname = input('Ingresa un nombre de archivo: ')

fhand = open(fname)
#ejecicio 1
def analizador(linea):
    if linea.startswith('From ') == True:
       c=((linea.split())[2])
       cou[c] = cou.get(c, 0)+1
cou = dict()
list(map(analizador,fhand))
print(cou)



