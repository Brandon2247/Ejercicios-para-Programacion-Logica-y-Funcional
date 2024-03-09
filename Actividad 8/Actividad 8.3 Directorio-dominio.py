fname = input('Ingresa un nombre de archivo: ')
fhan = open(fname)
def analizador(linea):
    if linea.startswith('From ') == True:
       c=((linea.split())[1])
       c2=((c.split('@'))[1])
       cou[c2] = cou.get(c2, 0)+1
cou = dict()
list(map(analizador,fhan))
print(cou)