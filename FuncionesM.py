def Programa1():
    print("Programa 1 \n para intercambiar variables \n")
    a = 7
    b = 0
    c = 0
    b = a
    c = b
    a = a
    return a, b, c
    print("-------------------------------------------------")
    
def Programa2():
    print("Programa 2 \n para asignar variables \n ")
    A = 10
    B = 20
    AUX = 0
    AUX = A
    A = B
    B = AUX
    return A,B,AUX
    print("-------------------------------------------------")
    
def Programa3():
    print("Programa3 ")
    a = float(input("Leer A: "))
    b = float(input("Leer B: "))
    c = float(input("Leer C: "))
    d = (a + b + c) / 3
    return round(d, 2)
    print("-------------------------------------------------")
    
def Programa4():
    print("Programa4 que calcula el area de un triangulo \n")
    Base = float(input("Escriba el valor de la Base "))
    Altura = float(input("Escriba el valor de la Altura "))
    Area = (Base * Altura ) / 2
    return round(Area, 2)
    print("-------------------------------------------------")
    
def Programa5():
    print("Programa5 que calcula el perimetro de un rectangulo \n")
    AB = float(input("Escriba el valor AB "))
    BC = float(input("Escriba el valor BC "))
    CD = float(input("Escriba el valor CD "))
    DA = float(input("Escriba el valor DA "))
    P = AB + BC + CD + DA
    return round(P,2)
    print("-------------------------------------------------")
    
def Programa6():
    print("Programa6 que calcula el area de un trapecio \n")
    Base1 = float(input("Escriba el valor de Base 1 "))
    Base2 = float(input("Escriba el valor de Base 2 "))
    Altura = float(input("Escriba el valor de la Altura "))
    Area = ((Base1 + Base2) * Altura) / 2
    return round(Area, 2)
    print("-------------------------------------------------")
    
def Programa7():
    print("Programa7 que calcula el volumen de un prisma rectangular \n")
    Largo = float(input("Escriba el valor de Largo "))
    Ancho = float(input("Escriba el valor de Ancho "))
    Altura = float(input("Escriba el valor de la Altura "))
    Vol = Largo * Ancho * Altura
    return round(Vol, 2)
    print("-------------------------------------------------")
    
def Programa8():
    print("Programa8 que resuelva cada ecuacion de un valor x \n")
    x = float(input("Escriba el valor de x: "))
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) -5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) -5)/7)
    return A, B, C, D, E, F
    print("-------------------------------------------------")

def Programa9():
    print("Programa9 que resuelva un valor x y y \n ")
    a = float(input("Escriba el valor de a "))
    b = float(input("Escriba el valor de b "))
    c = float(input("Escriba el valor de c "))
    C1 = (4 * a) + (3 * b)
    C2 = (21 * a) - 18 + (8 * b) - 5
    C3 = (4 * a) + (3 * b) + 7
    C4 = (2 * a) + (3 * b) - (c **5)
    C5 = (2 * a) + (3 * b) - (c **2)
    return(C1,C2,C3,C4,C5)
    print("-------------------------------------------------")
    
def Programa10():
    print("Programa10 que convierta una cantidad de metros a pies y metros a pulgadas \n")
    metros = float(input("Escriba el valor de metros: "))
    pies = metros * 3.281
    pulgadas = metros * 39.37
    return pies, pulgadas
    print("-------------------------------------------------")
    
def Programa11():
    print("Programa11 regla de tres simple \n")
    A1 = float(input("Escriba el valor de A1 "))
    B2 = float(input("Escriba el valor de B2 "))
    C3 = float(input("Escriba el valor de C3 "))
    x = (B2 * C3) / A1
    return x
    print("-------------------------------------------------")
    
