def sumar_numeros_pares(c):
    suma = 0
    for x in range(1, c + 1):
        if x % 2 == 0:
            suma += x
    return suma

resultado = sumar_numeros_pares(20)
print("La Suma de los numeros pares entre 1 y 20 es:", resultado)