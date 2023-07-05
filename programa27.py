# Programa 26 Clasificacion de Triangulos

LadoA = float(input("Escriba valor del 1lado "))
LadoB = float(input("Escriba valor del 2lado "))
LadoC = float(input("Escriba valor del 3lado "))

if LadoA == LadoB == LadoC:
    print("Es un Triangulo Equilatero")
elif LadoA == LadoB or LadoB == LadoC or LadoA == LadoC:
    print("Es un Triangulo Isosceles")
else:
    print("Es un Triangulo Escaleno")

print(" \n Fin del Programa")
