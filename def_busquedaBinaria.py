#Busqueda binaria:
'''
La lista se necesita encuentra ordenada de menor a mayor.
Busco en la primera mitad y devuelvo el indice donde esta.
si el numero que estoy buscando es mas grande busco a la derecha sino busco
a la izquierda.
me enfoco al numero que esta en el medio sino vuelvo a preguntar.

Va descartando prociones y de a mitades, pero debe estar ordenada la lista.

'''

def busquedaBinaria(lista, valorBuscado):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valorBuscado:
            return medio
        if lista[medio] > valorBuscado:
            fin = medio - 1
        else:  # lista[medio] < valorBuscado
            inicio = medio + 1
    return None

# Programa principal
numeros = [1, 2, 3, 5, 7]
indice = busquedaBinaria(numeros, 5)

if indice is not None:
    print("El número buscado está en el índice:", indice)
    print("Valor encontrado:", numeros[indice])
else:
    print("No se encontró el valor.")
