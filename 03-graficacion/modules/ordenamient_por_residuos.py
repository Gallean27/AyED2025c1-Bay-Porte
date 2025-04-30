import random

def ordenamiento_por_residuos(lista):
    """
    Implementación del algoritmo de ordenamiento por residuos (Radix Sort)

    Args:
        lista: La lista de números enteros a ordenar.

    Returns:
        La lista ordenada (la misma lista que se pasó como argumento).
    """
    if not lista:
        return lista

    max_valor = max(lista)
    exp = 1
    n = len(lista)

    while max_valor // exp > 0:
        cubetas = [[] for _ in range(10)]
        for num in lista:
            indice_cubeta = (num // exp) % 10
            cubetas[indice_cubeta].append(num)

        i = 0
        for cubeta in cubetas:
            for num in cubeta:
                lista[i] = num
                i += 1
        exp *= 10
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

# Generar una lista de 580 números aleatorios de cinco dígitos
num_elementos = 580
lista_aleatoria = [random.randint(10000, 99999) for _ in range(num_elementos)]

# Crear una copia de la lista para ordenarla
lista_a_ordenar = lista_aleatoria[:]

# Ordenar la lista utilizando el ordenamiento por residuos (sin función auxiliar)
lista_ordenada_radix = ordenamiento_por_residuos(lista_a_ordenar)

# Verificar si la lista ordenada por Radix Sort está realmente ordenada
#if esta_ordenada(lista_ordenada_radix):
#    print(f"El ordenamiento por residuos funcionó correctamente con una lista de {num_elementos} números aleatorios de cinco dígitos.")
#    print("Primeros 10 elementos de la lista original:", lista_aleatoria[:10])
#    print("Primeros 10 elementos de la lista ordenada:", lista_ordenada_radix[:10])
#else:
#    print(f"¡El ordenamiento por residuos (sin auxiliar) NO funcionó correctamente con una lista de {num_elementos} números aleatorios de cinco dígitos!")
#    print("Primeros 10 elementos de la lista ordenada (por Radix Sort sin auxiliar):", lista_ordenada_radix[:10])
#    # Si falla, podríamos imprimir más elementos para depurar si es necesario