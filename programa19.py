print("programa 19. \n calcular la compra de 5 articulos \n ")
A1 = float(input("Escriba el valor del PrimerArticulo "))
A2 = float(input("Escriba el valor del SegundoArticulo "))
A3 = float(input("Escriba el valor del TercerArticulo "))
A4 = float(input("Escriba el valor del CuartoArticulo "))
A5 = float(input("Escriba el valor del QuintoArticulo "))

CompraSinImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA )
CompraConImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) * 0.07
PromedioDeLaCompra = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) / 5

print("El total de la compra sin impuesto es de: ", round(CompraSinImpuesto, 2))
print("El total de la compra con impuesto es de: ", round(CompraConImpuesto, 2))
print("El promedio de la compra sin impuesto es de: ", round(PromedioDeLaCompra, 2))