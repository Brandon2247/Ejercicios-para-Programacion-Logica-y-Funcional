# Actividad 5: Redondear al peso mas cercano. 

# Solicitud de valores
chicles = int(input("Ingrese la cantidad de chicles: "))
cerillos = int(input("Ingrese la cantidad de cerillos: "))
jabon = int(input("Ingrese la cantidad de los kilos de jabon : "))

# Calcular el Subtotal de los productos.
def subtotal(chicles, cerillos, jabon):
    return ((chicles)*0.80+(cerillos)*1.26+(jabon)*18.45)
print("\nEl subtotal del la compra es: ",subtotal(chicles, cerillos, jabon))

# Se añade el IVA del subtotal.
def iva():
    return subtotal(chicles, cerillos, jabon)*0.16
print("Iva: ",iva())

# Se calcula el valor total de los productos (En caso de valor decimal, se redondea).
def total():
    return subtotal(chicles, cerillos, jabon)+iva()
print("Total: ",round(total()))