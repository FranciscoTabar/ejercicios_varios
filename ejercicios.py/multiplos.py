"""cómo generar una lista con los números múltiplos de cierto número,
dando el intervalo y asumiendo que el número base es el inicio del intervalo."""

def listaMultiplos (inicio,final):
    multiplos=[]
    for x in range(inicio,final+1,inicio):
        multiplos.append(x)
    return multiplos

x = int(input("ingrese el inicio del intervalo\n"))
y= int(input("ingrese el fin del intervalo:\n"))
resultado= listaMultiplos(x,y)
print("la lista de multiplos para el primer valor es:\n", resultado)
    
