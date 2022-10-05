def divisible(t,n):
    return(t % n == 0)

def bisiesto(a):
    return(divisible(a,4) and (not(divisible(a,100)) or divisible(a,400)))

def meses(a):
    if(bisiesto(a)):
        feb = 29
    else:
        feb = 28
    anno = [31,feb,31,30,31,30,31,31,30,31,30,31]
    return(anno)

def take(numMes,a):
    return(meses(a)[:numMes])

def numeroDia(d,m,a):
    return(((a-1)*365
            +(a-1)//4
            -(a-1)//100
            +(a-1)//400
            +sum(take(m-1,a))
            +d)%7)

print("Introduce la fecha: ")
d = int(input("dia: "))
m = int(input("mes: "))
a = int(input("año: "))
diaSemana = numeroDia(d,m,a)
if diaSemana == 0:
    print("Domingo")
if diaSemana == 1:
    print("Lunes")
if diaSemana == 2:
    print("Martes")
if diaSemana == 3:
    print("Miercoles")
if diaSemana == 4:
    print("Jueves")
if diaSemana == 5:
    print("viernes")
if diaSemana == 6:
    print("Sabado")