def Programa12():
    print(" Programa12 que calcule el interes a pagar por un prestamo \n")
    montoP = float(input("Escribir Monto: "))
    tasaM = float(input("Escribir Tasa: "))
    plazoPorMes = float(input("Escribir Plazo: "))
    tasaporcentaje = tasaM * 100
    tasaM = tasaM / 12
    cuota = montoP * (tasaM / (1-(1 + tasaM) ** (-plazoPorMes)))
    interesMensual = montoP * tasaM
    CapitalMensual = cuota - interesMensual
    return cuota, interesMensual, CapitalMensual
    print("-------------------------------------------------")
    
def Programa13():
    print("Programa13 para calcular el salario neto de empleados \n")
    salarioBruto = float(input("Escriba el valor de salarioBruto "))
    seguroSocial = salarioBruto * 0.05
    seguroEducativo = salarioBruto * 0.02
    cuotaPrestamo = 50
    salarioNeto = salarioBruto - seguroSocial - seguroEducativo - cuotaPrestamo
    return salarioNeto
    print("-------------------------------------------------")
    
def Programa14():
    print("Programa14 para calcular el costo total de compra de combustible \n")
    Pgasolina = float(input("Escriba el precioDeLaGasolina: "))
    Clitros = float(input("Escriba la Clitros: "))
    costoSinImpuesto = Pgasolina * Clitros
    costoTotal = costoSinImpuesto * 1.07
    return costoSinImpuesto, costoTotal
    print("-------------------------------------------------")
    
def Programa15():
    print("Programa15 que de el total de la compra con el impuesto \n")
    Articulo1 = float(input("Escribir valor del articulo1: "))
    Articulo2 = float(input("Escribir valor del articulo2: "))
    Articulo3 = float(input("Escribir valor del articulo3: "))
    PrecioA = Articulo1 + Articulo2 + Articulo3
    Impuesto = PrecioA * 1.07
    return PrecioA,Impuesto
    print("-------------------------------------------------")
    
def Programa16():
    print("Programa16 Algoritmo para saber la nota final \n")
    N1 = float(input("Escribir primera evaluacion: "))
    N2 = float(input("Escribir segunda evaluacion: "))
    N3 = float(input("Escribir tercera evaluacion: "))
    N4 = float(input("Escribir cuarta evaluacion: "))
    N5 = float(input("Escribir quinta evaluacion: "))
    Nfinal = float ((N1 + N2 + N3 + N4 + N5) / 100)
    return Nfinal
    print("-------------------------------------------------")
    
def Programa17():
    print("Programa17 Conversion de unidades de medidas ")
    unidad = float(input("Ingrese la cantidad: "))
    Gramos = unidad / 0.001
    Kilogramos = unidad / 1000
    Centimetros = unidad / 0.01
    Metros = unidad / 100
    return (Gramos,Kilogramos,Centimetros,Metros)
    print("-------------------------------------------------")
    
def Programa18():
    print("Programa18 Calcular el interes compuesto ")
    capitalInicial = float(input("Ingrese el capital inicial "))
    Interes = float(input("Ingrese la tasa de interes "))
    periodoAhorro = float(input("Ingrese el periodo de ahorro "))
    capitalFinal = round(capitalInicial * (1 + Interes) ** periodoAhorro, 2)
    return capitalFinal
    print("-------------------------------------------------")
    
def Programa19():
    print("programa 19 Calcular la compra de 5 articulos \n ")
    PrimerA = float(input("Escriba el valor del PrimerArticulo "))
    SegundoA = float(input("Escriba el valor del SegundoArticulo "))
    TercerA = float(input("Escriba el valor del TercerArticulo "))
    CuartoA = float(input("Escriba el valor del CuartoArticulo "))
    QuintoA = float(input("Escriba el valor del QuintoArticulo "))    
    CompraSinImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA )
    CompraConImpuesto = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) * 0.07
    PromedioDeLaCompra = (PrimerA + SegundoA+ TercerA + CuartoA + QuintoA ) / 5
    return (CompraSinImpuesto,CompraConImpuesto,PromedioDeLaCompra)
    print("-------------------------------------------------")
    
