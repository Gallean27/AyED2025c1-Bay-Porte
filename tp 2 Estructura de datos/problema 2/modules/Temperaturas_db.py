
import datetime

from ArbolAVL import ArbolAVL

## Clase Temperaturas_DB

#`Temperaturas_DB` instanciará un ArbolAVL y usará sus métodos internos para realizar las operaciones, manejando la conversión de fechas.

#```python
class Temperaturas_DB:
    def __init__(self):
        # Instanciamos la clase ArbolAVL internamente
        self.arbol_avl = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha_str):
        """
        Guarda la medida de temperatura asociada a la fecha.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        self.arbol_avl.insertar(fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        """
        Devuelve la medida de temperatura en la fecha determinada.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        nodo = self.arbol_avl.buscar_nodo(fecha)
        if nodo:
            return nodo.valor
        return None

    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")
        max_val = self.arbol_avl.max_valor_en_rango(self.arbol_avl.raiz, fecha1, fecha2)
        return max_val if max_val != float('-inf') else None

    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")
        min_val = self.arbol_avl.min_valor_en_rango(self.arbol_avl.raiz, fecha1, fecha2)
        return min_val if min_val != float('inf') else None

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        """
        min_val = self.min_temp_rango(fecha1_str, fecha2_str)
        max_val = self.max_temp_rango(fecha1_str, fecha2_str)
        return min_val, max_val

    def borrar_temperatura(self, fecha_str):
        """
        Recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        """
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        # Asegurarse de que el nodo exista antes de intentar borrar
        if self.arbol_avl.buscar_nodo(fecha):
            self.arbol_avl.borrar(fecha)
        else:
            print(f"La fecha {fecha_str} no se encuentra en la base de datos.")


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
        self.arbol_avl.obtener_pares_en_rango(self.arbol_avl.raiz, fecha1, fecha2, resultados)
        # Los resultados ya vienen ordenados por fecha debido al recorrido in-order
        return [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in resultados]

    def cantidad_muestras(self):
        """
        Devuelve la cantidad de muestras de la BD.
        """
        return self.arbol_avl.get_cantidad_nodos()