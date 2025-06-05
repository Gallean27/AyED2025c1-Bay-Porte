import datetime

import datetime # Necesario si las claves o valores son de tipo datetime

class NodoAVL:
    """
    Representa un nodo en un árbol AVL genérico.
    Almacena una clave (para ordenamiento) y un valor asociado.
    """
    def __init__(self, clave, valor): 
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1
        # Almacena el valor mínimo y máximo del subárbol para consultas de rango
        self.max_valor_subarbol = valor
        self.min_valor_subarbol = valor

    def __str__(self):
        """
        Representación en cadena del nodo (clave: valor).
        """
        # Formatea la clave si es un objeto datetime para una mejor lectura
        if isinstance(self.clave, datetime.datetime):
            return f"({self.clave.strftime('%d/%m/%Y')}: {self.valor})"
        return f"({self.clave}: {self.valor})"
    
class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.cantidad_nodos = 0

    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierda) - self._get_altura(nodo.derecha)

    def _actualizar_alturas_y_extremos(self, nodo):
        if not nodo:
            return

        nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))

        # Actualizar min/max_valor_subarbol basado en el valor del nodo y sus hijos
        nodo.max_valor_subarbol = nodo.valor
        nodo.min_valor_subarbol = nodo.valor

        if nodo.izquierda:
            nodo.max_valor_subarbol = max(nodo.max_valor_subarbol, nodo.izquierda.max_valor_subarbol)
            nodo.min_valor_subarbol = min(nodo.min_valor_subarbol, nodo.izquierda.min_valor_subarbol)
        if nodo.derecha:
            nodo.max_valor_subarbol = max(nodo.max_valor_subarbol, nodo.derecha.max_valor_subarbol)
            nodo.min_valor_subarbol = min(nodo.min_valor_subarbol, nodo.derecha.min_valor_subarbol)

    def _rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        self._actualizar_alturas_y_extremos(z)
        self._actualizar_alturas_y_extremos(y)
        return y

    def _rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        self._actualizar_alturas_y_extremos(z)
        self._actualizar_alturas_y_extremos(y)
        return y

    def _insertar_recursivo(self, nodo, clave, valor):
        if not nodo:
            self.cantidad_nodos += 1
            return NodoAVL(clave, valor)
        
        if clave < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, clave, valor)
        else: # La clave ya existe, actualizar el valor
            nodo.valor = valor
            self._actualizar_alturas_y_extremos(nodo)
            return nodo

        self._actualizar_alturas_y_extremos(nodo)
        balance = self._get_balance(nodo)

        # Casos de desbalanceo
        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotacion_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def insertar(self, clave, valor):
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def _borrar_recursivo(self, nodo, clave):
        if not nodo:
            return nodo

        if clave < nodo.clave:
            nodo.izquierda = self._borrar_recursivo(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._borrar_recursivo(nodo.derecha, clave)
        else: # Nodo encontrado, se debe borrar
            if nodo.izquierda is None:
                temp = nodo.derecha
                self.cantidad_nodos -= 1
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                self.cantidad_nodos -= 1
                return temp

            temp = self._min_valor_nodo(nodo.derecha)
            nodo.clave = temp.clave
            nodo.valor = temp.valor
            # Actualizar también los valores de subárbol para el nodo actual
            nodo.max_valor_subarbol = temp.max_valor_subarbol
            nodo.min_valor_subarbol = temp.min_valor_subarbol
            nodo.derecha = self._borrar_recursivo(nodo.derecha, temp.clave)

        if nodo is None:
            return nodo

        self._actualizar_alturas_y_extremos(nodo)
        balance = self._get_balance(nodo)

        # Casos de desbalanceo
        if balance > 1 and self._get_balance(nodo.izquierda) >= 0:
            return self._rotacion_derecha(nodo)
        if balance < -1 and self._get_balance(nodo.derecha) <= 0:
            return self._rotacion_izquierda(nodo)
        if balance > 1 and self._get_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        if balance < -1 and self._get_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def borrar(self, clave):
        # Comprobar si la clave existe antes de intentar borrar para decrementar correctamente
        if self.buscar_nodo(clave):
            self.raiz = self._borrar_recursivo(self.raiz, clave)
            return True
        return False # No se encontró la clave para borrar

    def buscar_nodo(self, clave):
        nodo = self.raiz
        while nodo:
            if clave == nodo.clave:
                return nodo
            elif clave < nodo.clave:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        return None

    def max_valor_en_rango(self, nodo, clave1, clave2):
        if not nodo:
            return float('-inf') # Para números, un valor muy bajo
        
        # Optimización: si el nodo actual está completamente fuera del rango de consulta
        if nodo.clave > clave2:
            return self.max_valor_en_rango(nodo.izquierda, clave1, clave2)
        if nodo.clave < clave1:
            return self.max_valor_en_rango(nodo.derecha, clave1, clave2)

        # El nodo actual está en el rango o su subárbol se superpone
        current_max = float('-inf')

        # Si la clave del nodo actual está dentro del rango, consideramos su valor
        if clave1 <= nodo.clave <= clave2:
            current_max = nodo.valor
        
        # Recursivamente buscar en los subárboles
        # Es importante pasar los límites correctos al llamar recursivamente
        max_left = self.max_valor_en_rango(nodo.izquierda, clave1, clave2)
        max_right = self.max_valor_en_rango(nodo.derecha, clave1, clave2)
        
        return max(current_max, max_left, max_right)


    def min_valor_en_rango(self, nodo, clave1, clave2):
        if not nodo:
            return float('inf') # Para números, un valor muy alto

        # Optimización: si el nodo actual está completamente fuera del rango de consulta
        if nodo.clave > clave2:
            return self.min_valor_en_rango(nodo.izquierda, clave1, clave2)
        if nodo.clave < clave1:
            return self.min_valor_en_rango(nodo.derecha, clave1, clave2)
        
        # El nodo actual está en el rango o su subárbol se superpone
        current_min = float('inf')

        # Si la clave del nodo actual está dentro del rango, consideramos su valor
        if clave1 <= nodo.clave <= clave2:
            current_min = nodo.valor

        # Recursivamente buscar en los subárboles
        min_left = self.min_valor_en_rango(nodo.izquierda, clave1, clave2)
        min_right = self.min_valor_en_rango(nodo.derecha, clave1, clave2)

        return min(current_min, min_left, min_right)


    def obtener_pares_en_rango(self, nodo, clave1, clave2, resultados):
        if not nodo:
            return

        # Recorrido in-order para obtener claves ordenadas
        if nodo.clave >= clave1: # Podría haber elementos relevantes a la izquierda
            self.obtener_pares_en_rango(nodo.izquierda, clave1, clave2, resultados)

        if clave1 <= nodo.clave <= clave2:
            resultados.append((nodo.clave, nodo.valor))

        if nodo.clave <= clave2: # Podría haber elementos relevantes a la derecha
            self.obtener_pares_en_rango(nodo.derecha, clave1, clave2, resultados)

    def get_cantidad_nodos(self):
        return self.cantidad_nodos

    # Sobrecarga __str__ para AVLTree (Opción B: Estructurada, más útil para genericidad)
    def __str__(self):
        if not self.raiz:
            return "Árbol AVL vacío."
        
        def _print_tree_recursive(nodo, level=0, prefix="Root: "):
            ret = ""
            if nodo:
                balance = self._get_balance(nodo)
                # Intenta formatear la clave si es datetime, de lo contrario, úsala directamente
                clave_display = nodo.clave.strftime('%d/%m/%Y') if isinstance(nodo.clave, datetime.datetime) else str(nodo.clave)
                valor_display = str(nodo.valor)
                min_sub_display = str(nodo.min_valor_subarbol)
                max_sub_display = str(nodo.max_valor_subarbol)

                ret += "    " * level + prefix + \
                       f"({clave_display}: {valor_display}, H: {nodo.altura}, B: {balance}, " \
                       f"MinS: {min_sub_display}, MaxS: {max_sub_display})\n"
                
                # Recursively call and append the results
                ret += _print_tree_recursive(nodo.izquierda, level + 1, "L--- ")
                ret += _print_tree_recursive(nodo.derecha, level + 1, "R--- ")
            return ret
        
        # Start the recursive printing from the root
        return _print_tree_recursive(self.raiz)
        
        return _print_tree(self.raiz)