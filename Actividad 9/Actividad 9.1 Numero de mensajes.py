fname = input('Ingresa un nombre de archivo: ')
fhan = open(fname)
def analizador(linea):
    if linea.startswith('From ') == True:
        c=((linea.split())[1])
        cou[c] = cou.get(c, 0)+1
cou = dict()
list (map(analizador,fhan))

#print(cou)
def tupla(x):
    key,val = x
    return val,key

Y=list(map(tupla,list(cou.items())))
Y.sort(reverse=True)

def prin(a):
    cantidad, email = a
    print(email, cantidad)
list(map(prin, Y[:1]))