value = 1
A = int(input("escribe el 1numero "))
B = int(input("escribe el 2numero "))
C = int(input("escribe el 3numero "))

while value <= 1:
    print(value)
    if A > B and A > C:
        print('el numero mayor es a = ', A)
    if B > A and B > C:
        print('el numero mayor es b = ', B)
    if C > A and C > B:
        print('el numero mayor es c = ', C)
        break
    value += 1
   
    
    