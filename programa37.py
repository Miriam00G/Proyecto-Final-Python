Contador = 0
Total = 0

while Contador <5:
    Precio = float(input("Ingrese el precio del articulo: "))
    Impuesto = Precio * 0.07
    Total = Impuesto
    Contador += 1
    
print("El total de impuestos a pagar es:", Total)