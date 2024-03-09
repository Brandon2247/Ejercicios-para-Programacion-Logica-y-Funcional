def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

inicio = int(input("Primer Rango de años: "))
fin = int(input("Segundo Rango de años: "))
print(f"Imprimiendo años bisiestos del {inicio} al {fin}")

for anio in range(inicio, fin+1):
    if es_bisiesto(anio):
        print(anio, end=", ")
