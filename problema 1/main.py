from matplotlib import pyplot as plt
from random import randint
import time
from modules.ordenamientos import ordenamiento_burbuja, ordenamiento_radix, ordenamiento_rapido

tamanos = range(1,1000,10)
tiempos_ordenamiento_burbuja = []
tiempos_ordenamiento_radix = []
tiempos_ordenamiento_rapido = []

# figsize es el tamaño de la figura en pulgadas (width, height)
plt.figure(figsize=(10, 6))



for n in tamanos:

    datos= [randint(1, 10000) for _ in range(n)]
    # datos = []
    # for _ in range(n):
    #     datos.append(randint(1, 10000))    


    inicio = time.perf_counter()
    ordenamiento_burbuja(datos.copy())
    fin = time.perf_counter()

    tiempos_ordenamiento_burbuja.append(fin - inicio) 

    
    inicio = time.perf_counter()
    ordenamiento_radix(datos.copy())
    fin = time.perf_counter()

    tiempos_ordenamiento_radix.append(fin - inicio) 


    inicio = time.perf_counter()
    ordenamiento_rapido(datos.copy())
    fin = time.perf_counter()

    tiempos_ordenamiento_rapido.append(fin - inicio) 

# plt.plot(tamanos, tiempos_ordenamiento_por_seleccion, marker='o', label="ordenamiento_por_seleccion")
plt.plot(tamanos, tiempos_ordenamiento_burbuja, label="ordenamiento_burbuja")
plt.plot(tamanos, tiempos_ordenamiento_rapido, label="ordenamiento_rapido")
plt.plot(tamanos, tiempos_ordenamiento_radix, label="ordenamiento_radix")



plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
plt.grid() # cuadriculado
plt.savefig('problema 1/docs/graficacion.png')
plt.show()


