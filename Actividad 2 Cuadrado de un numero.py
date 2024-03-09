def cuadrado(n):
    return n**2

print(list(map(cuadrado,[1,2,3,4,5])))

# Si se desea utilizar la funcion Lambda, el resultado seria lo siguiente:

print(list(map(lambda n: n**2,range(1,11))))