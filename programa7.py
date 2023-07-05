print("Programa7. \nPrograma que calcula el volumen de un prisma rectangular \n")
i1 = float(input("Escriba el valor de Largo "))
i2 = float(input("Escriba el valor de Ancho "))
i3 = float(input("Escriba el valor de la Altura "))

Largo = float(i1)
Ancho = float(i2)
Altura = float(i3)

Vol = Largo * Ancho * Altura

VolR = round(Vol,4)

print("El volumen de un prisma rectangular ",VolR) 
