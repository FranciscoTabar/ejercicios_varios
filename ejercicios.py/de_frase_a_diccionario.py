""" armar un programa que reciba un afrase y devuelva un diccionario 
con las letras que se repiten en la frase"""

frase = "la palabra que mas se. repite en esta frase seguro es la, O QUIZAS palabra palabra "
contador = {}#diccionario vacio
palabras= frase.replace(",","").replace(".","").lower().split()#remmplazo las colas,reemplazo los puntos, todo en minuscula, divido la frase en elemtos de una lista
for elem in palabras:
    if elem in contador:
        contador[elem]+=1
    else:
        contador[elem]=1
print(contador)