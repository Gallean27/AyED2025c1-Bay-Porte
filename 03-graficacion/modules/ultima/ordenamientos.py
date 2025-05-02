
from random import randint
# -*- coding: utf-8 -*-
def ordenamiento_burbuja(unaLista):
    n = len(unaLista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if unaLista[j] > unaLista[j + 1]:
                temp = unaLista[j]
                unaLista[j] = unaLista[j + 1]
                unaLista[j + 1] = temp
    return unaLista # Es importante retornar la lista ordenada
#def ordenamientoBurbuja(unaLista): #definicion de funcion ordenamiento Burbuja que toma un argumento: unaLista
 #   for extremo in range(len(unaLista)-1,0,-1): # bucle exterior Calcula el índice del último elemento de la lista y le resta 1. Esto se debe a que en cada pasada del bucle exterior, el elemento más grande "burbujea" hacia su posición correcta al final de la porción no ordenada de la lista. Por lo tanto, no necesitamos comparar los elementos que ya están en su lugar.
  #      for i in range(extremo): #Este es el bucle interior
   #         if unaLista[i]>unaLista[i+1]: #Esta línea realiza la comparación clave del algoritmo Burbuja
    #            temp = unaLista[i] #Si la condición del if es verdadera, esta línea guarda el valor del elemento actual (unaLista[i]) en una variable temporal llamada temp. Esto es necesario para poder intercambiar los valores sin perder uno de ellos.
     #           unaLista[i] = unaLista[i+1]#Esta línea reemplaza el valor del elemento actual (unaLista[i]) con el valor del elemento siguiente (unaLista[i+1]).
      #          unaLista[i+1] = temp# Esta línea reemplaza el valor del elemento siguiente (unaLista[i+1]) con el valor que se guardó previamente en la variable temporal temp (que era el valor original del elemento actual). Estas tres últimas líneas (temp = ..., unaLista[i] = ..., unaLista[i+1] = ...) realizan el intercambio de los dos elementos adyacentes.

def obtener_digito(numero, posicion_digito, base = 10):
    """
    Obtiene el dígito en la posición especificada (de derecha a izquierda) de un número.
    Devuelve cero si la posición es mayor que el número de dígitos del número.
    """
    return (numero // (base ** posicion_digito)) % base
def ordenamiento_radix(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento Radix.
    """
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(lista)
    exp = 1  # Exponente para la posición del dígito
    lista_aux = [[] for _ in range(10)]  
    pos = 0  # Inicializa la posición del dígito
    while max_num // exp > 0:
        # Coloca los números en la lista auxiliar según el dígito actual
        for num in lista:
            digit = obtener_digito(num, pos)  # Obtiene el dígito en la posición actual
            lista_aux[digit].append(num)

        # Reconstruye la lista original a partir de la lista auxiliar
        sig_pos = 0  # Inicializa la posición en la lista original
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  # Añade el número a la lista original 
                sig_pos += 1    


        # Limpia la lista auxiliar para la siguiente posición de dígito
        lista_aux = [[] for _ in range(10)]

        # Aumenta el exponente para pasar al siguiente dígito
        exp *= 10
        pos += 1
 
 
    return lista

def ordenamientoRapido(unaLista):  #definimos la funcion
   ordenamientoRapidoAuxiliar(unaLista, 0, len(unaLista)-1) #Llama a una función auxiliar llamada ordenamientoRapidoAuxiliar. Le pasa la lista (unaLista), el índice del primer elemento (0), y el índice del último elemento (len(unaLista)-1). Esta función auxiliar es la que realmente implementa la lógica recursiva del Quicksort.
def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo): #Define la función auxiliar ordenamientoRapidoAuxiliar que toma tres argumentos
   if primero<ultimo: #Esta es la condición base para la recursión. Si el índice del primer elemento (primero) es menor que el índice del último elemento (ultimo), significa que la sublista tiene al menos dos elementos y necesita ser ordenada. Si primero es igual o mayor que ultimo, la sublista tiene cero o un elemento, que ya está ordenado.

       puntoDivision = particion(unaLista,primero,ultimo) #Llama a la función particion para dividir la sublista actual en dos partes: los elementos menores que un "pivote" y los elementos mayores que el pivote. La función particion devuelve el índice del "punto de división" (la posición final del pivote después de la partición).

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)#Realiza una llamada recursiva a ordenamientoRapidoAuxiliar para ordenar la sublista que está a la izquierda del puntoDivision (desde el primer elemento hasta el elemento justo antes del pivote).
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo) #Realiza una llamada recursiva a ordenamientoRapidoAuxiliar para ordenar la sublista que está a la izquierda del puntoDivision (desde el primer elemento hasta el elemento justo antes del pivote).
def particion(unaLista,primero,ultimo): #Define la función particion que toma la lista y los índices del primer y último elemento de la sublista a particionar.
   valorPivote = unaLista[primero] # Selecciona el primer elemento de la sublista como el "pivote". Los elementos de la sublista se compararán con este valor pivote.

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False #Inicializa una variable booleana hecho a False. Esta variable se utilizará para controlar el bucle while principal de la partición.
   while not hecho: #Inicia un bucle while que continuará hasta que la variable hecho se establezca en True (lo que ocurre cuando las marcas izquierda y derecha se cruzan).

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:#Este bucle while interno mueve la marcaIzq hacia la derecha mientras no se cruce con marcaDer y el elemento en marcaIzq sea menor o igual que el valorPivote. El objetivo es encontrar un elemento en el lado izquierdo que sea mayor que el pivote.
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq: #Este bucle while interno mueve la marcaDer hacia la izquierda mientras no se cruce con marcaIzq y el elemento en marcaDer sea mayor o igual que el valorPivote. El objetivo es encontrar un elemento en el lado derecho que sea menor que el pivote.
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq: #Si la marcaDer se ha movido a la izquierda de la marcaIzq, significa que se han encontrado todos los elementos mayores que el pivote a la izquierda y todos los elementos menores que el pivote a la derecha, por lo que la partición de esta sublista está completa.
           hecho = True # para salir del while
       else: #Si marcaDer aún no ha cruzado marcaIzq, significa que se han encontrado elementos en los lados incorrectos (un elemento mayor que el pivote a la izquierda y un elemento menor que el pivote a la derecha), y deben ser intercambiados.
           temp = unaLista[marcaIzq] #Guarda el valor del elemento en marcaIzq en una variable temporal temp.
           unaLista[marcaIzq] = unaLista[marcaDer] # naLista[marcaIzq] = unaLista[marcaDer]: Reemplaza el elemento en marcaIzq con el elemento en marcaDer
           unaLista[marcaDer] = temp # Reemplaza el elemento en marcaDer con el valor que se guardó en temp (el valor original del elemento en marcaIzq). Estas tres líneas realizan el intercambio de los elementos.

   temp = unaLista[primero] #Después de que el bucle while principal termina (cuando las marcas se cruzan), esta línea guarda el valor del pivote (que estaba al principio de la sublista) en la variable temp.
   unaLista[primero] = unaLista[marcaDer] #Coloca el elemento en marcaDer (que ahora es el elemento más grande de la partición izquierda o un elemento menor que el pivote) en la posición del pivote (al principio de la sublista).
   unaLista[marcaDer] = temp # Coloca el valor original del pivote en la posición de marcaDer. Ahora el pivote está en su posición final correcta dentro de la sublista particionada, con todos los elementos menores a su izquierda y todos los elementos mayores a su derecha.

   return marcaDer #Devuelve el índice de la posición final del pivote (marcaDer), que es el "punto de división".


"""
if __name__ == '__main__':
    # ordena numeros
    M, N = 500, 8000
    datos = [randint(-M, M) for i in range(N)]
    
    
    datos_ordenados = sorted(datos)
    
    datos = ordenamiento_burbuja(datos)
    
    assert datos == datos_ordenados


#unaLista = [54,26,93,17,77,31,44,55,20]

ordenamiento_burbuja(datos) #Esta línea llama a la función ordenamientoBurbuja y le pasa la lista unaLista como argumento. Después de que la función se ejecute, la lista unaLista habrá sido modificada para estar ordenada.

#print(unaLista) # Esta línea imprime el contenido de la lista unaLista después de que la función ordenamientoBurbuja la haya ordenado. La salida será la lista original, pero ahora en orden ascendente.
print(datos_ordenados)

"""