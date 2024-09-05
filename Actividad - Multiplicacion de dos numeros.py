def multiplicador(n):
    return (int (a)*n)

a= input('Ingresa el numero a multiplicar: ')
print(list(map(multiplicador,range(1,11))))

# Si se desea utilizar la funcion Lambda, esta misma funcion quedaria de la siguiente manera

print(list(map(lambda n, a = input('\nIngresa otro numero: '): int (a)*n,range(1,11))))