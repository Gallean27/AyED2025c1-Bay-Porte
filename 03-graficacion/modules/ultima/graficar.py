import matplotlib.pyplot as plt
import time
from tiempos import medir_tiempos 
from ordenamientos import ordenamiento_burbuja , ordenamientoRapido, ordenamiento_radix




def graficar_tiempos(metodos_ordenamiento):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    plt.figure(figsize=(10, 6))
    for metodo_ord in metodos_ordenamiento:
        nombre_metodo = metodo_ord.__name__
        tiempos = medir_tiempos(metodo_ord, tamanos) 
        plt.plot(tamanos, tiempos, marker='o', label=nombre_metodo)
    plt.xlabel('Tamaño de la lista (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución de algoritmos de ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    metodos_ordenamiento = [ordenamiento_burbuja , ordenamientoRapido, ordenamiento_radix]
    graficar_tiempos(metodos_ordenamiento)
   
"""
from matplotlib import pyplot as plt
from tiempos import medir_tiempos

from ordenamiento_burbuja1 import ordenamiento_burbuja
from ordenamiento_rapido import ordenamientoRapido
from ordenamiento_radix1 import ordenamiento_radix


def graficar_tiempos(lista_metodos_ord):
    
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()
    
    
    
if __name__ == '__main__':
    graficar_tiempos([ordenamiento_burbuja])
   graficar_tiempos([ordenamiento_radix])
   graficar_tiempos([ordenamientoRapido])
    """