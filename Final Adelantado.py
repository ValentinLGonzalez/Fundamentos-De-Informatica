def busquedaLineal(lista, numero):
    for elemento in lista:
        if elemento == numero:
            return True
    return False

# Funcion para ordenar la lista (Burbuja, seleccion o inserción)
def ordenamientoPorInsercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista [j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

# Programa principal
lista = [2, 4, 6, 8, 10] # Lista inicial
print("Lista original: ", lista)

# Leer el numero a buscar 
numero = int(input("Ingrese el numero a buscar: "))

# Realizar búsqueda lineal
if busquedaLineal(lista, numero):
    if numero % 2 == 0: # Verificar si el numero es par
        lista.append(numero)
        print("Resultado: Numero encontrado y es par, agregado a la lista")
    else:
        print("Resultado: Numero encontrado, pero no es par")
else:
    print("Resultado: Numero no encontrado")

# Mostrar lista antes del ordenamiento
print("Lista antes del ordenamiento:", lista)

# Ordenar la lista
ordenamientoPorInsercion(lista)

# Mostrar lista después del ordenamiento
print("Lista después del ordenamiento:", lista)