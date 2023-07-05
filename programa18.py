print("Programa18. \nCalculo del interes compuesto ")

Ci = float(input("Ingrese la capital inicial "))
i = float(input("Ingrese la tsa de interes "))
n = float(input("Ingrese el periodo de ahorro "))

Cf = ci * (1 + i) ** n

prin(f"La capital final es de {round(Cf,2)} ")