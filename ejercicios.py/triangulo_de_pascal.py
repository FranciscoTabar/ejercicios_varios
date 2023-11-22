"""contruye un triangulo de pascal"""
filas= int(input("ingrese el numero de filas:\n"))

from math import factorial
for n in range(filas):
    for j in range(filas - n+1):
        print(end=" ")
    for r in range(n+1):
        numero= factorial(n)/(factorial(n-r)*factorial(r))
        print(int(numero),end=" ")
    print()

