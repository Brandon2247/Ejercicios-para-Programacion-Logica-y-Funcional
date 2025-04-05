def descuento(elemento):
    clave,valor=elemento.items()
    return (clave[1]*valor[1]/100)
    #return precio - (precio * porcentaje/100)

def iva(elementos):
    clave,valor=elementos.items()
    return (clave[1]*16/100)+clave[1]
    

def precioCesta(aux, funcion):
    return sum(list(map(funcion,aux)))

cesta = [{'manzana':40, 'porcentaje':8}, {'azucar':50, 'porcentaje':10},
        {'cebolla':30, 'porcentaje':4},{'cebolla':30, 'porcentaje':50}]
print('Total precio con descuento: ', precioCesta(cesta, descuento))
print('Total precio con IVA: ', precioCesta(cesta, iva))