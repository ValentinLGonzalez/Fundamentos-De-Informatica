#Algoritmo de Ordenamiento - Seleccion:
'''
Parte en 2(sublista) la lista en una parte ordenada y otra parte desordenada, mas ordenada mas rapido

Buca el elemento mas pequeño con respecto a la lista (elemento m de menor)
y realiza el intercambio con una variable temporal.

'''
def seleccion(lista):
    for i in range(0, len(lista)-1):
        #El primer elemento sin ordenar es el más pequeño
        menorIndice = i
        #El siguiente bucle trabaja sobre la lista «no ordenada»
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[menorIndice]):
                menorIndice = j
        #Intercambia los valores
        temporal = lista[menorIndice]
        lista[menorIndice] = lista[i]
        lista[i] = temporal
        
numeros = [7, 1, 5, 3, 2]
seleccion (numeros)
print(numeros)