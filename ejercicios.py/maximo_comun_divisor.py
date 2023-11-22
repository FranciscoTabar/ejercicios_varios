"""armar un afincion que permita encontar el maximo comun divisor entre dos numeros"""

"""def mcd(a , b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)
a = int(input("ingrese el primer numero:\n"))
b = int (input(" el segundo numero:\n"))
print( "el resultado es:", mcd(a, b))"""


def mcd_alt(x,y):
    if x > y:
        menor = y
    else:
        menor = x
    for i in range( 1, menor +1):
        if x % i == 0 and y % i == 0:
            mcd_alt= i
    return mcd_alt

x = int(input("ingrese el primer valor:\n"))
y = int(input("ingrese el segundo valor:\n"))
resultado= mcd_alt(x,y)
print("el resultado es :", resultado)