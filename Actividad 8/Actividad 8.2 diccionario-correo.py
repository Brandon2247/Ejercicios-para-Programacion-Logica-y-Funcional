fname = input('Ingresa un nombre de archivo: ')
fhan = open(fname)
def analizador(linea):
    if linea.startswith('From ') == True:
       c=((linea.split())[1])
       cou[c] = cou.get(c, 0)+1
cou = dict()
list(map(analizador,fhan))
print(cou)