def Programa20():
    print("programa20 Calcular salario neto de empleados \n ")
    SalarioB = float(input("Escribir valor de salario bruto "))
    SeguroS = SalarioB * 0.08
    SeguroE = SalarioB * 0.02
    Impuesto = SalarioB * 0.15
    Prestamo = 100
    SalarioN = SalarioB - SeguroS - SeguroE - Impuesto - Prestamo
    return SalarioN
    print("-------------------------------------------------")
    
def Programa21():
    print("Programa21 Calcular si una persona paga impuestos \n ")
    salario = float(input(" Escriba el Salario: "))
    if salario > 3000:
        impuesto = salario * 1.07
        return('Esta Persona debe abonar impuestos',impuesto)
    else:
        return('No debe abonar impuestos')
    print("-------------------------------------------------")
    
def Programa22():
    print("Programa22 Calcular temperatura \n ")
    temperatura = float(input(" Escriba la temperatura: "))
    if temperatura < 20:
        if temperatura < 10:
            return('Nivel azul')
        else:
            return('Nivel verde')
    else:
        if temperatura < 30:
            return('Nivel naranja')
        else:
            return('Nivel rojo')
    print("-------------------------------------------------")
    
def Programa23():
    print("Programa23 Mostrar si una persona es mayor \n ")
    edad = int(input("Escriba la edad de una persona: "))
    if edad < 20:
        return('menor de edad')
    else:
        return('mayor de edad')
    print("-------------------------------------------------")
    
def Programa24():
    print("Programa24 Calcular el numero mayor \n ")
    a = int(input("escribe el 1numero "))
    b = int(input("escribe el 2numero "))
    c = int(input("escribe el 3numero "))
    if a > b and a > c:
        return('el numero mayor es a = ', a)
    if b > a and b > c:
        return('el numero mayor es b = ', b)
    if c > a and c > b:
        return('el numero mayor es c = ', c)
    print("-------------------------------------------------")
    
def Programa25():
    print("Programa25 Calculadora de descuentos \n ")
    PrecioProducto = float(input("Escriba el precio original del producto "))
    Porcentaje = float(input("Escriba el porcentaje de descuento "))
    Porcentaje/100
    Porcentaje = PrecioProducto * Porcentaje/100
    PrecioFinal = PrecioProducto - Porcentaje
    if PrecioProducto < 50:
        return("Oferta Especial", PrecioFinal)
    else:
        return("Precio Final", PrecioFinal)
    print("-------------------------------------------------")
    
def Programa26():
    print("Programa26 Calcular lados de un triangulo \n ")
    LadoA = float(input("Escriba valor del 1lado "))
    LadoB = float(input("Escriba valor del 2lado "))
    LadoC = float(input("Escriba valor del 3lado "))
    if LadoA == LadoB == LadoC:
        return("Es un Triangulo Equilatero")
    elif LadoA == LadoB or LadoB == LadoC or LadoA == LadoC:
        return("Es un Triangulo Isosceles")
    else:
        return("Es un Triangulo Escaleno")
    print("-------------------------------------------------")
    
def Programa27():
    print("Programa27 Solicitar al usuario ingresar un numero \n ")
    numero = int(input("Escribir un numero: "))
    if numero > 0:
        return("numero es positivo ")
    elif numero == 0:
        return("numero es cero ")
    else:
        return("numero es negativo ")
    print("-------------------------------------------------")
    
def Programa28():
    print("Programa28 Solicitar al usuario ingresar una calificacion \n ")
    calificacion = float(input("Escribir una calificacion: "))
    if  90 <= calificacion <= 100:
        print("Su calificacion es una A")
    elif  80 <= calificacion <= 89:
        print("Su calificacion es una B")
    elif 70 <= calificacion <= 79:
        print("Su calificacion es una C")
    elif 60 <= calificacion <= 69:
        print("Su calificacion es una D")
    else:
        print("Su calificacion es una F")
    return None
    print("-------------------------------------------------")
    

