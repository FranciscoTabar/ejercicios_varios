"""crearemos una función que a partir de una lista, 
nos indicará cuántas veces se repite cada elemento de esa lista, almacenando los resultados en tuplas de dos valores: el primer valor será un elemento de la lista,
y el segundo valor la cantidad de veces que se repite."""

def lista_de_tuplas(lista):
    if type(lista) != list:
        return None
    else:    
        contador={}
        for elem in lista:
            if elem in contador:
                contador[elem]+=1
            else:
                contador[elem]=1
        respuesta = list(contador.items())
        return respuesta

print(lista_de_tuplas(["data","data","data","facil","facil"]))


