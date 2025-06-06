# modules/grafo.py

import heapq
from .vertice import Vertice # Importa la clase Vertice desde el mismo paquete

class Grafo:
    """
    Representa un grafo compuesto por vértices y aristas.
    """
    def __init__(self):
        """
        Crea un grafo nuevo y vacío.
        """
        self.listaVertices = {} # Diccionario: {clave_vertice: objeto_Vertice}
        self.numVertices = 0

    def agregarVertice(self, clave_vert, carga_util=None):
        """
        Agrega una instancia de Vertice al grafo.
        :param clave_vert: Clave del nuevo vértice.
        :param carga_util: Carga útil del nuevo vértice.
        :return: El objeto Vertice creado.
        """
        self.numVertices += 1
        nuevo_vertice = Vertice(clave_vert, carga_util)
        self.listaVertices[clave_vert] = nuevo_vertice
        return nuevo_vertice

    def obtenerVertice(self, clave_vert):
        """
        Encuentra el vértice en el grafo con nombre clave_vert.
        :param clave_vert: Clave del vértice a buscar.
        :return: Objeto Vertice si existe, None en caso contrario.
        """
        return self.listaVertices.get(clave_vert, None)

    def agregarArista(self, deVertice_clave, aVertice_clave, ponderacion=0):
        """
        Agrega al grafo una nueva arista (bidireccional para este problema)
        que conecta dos vértices. Si los vértices no existen, los crea.
        :param deVertice_clave: Clave del vértice de origen.
        :param aVertice_clave: Clave del vértice de destino.
        :param ponderacion: Ponderación (peso) de la arista.
        """
        if deVertice_clave not in self.listaVertices:
            self.agregarVertice(deVertice_clave)
        if aVertice_clave not in self.listaVertices:
            self.agregarVertice(aVertice_clave)
        
        # Agregamos la arista en ambas direcciones ya que las rutas son bidireccionales
        self.listaVertices[deVertice_clave].agregarVecino(self.listaVertices[aVertice_clave], ponderacion)
        self.listaVertices[aVertice_clave].agregarVecino(self.listaVertices[deVertice_clave], ponderacion)

    def obtenerVertices(self):
        """
        Devuelve la lista de todas las claves de los vértices en el grafo.
        :return: Lista de claves de vértices.
        """
        return self.listaVertices.keys()

    def __contains__(self, clave_vert):
        """
        Devuelve True si el vértice dado está en el grafo, False de lo contrario.
        Permite la sintaxis 'vertice in grafo'.
        """
        return clave_vert in self.listaVertices

    def __iter__(self):
        """
        Permite iterar sobre los objetos Vertice en el grafo.
        """
        return iter(self.listaVertices.values())
