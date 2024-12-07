#Algoritmos de Inrserción:
'''
Empieza subdividiendo una lista de forma ordenada y otra de desordenada, siempre
empieza con 1 valor en la ordenada y con ese valor se evalua.
Se va acomodando en orden ascendente.
'''
def ordenamientoPorInsercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista [j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave