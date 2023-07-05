print("programa 20. \n Calcular salario neto de sus empleados \n ")
i1 = input("Escribir valor de salario bruto ")

SalarioB = float(i1)

SeguroS = SalarioB * 0.08
SeguroE = SalarioB * 0.02
Impuesto = SalarioB * 0.15
Prestamo = 100

SalarioN = SalarioB - SeguroS - SeguroE - Impuesto - Prestamo


print(" El salario neto a pagar es de: ", round(SalarioN, 2))
