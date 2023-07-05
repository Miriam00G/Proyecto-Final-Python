print("Programa12. \n Programa que calcule el interes a pagar por un prestamo \n")
i1 = input("Escribir Monto: ")
i2 = input("Escribir Tasa: ")
i3 = input("Escribir Plazo: ")

montoP = float(i1)
tasaM = float(i2)
plazoPorMes = float(i3)

tasaporcentaje = tasaM * 100
tasaM = tasaM / 12
cuota = montoP * (tasaM / (1-(1 + tasaM) ** (-plazoPorMes)))
interesMensual = montoP * tasaM
CapitalMensual = cuota - interesMensual

print("El resultado de cuota es ",round(cuota,2))
print("El resultado de interesMensual es ",round(interesMensual, 2))
print("El resultado de CapitalMensual es ",round(CapitalMensual, 2))



