"""generar una lista única sin listas en su interior,
 a partir de una lista con varias listas dentro de sus elementos."""

def lista_principal(lista):
    if type (lista) != list:
        return None
    resultado = []
    cola = [lista]

    while cola :
        elemento= cola.pop(0)
        if type (elemento) == list:
            cola.extend(elemento)
        else:
            resultado.append(elemento)
    return resultado

print(lista_principal([1,2,3,[1,2,3,[1,2,3]]]))