print("Programa14. \n Programa para calcular el costo total de compra de combustible \n")

Pgasolina = float(input("Escriba el precioDeLaGasolina: "))
Clitros = float(input("Escriba la Clitros: "))

costoSinImpuesto = Pgasolina * Clitros 
costoTotal = costoSinImpuesto * 1.07

print("El costoTotal a pagar es: ", round(costoTotal, 2))