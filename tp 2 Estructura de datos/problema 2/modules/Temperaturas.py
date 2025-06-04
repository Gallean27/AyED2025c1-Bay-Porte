import datetime

class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura
        self.izquierda = None
        self.derecha = None
        self.altura = 1
        self.max_temp_subarbol = temperatura
        self.min_temp_subarbol = temperatura

class Temperaturas_DB:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

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

        # Actualizar min/max_temp_subarbol
        nodo.max_temp_subarbol = nodo.temperatura
        nodo.min_temp_subarbol = nodo.temperatura

        if nodo.izquierda:
            nodo.max_temp_subarbol = max(nodo.max_temp_subarbol, nodo.izquierda.max_temp_subarbol)
            nodo.min_temp_subarbol = min(nodo.min_temp_subarbol, nodo.izquierda.min_temp_subarbol)
        if nodo.derecha:
            nodo.max_temp_subarbol = max(nodo.max_temp_subarbol, nodo.derecha.max_temp_subarbol)
            nodo.min_temp_subarbol = min(nodo.min_temp_subarbol, nodo.derecha.min_temp_subarbol)

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

    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            self.cantidad += 1
            return NodoAVL(fecha, temperatura)
        if fecha < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.derecha = self._insertar(nodo.derecha, fecha, temperatura)
        else: # La fecha ya existe, actualizar la temperatura
            nodo.temperatura = temperatura
            self._actualizar_alturas_y_extremos(nodo) # Asegurarse de que se actualicen los extremos si cambia la temperatura
            return nodo

        self._actualizar_alturas_y_extremos(nodo)

        balance = self._get_balance(nodo)

        # Caso Izquierda-Izquierda
        if balance > 1 and fecha < nodo.izquierda.fecha:
            return self._rotacion_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and fecha > nodo.derecha.fecha:
            return self._rotacion_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and fecha > nodo.izquierda.fecha:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and fecha < nodo.derecha.fecha:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def guardar_temperatura(self, temperatura, fecha_str):
        """
        Guarda la medida de temperatura asociada a la fecha.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        if self.raiz is None or self._buscar_nodo(self.raiz, fecha) is None:
            # Solo incrementar si es una nueva fecha
            self.raiz = self._insertar(self.raiz, fecha, temperatura)
        else:
            # Si la fecha ya existe, _insertar la actualizará, no incrementamos la cantidad.
            self.raiz = self._insertar(self.raiz, fecha, temperatura)


    def _buscar_nodo(self, nodo, fecha):
        if not nodo:
            return None
        if fecha == nodo.fecha:
            return nodo
        elif fecha < nodo.fecha:
            return self._buscar_nodo(nodo.izquierda, fecha)
        else:
            return self._buscar_nodo(nodo.derecha, fecha)

    def devolver_temperatura(self, fecha_str):
        """
        Devuelve la medida de temperatura en la fecha determinada.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        nodo = self._buscar_nodo(self.raiz, fecha)
        if nodo:
            return nodo.temperatura
        return None # O lanzar una excepción si la fecha no se encuentra

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def _borrar(self, nodo, fecha):
        if not nodo:
            return nodo

        if fecha < nodo.fecha:
            nodo.izquierda = self._borrar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self._borrar(nodo.derecha, fecha)
        else: # Nodo encontrado, se debe borrar
            if nodo.izquierda is None:
                temp = nodo.derecha
                self.cantidad -= 1
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                self.cantidad -= 1
                return temp

            # Nodo con dos hijos: obtener el sucesor in-order (el más pequeño en el subárbol derecho)
            temp = self._min_valor_nodo(nodo.derecha)
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            nodo.derecha = self._borrar(nodo.derecha, temp.fecha)

        if nodo is None:
            return nodo

        self._actualizar_alturas_y_extremos(nodo)

        balance = self._get_balance(nodo)

        # Casos de desbalanceo (mismas rotaciones que la inserción)
        # Caso Izquierda-Izquierda
        if balance > 1 and self._get_balance(nodo.izquierda) >= 0:
            return self._rotacion_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and self._get_balance(nodo.derecha) <= 0:
            return self._rotacion_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and self._get_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and self._get_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def borrar_temperatura(self, fecha_str):
        """
        Recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        # Antes de borrar, verificar si la fecha existe para no decrementar si no se encuentra
        if self._buscar_nodo(self.raiz, fecha):
            self.raiz = self._borrar(self.raiz, fecha)
        else:
            print(f"La fecha {fecha_str} no se encuentra en la base de datos.")


    def _max_temp_rango_interno(self, nodo, fecha1, fecha2):
        if not nodo:
            return float('-inf')

        # Si el rango del nodo está completamente fuera del rango de consulta
        if nodo.fecha > fecha2:
            return self._max_temp_rango_interno(nodo.izquierda, fecha1, fecha2)
        if nodo.fecha < fecha1:
            return self._max_temp_rango_interno(nodo.derecha, fecha1, fecha2)

        # Si el rango del nodo está completamente dentro del rango de consulta
        # Y el nodo contiene el max del subarbol en sí mismo
        if fecha1 <= nodo.fecha and nodo.fecha <= fecha2:
            current_max = nodo.temperatura
            # Podemos usar los valores precalculados del subárbol si el subárbol está dentro del rango
            if nodo.izquierda and nodo.izquierda.fecha >= fecha1:
                 current_max = max(current_max, nodo.izquierda.max_temp_subarbol)
            if nodo.derecha and nodo.derecha.fecha <= fecha2:
                 current_max = max(current_max, nodo.derecha.max_temp_subarbol)

            # Si alguna parte del subárbol se extiende fuera del rango, debemos explorar esa parte
            if nodo.izquierda and nodo.izquierda.fecha < fecha1:
                current_max = max(current_max, self._max_temp_rango_interno(nodo.izquierda, fecha1, fecha2))
            if nodo.derecha and nodo.derecha.fecha > fecha2:
                current_max = max(current_max, self._max_temp_rango_interno(nodo.derecha, fecha1, fecha2))
            return current_max
        
        # Caso general: el nodo podría no estar en el rango, pero sus hijos sí.
        # Esto sucede cuando el rango de consulta no "contiene" el nodo central,
        # pero se superpone con sus subárboles.
        res = float('-inf')
        if fecha1 <= nodo.fecha <= fecha2:
            res = max(res, nodo.temperatura)

        res = max(res, self._max_temp_rango_interno(nodo.izquierda, fecha1, fecha2))
        res = max(res, self._max_temp_rango_interno(nodo.derecha, fecha1, fecha2))
        return res

    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")
        max_val = self._max_temp_rango_interno(self.raiz, fecha1, fecha2)
        return max_val if max_val != float('-inf') else None


    def _min_temp_rango_interno(self, nodo, fecha1, fecha2):
        if not nodo:
            return float('inf')

        if nodo.fecha > fecha2:
            return self._min_temp_rango_interno(nodo.izquierda, fecha1, fecha2)
        if nodo.fecha < fecha1:
            return self._min_temp_rango_interno(nodo.derecha, fecha1, fecha2)

        if fecha1 <= nodo.fecha and nodo.fecha <= fecha2:
            current_min = nodo.temperatura
            if nodo.izquierda and nodo.izquierda.fecha >= fecha1:
                 current_min = min(current_min, nodo.izquierda.min_temp_subarbol)
            if nodo.derecha and nodo.derecha.fecha <= fecha2:
                 current_min = min(current_min, nodo.derecha.min_temp_subarbol)
            
            if nodo.izquierda and nodo.izquierda.fecha < fecha1:
                current_min = min(current_min, self._min_temp_rango_interno(nodo.izquierda, fecha1, fecha2))
            if nodo.derecha and nodo.derecha.fecha > fecha2:
                current_min = min(current_min, self._min_temp_rango_interno(nodo.derecha, fecha1, fecha2))
            return current_min

        res = float('inf')
        if fecha1 <= nodo.fecha <= fecha2:
            res = min(res, nodo.temperatura)
        res = min(res, self._min_temp_rango_interno(nodo.izquierda, fecha1, fecha2))
        res = min(res, self._min_temp_rango_interno(nodo.derecha, fecha1, fecha2))
        return res


    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")
        min_val = self._min_temp_rango_interno(self.raiz, fecha1, fecha2)
        return min_val if min_val != float('inf') else None


    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        min_val = self.min_temp_rango(fecha1_str, fecha2_str)
        max_val = self.max_temp_rango(fecha1_str, fecha2_str)
        return min_val, max_val

    def _devolver_temperaturas_interno(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        # Recorrido in-order para obtener fechas ordenadas
        if nodo.fecha >= fecha1: # Podría haber elementos relevantes a la izquierda
            self._devolver_temperaturas_interno(nodo.izquierda, fecha1, fecha2, resultados)

        if fecha1 <= nodo.fecha <= fecha2:
            resultados.append(f"{nodo.fecha.strftime('%d/%m/%Y')}: {nodo.temperatura} ºC")

        if nodo.fecha <= fecha2: # Podría haber elementos relevantes a la derecha
            self._devolver_temperaturas_interno(nodo.derecha, fecha1, fecha2, resultados)

    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        """
        Devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro
        con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas.
        """
        fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")
        resultados = []
        self._devolver_temperaturas_interno(self.raiz, fecha1, fecha2, resultados)
        return resultados

    def cantidad_muestras(self):
        """
        Devuelve la cantidad de muestras de la BD.
        """
        return self.cantidad