import random

def ordenamiento_quicksort(lista, bajo, alto):
    """
    Implementación del algoritmo de ordenamiento Quicksort (recursivo) sin función auxiliar.

    Args:
        lista: La lista a ordenar (se modifica in-place).
        bajo: El índice inferior de la sublista a ordenar.
        alto: El índice superior de la sublista a ordenar.

    Returns:
        La lista ordenada (la misma lista que se pasó como argumento).
    """
    if bajo < alto:
        pivote = lista[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if lista[j] <= pivote:
                i = i + 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        indice_particion = i + 1

        ordenamiento_quicksort(lista, bajo, indice_particion - 1)
        ordenamiento_quicksort(lista, indice_particion + 1, alto)
    return lista

def esta_ordenada(lista):
    """
    Verifica si una lista está ordenada de forma ascendente.

    Args:
        lista: La lista a verificar.

    Returns:
        True si la lista está ordenada, False en caso contrario.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Generar una lista de 620 números aleatorios de cinco dígitos
num_elementos = 620
lista_aleatoria = [random.randint(10000, 99999) for _ in range(num_elementos)]

# Crear una copia de la lista para ordenarla
lista_a_ordenar = lista_aleatoria[:]

# Ordenar la lista utilizando el ordenamiento Quicksort (sin función auxiliar)
lista_ordenada_quicksort = ordenamiento_quicksort(lista_a_ordenar, 0, len(lista_a_ordenar) - 1)

# Verificar si la lista ordenada por Quicksort está realmente ordenada
#if esta_ordenada(lista_ordenada_quicksort):
#    print(f"El ordenamiento Quicksort funcionó correctamente con una lista de {num_elementos} números aleatorios de cinco dígitos.")
#    print("Primeros 10 elementos de la lista original:", lista_aleatoria[:10])
#    print("Primeros 10 elementos de la lista ordenada:", lista_ordenada_quicksort[:10])
#else:
#    print(f"¡El ordenamiento Quicksort (sin auxiliar) NO funcionó correctamente con una lista de {num_elementos} números aleatorios de cinco dígitos!")
#    print("Primeros 10 elementos de la lista ordenada (por Quicksort sin auxiliar):", lista_ordenada_quicksort[:10])
#    # Si falla, podríamos imprimir más elementos para depurar si es necesario