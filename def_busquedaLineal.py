# Función para realizar la búsqueda lineal

'''
Verifica si existe o no existe un elemento de la lista.
Ventaja que si esta al principio anda sino hace el recorrido completo hasta el final.
'''

def busquedaLineal(lista, numero):
    for elemento in lista:
        if elemento == numero:
            return True
    return False