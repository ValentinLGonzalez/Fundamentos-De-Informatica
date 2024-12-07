#Metodos de Ordenamiento:

#Burbujeo:
'''El ordenamiento lo hace de menor a mayor pero podemos cambiarlo en el codigo y se resuelven de menor a mayor.
Se hace comparacion de a pares.
Necesitas una variable temporal para intercambiar.
y se hace posicion vs posicion +1

El numero mas grande queda hacia el final periodicamente.


'''

#Codigo de Ordenamiento Burbuja:

def burbuja(lista):
    #Se inicia como True para que entre al bucle al menos una vez
    huboIntercambio = True
    while huboIntercambio:
        huboIntercambio = False
    for i in range(0, (len(lista) - 1)):
        if (lista[i] > lista[i+1]):
            #Se produce el intercambio de datos
            temporal = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = temporal
            huboIntercambio = True
            
numeros = [7, 1, 5, 3, 2]
burbuja (numeros)
print(numeros)