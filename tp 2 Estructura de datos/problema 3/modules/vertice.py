# modules/vertice.py

class Vertice:
    """
    Representa un vértice (nodo) en un grafo.
    """
    def __init__(self, clave, carga_util=None):
        """
        Inicializa un nuevo vértice.
        :clave: Nombre único del vértice.
        :carga_util: Información adicional asociada al vértice.
        """
        self.clave = clave
        self.carga_util = carga_util
        self.vecinos = {} # Diccionario: {objeto_Vertice_vecino: peso_arista}

    def agregarVecino(self, vecino_obj, peso=0):
        """
        Agrega un vecino a este vértice con un peso específico de arista.
        :vecino_obj: Objeto Vertice vecino.
        :peso: Peso de la arista que conecta a este vértice con el vecino.
        """
        self.vecinos[vecino_obj] = peso

    def obtenerConexiones(self):
        """
        Devuelve todos los objetos Vertice vecinos conectados a este vértice.
        :return: Lista de objetos Vertice vecinos.
        """
        return self.vecinos.keys()

    def obtenerPeso(self, vecino_obj):
        """
        Devuelve el peso de la arista que conecta a este vértice con un vecino específico.
        :vecino_obj: Objeto Vertice vecino.
        :return: Peso de la arista.
        """
        return self.vecinos.get(vecino_obj, None)

    def obtenerClave(self):
        """
        Devuelve la clave (nombre) del vértice.
        :return: La clave del vértice.
        """
        return self.clave

    def __str__(self):
        """
        Representación en cadena del vértice.
        """
        return str(self.clave) + ' conectado a: ' + str([x.clave for x in self.vecinos])

    def __repr__(self):
        """
        Representación oficial para desarrolladores.
        """
        return f"Vertice({self.clave})"

    def __hash__(self):
        """
        Permite que los objetos Vertice sean usados como claves de diccionario, basado en su clave.
        """
        return hash(self.clave)

    def __eq__(self, other):
        """
        Define la igualdad entre dos objetos Vertice basada en su clave.
        """
        return isinstance(other, Vertice) and self.clave == other.clave
