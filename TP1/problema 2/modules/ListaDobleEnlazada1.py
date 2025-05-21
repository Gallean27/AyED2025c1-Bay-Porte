class Nodo: 
   
    def __init__(self, dato):
        self.dato = dato #  item: El dato almacenado en el nodo.
        self.siguiente = None # siguiente: Referencia al siguiente nodo en la lista,puede ser None
        self.anterior = None # anterior: Referencia al nodo anterior en la lista,puede ser None

class ListaDobleEnlazada: # Implementacion de una lista doble enlazada
    def __init__(self):
        self.cabeza = None # primero: Referencia al primer nodo de la lista None si la lista esta vacia
        self.cola = None #ultimo: Referencia al último nodo de la lista None si la lista esta vacia
        self.tamanio = 0 #tamano: El número de elementos en la lista

    def esta_vacia(self): # Verifica si la lista esta vacia
            return self.tamanio == 0 #bool: True si la lista no contiene elementos, False en caso contrario.

    def __len__(self): # Devuelve el numero de elementos de la lista 
     
        return self.tamanio

    def agregar_al_inicio(self, dato):
       
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
       
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion=None): # agregamos un elemento en una posicion especifica de la lista, si la posicion es None agrega al final
       
            #item: El dato a insertar. posicion (int, optional): La posición donde insertar el elemento (comenzando desde 0). Defaults to None.       
            #IndexError: Si la posición es inválida.
        
        if posicion is None:
            self.agregar_al_final(dato)
            return

        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posicion invalida")

        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            nuevo_nodo.anterior = nodo_actual.anterior
            nuevo_nodo.siguiente = nodo_actual
            nodo_actual.anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None): #Remueve y retorna el elemento de una posición específica de la lista.Si la posición es None, se extrae el último elemento.
                                      #La posición del elemento a extraer (comenzando desde 0). IndexError: Si la lista está vacía o la posición es inválida.      
       
        if self.esta_vacia():
            raise IndexError("La lista está vacía")

        if posicion is None:
            posicion = self.tamanio - 1
        elif posicion < 0:
            posicion= self.tamanio + posicion 

        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            item = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            item = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            item = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior

        self.tamanio -= 1
        return item

    def copiar(self): #Crea y retorna una copia superficial de la lista doble enlazada.
      
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return nueva_lista

    def invertir(self): # Invierte el orden de los elementos en la lista doble enlazada
       
        if self.esta_vacia():
            return

        nodo_actual = self.cabeza
        temp = None
        self.cola = nodo_actual

        while nodo_actual is not None:
            temp = nodo_actual.anterior
            nodo_actual.anterior = nodo_actual.siguiente
            nodo_actual.siguiente = temp
            nodo_actual = nodo_actual.anterior

        if temp is not None:
            self.cabeza = temp.anterior

    def concatenar(self, otra_lista): #Concatena otra lista doble enlazada al final de la lista actual
        
        if not isinstance(otra_lista, ListaDobleEnlazada):
            raise TypeError("El argumento debe ser una ListaDobleEnlazada")

        nodo_actual = otra_lista.cabeza
        while nodo_actual is not None:
            self.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def __add__(self, otra_lista): #Implementa el operador de suma (+) para concatenar dos listas dobles enlazadas
       
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente




