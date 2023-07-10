#  Importar funciones desde la carpeta "Funciones_M.py"
from FuncionesM import Programa1, Programa2, Programa3, Programa4, Programa5, Programa6, Programa7, Programa8, Programa9, Programa10, Programa11, Programa12, Programa13, Programa14, Programa15, Programa16, Programa17, Programa18, Programa19, Programa20, Programa21, Programa22, Programa23, Programa24, Programa25, Programa26, Programa27, Programa28, Programa29, Programa30, Programa31, Programa32, Programa33, Programa34, Programa35, Programa36, Programa37, Programa38, Programa39
# Menu De Programas
print("Menu De Programas: ")
print("1. Programa1: Intercambiar valores")
print("2. Programa2: Asignar variables")
print("3. Programa3: Resultado de 3 valores")
print("4. Programa4: Calculo del area de un triangulo")
print("5. Programa5: Calculo de un perimetro de un rectangulo")
print("6. Programa6: Calculo del area de un trapecio")
print("7. Programa7: Calculo del volumen de un prisma rectangular")
print("8. Programa8: Resolucion de un valor x")
print("9. Programa9: Resolucion de un valor x y y")
print("10. Programa10: Conversion de unidades de medidas")
print("11. Programa11: Regla de tres simple")
print("12. Programa12: Interes a pagar por un prestamo")
print("13. Programa13: Calculo de salario neto de empleados")
print("14. Programa14: Costo total de la compra de combustible ")
print("15. Programa15: Compra total con el impuesto")
print("16. Programa16: Algoritmo de nota final")
print("17. Programa17: Conversion de unidades de medidas")
print("18. Programa18: Calculo de interes compuesto")
print("19. Programa19: Calculo por la compra de 5 articulos")
print("20. Programa20: Calculo salario de empleados")
print("21. Programa21: Calcular si una persona paga impuestos")
print("22. Programa22: Calcular temperatura")
print("23. Programa23: Mostrar si una persona es mayor")
print("24. Programa24: Calcular numero mayor")
print("25. Programa25: Calculadora de descuentos")
print("26. Programa26: Calculo de los lados de un triangulo")
print("27. Programa27: Solicitar al usuario ingresar un numero")
print("28. Programa28: Solicitar al usuario ingresar una calificacion")
print("29. Programa29: Saber calificaciones")
print("30. Programa30: Saber cuando un numero es positivo, negativo o cero")
print("31. Programa31: Numeros del 1 al 7")
print("32. Programa32: Calificacion a evaluar")
print("33. Programa33: Tablas de multiplicar del 1 al 12")
print("34. Programa34: Saber cuando un numero es par o impar")
print("35. Programa35: Numeros del 1 al 10")
print("36. Programa36: Lista de numeros")
print("37. Programa37: Total de un impuesto a pagar")
print("38. Programa38: Sumar numeros pares")
print("39. Programa39: Calculo de area de un triangulo")
print("--------------------------------------------------------------------------")

#Bucle Principal
while True:
    #Se pide al usuario ingresar el Nombre del Programa que desea llamar
    Nombre_Programa = input("Ingrese el Nombre del Programa que desea llamar (o 'salir' para cerrar):")
    
    #Se usan estructuras condicionales para determinar que funcion llamar
    if Nombre_Programa == "salir":
        break
    elif Nombre_Programa == "Programa1":
        resultado = Programa1()
        print(f"El intercambiar valores de a, b y c es:{resultado} ")
        print("------------------------------------------------------------------")
    elif Nombre_Programa == "Programa2":
        resultado = Programa2()
        print(f" para asignar variables de A, B y AUX es: {resultado} ")
        print("------------------------------------------------------------------")
    elif Nombre_Programa == "Programa3":
        resultado = Programa3()
        print(f"El resultado del programa3 es: {resultado} ")
        print("------------------------------------------------------------------")
    elif Nombre_Programa == "Programa4":
        resultado = Programa4()
        print(f"El resultado de el area de un triangulo es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa5":
        resultado = Programa5()
        print(f"El resultado de el area del perimetro de un rectangulo es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa6":
        resultado = Programa6()
        print(f"El resultado de el area de el area de un trapecio es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa7":
        resultado = Programa7()
        print(f"El volumen de un prisma rectangular es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa8":
        A, B, C, D, E, F = Programa8()
        print(f"El resultado a es: {A} ")
        print(f"El resultado b es: {B} ")
        print(f"El resultado c es: {C} ")
        print(f"El resultado d es: {D} ")
        print(f"El resultado e es: {round(E, 2)} ")
        print(f"El resultado f es: {round(F, 2)} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa9":
        C1, C2, C3, C4, C5 = Programa9()
        print(f"El resultado de un valor x y y es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa10":
        pies, pulgadas = Programa10()
        print(f"El resultado en pies es de: {pies} ")
        print(f"El resultado en pulgadas es de: {round(pulgadas, 2)} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa11":
        resultado = Programa11()
        print(f"El resultado de una regla de tres simple es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa12":
        montoP, tasaM, plazoPorMes = Programa12()
        print(f"El monto es: {montoP} Dolares")
        print(f"La tasa mensual es: {tasaM} Dolares")
        print(f"El plazo por mes es de: {plazoPorMes} Dolares")
        print("-----------------------------------------------------------------")    
    elif Nombre_Programa == "Programa13":
        resultado = Programa13()
        print(f"El salario neto de empleados es de: {resultado} ")
        print("-----------------------------------------------------------------") 
    elif Nombre_Programa == "Programa14":
        costoSinImpuesto, costoTotal = Programa14()
        print(f"El costo sin impuesto es de: {costoSinImpuesto} ")
        print(f"El costo total es de: {costoTotal} ")
        print("-----------------------------------------------------------------") 
    elif Nombre_Programa == "Programa15":
        resultado = Programa15()
        print(f"El total de una compra con impuesto es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa16":
        resultado = Programa16()
        print(f"El resultado de una nota final es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa17":
        gramos, kilogramos, centimetros, metros = Programa17()
        print(f"El resultado de gramos es: {gramos} ")
        print(f"El resultado de kilogramos es: {kilogramos} ")
        print(f"El resultado de centimetros es: {centimetros} ")
        print(f"El resultado de metros es: {metros} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa18":
        resultado = Programa18()
        resultado_redondeado = round(resultado, 2)
        print(f"El resultado de un interes compuesto es de: {resultado_redondeado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa19":
        CompraSinImpuesto,CompraConImpuesto,PromedioDeLaCompra = Programa19()
        print(f"Por la compra de 5 articulos sin impuesto es de: {CompraSinImpuesto} ")
        print(f"Por la compra de 5 articulos con impuesto es de: {CompraConImpuesto} ")
        print(f"El promedio de una compra de 5 articulos es de: {PromedioDeLaCompra} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa20":
        resultado = Programa20()
        print(f"El salario neto de empleados es de: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa21":
        resultado = Programa21()
        print(f"Saber si una persona paga impuesto: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa22":
        resultado = Programa22()
        print(f"Al calcular una temperatura es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa23":
        resultado = Programa23()
        print(f"Saber si una persona es mayor o menor: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa24":
        resultado = Programa24()
        print(f"El resultado al calcular si un numero es mayor es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa25":
        resultado = Programa25()
        print(f"El resultado de un producto con impuesto es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa26":
        resultado = Programa26()
        print(f"Al calcular los lados de un triangulo sabemos que: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa27":
        resultado = Programa27()
        print(f"EL resultado al solicitar ingresar un numero es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa28":
        resultado = Programa28()
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa29":
        Programa29()
    elif Nombre_Programa == "Programa30":
        Programa30()       
    elif Nombre_Programa == "Programa31":
        Programa31()    
    elif Nombre_Programa == "Programa32":
        Programa32()    
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa33":
        Programa33()
    elif Nombre_Programa == "Programa34":
        Programa34()           
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa35":
        Programa35()
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa36":
        Programa36()   
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa37":
        resultado = Programa37()
        print(f"El Total de una compra es de: {resultado} Balboas ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa38":
        resultado = Programa38()
        print(f"El resultado del Programa 38 es: {resultado} ")
        print("-----------------------------------------------------------------")
    elif Nombre_Programa == "Programa39":
        resultado = Programa39()
        print(F"El resultado de calcular el area de un triangulo es de: {resultado} ")
        print("-----------------------------------------------------------------")
        
print("Fin de los Programas \n ")