from matplotlib import pyplot as plt
from random import randint
import time

from ListaDobleEnlazada1 import ListaDobleEnlazada
# creamos cuatro listas vacias
tamanoslde = [] #tamaños de la lista doble enlazada que se van a probar.
tiempos_len = [] #Almacenará los tiempos de ejecución de la función len() para cada tamaño de lista.
tiempos_copiar = [] #Almacenará los tiempos de ejecución del método copiar() para cada tamaño de lista.
tiempos_invertir = [] #Almacenará los tiempos de ejecución del método invertir() para cada tamaño de lista.

for N in range(10, 8000, 100): 
    lista = ListaDobleEnlazada()
    
    
    for i in range(N): #itera sobre diferentes valores de N (tamaños de la lista)
        lista.agregar_al_final(i)  

   
    inicio = time.perf_counter()
    tamaño = len(lista)  
    fin = time.perf_counter()
    tiempos_len.append(fin - inicio)

   
    inicio = time.perf_counter()
    copia = lista.copiar()
    fin = time.perf_counter()
    tiempos_copiar.append(fin - inicio)

   
    inicio = time.perf_counter()
    lista.invertir()
    fin = time.perf_counter()
    tiempos_invertir.append(fin - inicio)

    tamanoslde.append(N)



plt.plot(tamanoslde, tiempos_len, label='len()', marker='o')
plt.plot(tamanoslde, tiempos_copiar, label='copiar()', marker='o')
plt.plot(tamanoslde, tiempos_invertir, label='invertir()', marker='o')
plt.xlabel('Cantidad de elementos (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Cantidad de elementos vs Tiempo de ejecución')
plt.legend()
plt.grid(True)

plt.show()
