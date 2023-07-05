def Programa1():
    print("Programa 1 \n para intercambiar variables \n")
    a = 7
    b = 0
    c = 0
    b = a
    c = b
    a = a
    return a, b, c

def Programa2():
    print("Programa 2 \n para asignar variables \n ")
    A = 10
    B = 20
    AUX = 0
    AUX = A
    A = B
    B = AUX
    return A,B,AUX

def Programa3(a,b,c):
    print("Programa 3 \n ")
    d = (a + b + c) / 3
    return d

def Programa4():
    print("Programa 4 \n que calcula el area de un triangulo \n")
    Base = 2
    Altura = 7
    Area = (Base * Altura ) / 2
    return Area

def Programa5(AB, BC, CD, DA):
    print("Programa 5 \n Programa que calcula el perimetro de un rectangulo \n")
    P = AB + BC + CD + DA
    return P

def Programa6(Base1, Base2, Altura):
    print("Programa 6 \n Programa que calcula el area de un trapecio \n")
    A = ((Base1 + Base2)*Altura)/2
    return A
    
def Programa7(Largo, Ancho, Altura):
    print("Programa7 \nPrograma que calcula el volumen de un prisma rectangular \n")
    Vol = Largo * Ancho * Altura
    return Vol
    
def Programa8(x):
    print("Programa8 \nPrograma que resuelva cada ecuacion de un valor x \n")
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) -5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) -5)/7)
    return A, B, C, D, E, F

def Programa9(a,b,c):
    print("Programa9. \nPrograma que resuelva un valor x y y \n ")
    C1 = (4 * a) + (3 * b)
    C2 = (21 * a) - 18 + (8 * b) - 5
    C3 = (4 * a) + (3 * b) + 7
    C4 = (2 * a) + (3 * b) - (c **5)
    C5 = (2 * a) + (3 * b) - (c **2)
    return(C1,C2,C3,C4,C5)
    
def Programa10(metros):
    print("Programa10 \n Programa que convierta una cantidad de metros a pies y metros a pulgadas \n")
    pies = metros * 3.281
    pulgadas = metros * 39.37
    return pies, pulgadas

def Programa11(A1,B2,C3):
    print("Programa11 \n Programa de regla de tres simple \n")
    x = (B2 * C3) / A1
    return x

def Programa12(tasaM,montoP,plazoPorMes):
    print("Programa12 \n Programa que calcule el interes a pagar por un prestamo \n")
    tasaporcentaje = tasaM * 100
    tasaM = tasaM / 12
    cuota = montoP * (tasaM / (1-(1 + tasaM) ** (-plazoPorMes)))
    interesMensual = montoP * tasaM
    CapitalMensual = cuota - interesMensual
    return cuota, interesMensual, CapitalMensual

def Programa13(salarioBruto):
    print("Programa13 \n Programa para calcular el salario neto de empleados \n")
    seguroSocial = salarioBruto * 0.05
    seguroEducativo = salarioBruto * 0.02
    cuotaPrestamo = 50
    salarioNeto = salarioBruto - seguroSocial - seguroEducativo - cuotaPrestamo
    return salarioNeto

def Programa14():
    print("Programa14 \n Programa para calcular el costo total de compra de combustible \n")
    costoSinImpuesto = Pgasolina * Clitros
    costoTotal = costoSinImpuesto * 1.07
    return costoSinImpuesto, costoTotal

def Programa15():
    print("Programa15. \n Programa que de el total de la compra con el impuesto \n")
    PrecioA = Articulo1 + Articulo2 + Articulo3
    Impuesto = PrecioA * 1.07
    return (totalSinImpuesto, totalDeCompra)

def Programa16():
    print("Programa16. \n algoritmo para saber la nota final \n")
    Nfinal = float ((N1 + N2 + N3 + N4 + N5) / 100)
    return Nfinal

def Programa17():
    print("Programa17. \n Conversion de unidades de medidas ")
    Gramos = unidad / 0.001
    Kilogramos = unidad / 1000
    Centimetros = unidad / 0.01
    Metros = unidad / 100
    return (Gramos,Kilogramos,Centimetros,Metros)

def Programa18():
    print("Programa18. \nCalculo del interes compuesto ")
    Cf = ci * (1 + i) ** n
    return Cf

def Programa19():
    print("programa 19. \n calcular la compra de 5 articulos \n ")
    CompraSinImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA )
    CompraConImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) * 0.07
    PromedioDeLaCompra = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) / 5


    






    


    

    

    
    

    

    
    
    
    
    