""" crea una funcion que tome un string y 
devuelva al primer caracter de ese string en mayuscula y el resto en muniscula"""

def primer_mayus(string):#defino la funcion 
    lista = []#armo una lista vacia donde colocare los caracteres 
    for i in range (len(string)):#establezco el rango de trabajo len=largo de la frase
        if i == 0:#condicion si i es el primer caracter entonces...
            lista.append(string[i].upper())#agregar a la lista vacia y upper=mayuscula
        else:#si i no es el primer caracter entonces...
            lista.append(string[i].lower()) #dejar loa caracteres en minuscula uso lower
    return"".join(lista)#regreso la union de los caracteres en la lista que arme

x = input("ingrese un apalabra \n")
resultado= primer_mayus(x)
print (resultado)