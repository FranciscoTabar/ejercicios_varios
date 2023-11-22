"""Armar una funcion que permita 
encontrar un secuencua de numeros [10,20,30] en una lista"""

def encontrar_num(lista):#defino la funcion
        i = 0 
        while i < (len(lista)-2):# el largo de la lista tiene que ser menor a dos por que la secuencia tiene tres lementos
            if lista[i]== 10 and lista[i+1]== 20 and lista[i+2]==30:#esta es la secuencia que quiero encontrar
                return True
            else:
                i += 1
secuencia= [10,20,30]
resultado= encontrar_num(secuencia)
print(resultado)
secuencia_dos = [12,40,10,20,30,58]
resultado2 = encontrar_num(secuencia_dos)
print(resultado2)


