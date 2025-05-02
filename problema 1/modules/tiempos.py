from random import randint
import time
import matplotlib.pyplot as plt

from ordenamientos import ordenamiento_burbuja , ordenamientoRapido, ordenamiento_radix


def medir_tiempos(metodo_ord, tamanos):
    tiempos = []
    for n in tamanos:
        datos = [randint(1, 10000) for _ in range(n)]
        inicio = time.perf_counter()
        metodo_ord(datos[:]) # Pasa una copia para no modificar la original
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        print(f"Tiempo para n={n}: {fin - inicio:.6f} segundos")
    return tiempos

if __name__ == '__main__':
    tamanos = [1, 10, 100, 200, 500, 700, 1000]

    tiempos_burbuja = medir_tiempos(ordenamiento_burbuja, tamanos)
    tiempos_radix = medir_tiempos(ordenamiento_radix, tamanos)
    tiempos_rapido = medir_tiempos(ordenamientoRapido, tamanos)

    
    print("\nTiempos de ordenamiento burbuja:", tiempos_burbuja)
    print("Tiempos de ordenamiento radix:", tiempos_radix)
    print("Tiempos de ordenamiento rapido:", tiempos_rapido)