# -*- coding: utf-8 -*-

class ColaDePrioridad:
    def __init__(self):
        self._monticulo = [] # Usaremos una lista para representar el monticulo

    def _intercambiar(self, i, j):
        self._monticulo[i], self._monticulo[j] = self._monticulo[j], self._monticulo[i]

    def _subir(self, indice): # Mueve el elemento hacia arriba en el monticulo si es menor que su padre
        
        while indice > 0:
            padre_indice = (indice - 1) // 2
            # El criterio de prioridad: (riesgo, orden_llegada)
            # Menor riesgo tiene mayor prioridad. Si son iguales, el que llegó antes.
            if self._monticulo[indice][0].get_riesgo() < self._monticulo[padre_indice][0].get_riesgo():
                self._intercambiar(indice, padre_indice)
                indice = padre_indice
            elif self._monticulo[indice][0].get_riesgo() == self._monticulo[padre_indice][0].get_riesgo():
                # Segundo criterio: orden de llegada (asumiendo que el segundo elemento de la tupla es el id de llegada)
                if self._monticulo[indice][1] < self._monticulo[padre_indice][1]:
                    self._intercambiar(indice, padre_indice)
                    indice = padre_indice
                else:
                    break # No es necesario subir más si el orden de llegada es menor o igual
            else:
                break # Ya está en su posición correcta

    def _bajar(self, indice):
        # Mueve el elemento hacia abajo en el monticulo si es mayor que alguno de sus hijos
        tamano = len(self._monticulo)
        while True:
            hijo_izquierdo_indice = 2 * indice + 1
            hijo_derecho_indice = 2 * indice + 2
            menor = indice # Asumimos que el actual es el menor

            # Compara con el hijo izquierdo
            if hijo_izquierdo_indice < tamano:
                # Criterio de prioridad: (riesgo, orden_llegada)
                if self._monticulo[hijo_izquierdo_indice][0].get_riesgo() < self._monticulo[menor][0].get_riesgo():
                    menor = hijo_izquierdo_indice
                elif self._monticulo[hijo_izquierdo_indice][0].get_riesgo() == self._monticulo[menor][0].get_riesgo():
                    if self._monticulo[hijo_izquierdo_indice][1] < self._monticulo[menor][1]:
                        menor = hijo_izquierdo_indice

            # Compara con el hijo derecho
            if hijo_derecho_indice < tamano:
                # Criterio de prioridad: (riesgo, orden_llegada)
                if self._monticulo[hijo_derecho_indice][0].get_riesgo() < self._monticulo[menor][0].get_riesgo():
                    menor = hijo_derecho_indice
                elif self._monticulo[hijo_derecho_indice][0].get_riesgo() == self._monticulo[menor][0].get_riesgo():
                    if self._monticulo[hijo_derecho_indice][1] < self._monticulo[menor][1]:
                        menor = hijo_derecho_indice

            if menor != indice:
                self._intercambiar(indice, menor)
                indice = menor
            else:
                break # El elemento ya está en su posición correcta

    def insertar(self, paciente, id_llegada):
        # Almacenamos tuplas (paciente, id_llegada) para el desempate
        self._monticulo.append((paciente, id_llegada))
        self._subir(len(self._monticulo) - 1)

    def extraer_minimo(self):
        if not self._monticulo:
            return None
        if len(self._monticulo) == 1:
            return self._monticulo.pop()[0] # Devuelve solo el objeto paciente
        
        # El paciente más crítico es la raíz (índice 0)
        minimo = self._monticulo[0]
        # Mueve el último elemento a la raíz
        self._monticulo[0] = self._monticulo.pop()
        # Restaura la propiedad del monticulo bajando el nuevo elemento raíz
        self._bajar(0)
        return minimo[0] # Devuelve solo el objeto paciente

    def esta_vacia(self):
        return len(self._monticulo) == 0

    def tamano(self):
        return len(self._monticulo)

    def __len__(self):
        return self.tamano()

    def __str__(self):
        # Para imprimir el contenido de la cola de prioridad
        # Esto es solo para depuración/visualización, no garantiza orden
        cad = "Contenido de la Cola de Prioridad (orden interno del monticulo):\n"
        for paciente_data in self._monticulo:
            cad += f"\t{paciente_data[0]} (ID Llegada: {paciente_data[1]})\n"
        return cad.strip()