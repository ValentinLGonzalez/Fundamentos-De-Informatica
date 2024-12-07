"""Desarrollo de un algoritmo combinado de búsqueda y ordenamiento


Desarrolla un programa que realice las siguientes funciones en una lista de números enteros:


1.	Búsqueda Lineal:
- El programa debe recibir como entrada un número entero que se desea buscar en la lista. 
- Primero, debe verificar si el número ya existe en la lista utilizando un algoritmo de búsqueda lineal. 
- Si el número no se encuentra en la lista, debe agregarlo al final de la lista. 

2.	Ordenamiento:
- Una vez realizada la búsqueda (y la posible inserción), el programa debe ordenar la lista utilizando uno de los siguientes algoritmos 
de ordenamiento: 
* Burbuja (Bubble Sort) 
* Selección (Selection Sort) 
* Inserción (Insertion Sort) 

3.	Salida:
- Imprimir la lista antes y después del proceso de ordenamiento, así como el estado del resultado de la búsqueda (si el número fue 
encontrado o agregado). 
- Ejemplo: 
* Lista original: [5, 3, 8, 1, 7] 
* Número a buscar: 4 
* Resultado: Número no encontrado, agregado a la lista. 
* Lista antes del ordenamiento: [5, 3, 8, 1, 7, 4] 
* Lista después del ordenamiento: [1, 3, 4, 5, 7, 8]"""

# Objetivos:
# 1. Realizar una busqueda lineal en la lista
# 2. Si el número no está en la lista, agregarlo al final
# 3. Ordenar la lista con uno de los algoritmos permitidos
# 4. Imprimir la lista antes y despues del ordenamiento, y el resultado de busqueda

# ENTRADAS: LISTA DE NUMEROS ENTEROS, NUMERO ENTERO A BUSCAR EN LA LISTA
# SALIDAS: MENSAJE INDICANDO SI EL NUMERO FUE ENCONTRADO O AGREGADO, LISTA ANTES DEL ORDENAMIENTO, LISTA DESPUES DEL ORDENAMIENTO



# Función para realizar la búsqueda lineal

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
lista = [1, 5, 9] # Lista inicial
print("Lista original: ", lista)

# Leer el numero a buscar 
numero = int(input("Ingrese el numero a buscar: "))

# Realizar busqueda lineal
if busquedaLineal(lista, numero):
    print("Resultado: Numero encontrado")
else:
    print("Resultado: Numero no encontrado, agregado a la lista")
    lista.append(numero)

# Mostrar lista antes del ordenamiento
print("Lista antes del ordenamiento:", lista)

# Ordenar la lista
ordenamientoPorInsercion(lista)

# Mostrar lista después del ordenamiento
print("Lista despues del ordenamiento:", lista)