def Programa29():
    print("Programa29 \n ")
    C = float(input("Escriba la calificacion: "))
    if 90 <= C <= 100:
        print("Su evaluacion es una A")
    elif 80 <= C <= 89:
        print("Su evaluacion es una B")
    elif 70 <= C <= 79:
        print("Su evaluacion es una C")
    elif 60 <= C <= 69:
        print("Su evaluacion es una D")
    else:
        print("Su evaluacion es una F")
    print("-------------------------------------------------")
    
def Programa30():
    print("Programa30 \n ")
    numero = int(input("Escribir un numero: "))
    if numero > 0:
        print("El numero es positivo ")
    elif numero == 0:
        print("El numero es cero ")
    else:
        print("El numero es negativo ")
    print("-------------------------------------------------")
    
def Programa31():
    print("Programa31 \n ")
    value = 1
    while value <= 10:
        print(value)
        if value == 7:
            break
        value += 1
    print("-------------------------------------------------")
   
def Programa32():
    Calificacion = int(input("Ingrese el numero de la calificacion a evaluar: "))
    
    for i in range(Calificacion):
        Calificacion = float(input("Ingrese la calificacion: "))
        
    if Calificacion >= 90 and Calificacion <= 100:
        letra = "A"
    elif Calificacion >= 80 and Calificacion <= 89:
        letra = "B"
    elif Calificacion >= 70 and Calificacion <= 79:
        letra = "C"
    elif Calificacion >= 60 and Calificacion <= 69:
        letra = "D"
    else:
        letra = "F"
    print(f"La Calificacion es {letra}")
    return None
    print("-------------------------------------------------")
    
def Programa33():
    print("Programa33 \n ")
    for i in range(1, 13):
        print("Tabla de multiplicar del", i)
        print("----------------------------")
        for  j in range(1, 13):
            resultado = i * j
            print(i, "x", j, "=", resultado)
            print()
    return None
    print("-------------------------------------------------")
    
def Programa34():
    print("Programa34 \n ")
    numero = 1
    while numero <= 15:
        print(numero)
        if numero % 2 == 0:
            print('Numero es impar')
        else:
            print('Numero es par')
        numero += 1
    return None
    print("-------------------------------------------------")
    
def Programa35():
    print("Programa35 Numeros del 1 al 10 \n ")
    numero = 0
    while numero <= 15:
        if numero %2 == 0:
            print(f"El numero {numero} es un numero par")
        else:
            print(f"El numero {numero} es un numero impar")
        numero += 1
    return None
    print("-------------------------------------------------")
    
def Programa36():
    print("Programa36 Lista de numeros \n ")
    Numeros = list(range(1, 11))
    for Numero in Numeros:
        if Numero > 5:
            print(f"El numero {Numero} es mayor ")
        elif Numero <= 0:
            print(f"El numero {Numero} es menor o igual a cero ")
        else:
            print(f"El numero {Numero} es menor ")
            
        if Numero == 9:
            break
    return None
    print("-------------------------------------------------")
    
def Programa37():
    print("Programa37 \n ")
    Contador = 0
    Total = 0
    
    while Contador < 5:
        Precio = float(input("Ingrese el precio del articulo: "))
        Impuesto = Precio * 0.07
        Total = Impuesto
        Contador += 1
    return Total
    print("-------------------------------------------------")
    
def Programa38():
    print("Programa38 \n ")
    Suma = 0
    for Numero in range(2, 21, 2):
        Suma += Numero
    return Suma
    print("-------------------------------------------------")
    
def Programa39():
    Base = float(input("Escriba el valor de la Base "))
    Altura = float(input("Escriba el valor de la Altura "))
    Area = (Base * Altura)/ 2
    return Area
    print("-------------------------------------------------")
    
print("Fin de los Programas \n ")