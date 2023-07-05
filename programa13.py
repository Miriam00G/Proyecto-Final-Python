print("Programa13. \n Programa para calcular el salario neto de empleados \n")
a1 = float(input("Escriba el valor de salarioBruto "))
salarioBruto = float(a1)

seguroSocial = salarioBruto * 0.05
seguroEducativo = salarioBruto * 0.02
cuotaPrestamo = 50
salarioNeto = salarioBruto - seguroSocial - seguroEducativo - cuotaPrestamo

print("El salario neto a pagar es de: ",salarioNeto)