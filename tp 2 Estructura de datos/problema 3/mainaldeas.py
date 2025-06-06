# main_aldeas.py

import os
from modules.grafo import Grafo # Importa la clase Grafo 
import heapq # Se mantiene aquí porque resolver_problema_aldeas lo usa directamente

def resolver_problema_aldeas(contenido_archivo, aldea_origen="Peligros"):
    """
    Resuelve el problema de la entrega de mensajes de William desde la aldea de origen
    a todas las demás aldeas de la forma más eficiente (costo mínimo total).

    Args:
        contenido_archivo (str): El contenido del archivo de datos de aldeas.
        aldea_origen (str): El nombre de la aldea desde la que se inician los envíos.

    Returns:
        tuple: Una tupla que contiene:
            - list: Lista de aldeas en orden alfabético.
            - dict: Información de entrega (de quién recibe y a quién envía réplicas).
            - int: Suma total de las distancias recorridas.
    """
    mi_grafo = Grafo()
    todas_las_aldeas = set()

    for linea in contenido_archivo.splitlines():
        if linea.strip() == "":
            continue

        partes = linea.strip().split(', ')

        if len(partes) == 3:
            # Tupla (S, T, d)
            origen_clave, destino_clave, distancia = partes[0], partes[1], int(partes[2])
            mi_grafo.agregarArista(origen_clave, destino_clave, distancia)
            todas_las_aldeas.add(origen_clave)
            todas_las_aldeas.add(destino_clave)
        elif len(partes) == 1:
            # Solo un nombre de aldea
            if partes[0] not in mi_grafo: # Usar el método __contains__ de Grafo
                mi_grafo.agregarVertice(partes[0])
            todas_las_aldeas.add(partes[0])

    aldeas_ordenadas = sorted(list(todas_las_aldeas))

    # Implementación de Dijkstra
    distancias = {vertice_clave: float('infinity') for vertice_clave in mi_grafo.obtenerVertices()}
    aldeas_previas = {vertice_clave: None for vertice_clave in mi_grafo.obtenerVertices()}
    
    distancias[aldea_origen] = 0
    # Cola de prioridad: (distancia_acumulada, clave_vertice)
    cola_prioridad = [(0, aldea_origen)]

    while cola_prioridad:
        distancia_actual, clave_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[clave_actual]:
            continue

        vertice_actual_obj = mi_grafo.obtenerVertice(clave_actual)

        if vertice_actual_obj is None:
            continue

        for vecino_obj in vertice_actual_obj.obtenerConexiones():
            peso_arista = vertice_actual_obj.obtenerPeso(vecino_obj)
            distancia_a_vecino = distancia_actual + peso_arista

            if distancia_a_vecino < distancias[vecino_obj.obtenerClave()]:
                distancias[vecino_obj.obtenerClave()] = distancia_a_vecino
                aldeas_previas[vecino_obj.obtenerClave()] = clave_actual
                heapq.heappush(cola_prioridad, (distancia_a_vecino, vecino_obj.obtenerClave()))

    # Reconstrucción del árbol de caminos más cortos y cálculo de la suma de distancias
    info_propagacion = {aldea: {"recibe_de": None, "envia_a": []} for aldea in aldeas_ordenadas}
    suma_total_distancias_recorridas = 0

    for aldea_clave in aldeas_ordenadas:
        if aldea_clave == aldea_origen:
            info_propagacion[aldea_clave]["recibe_de"] = "ORIGEN"
        else:
            remitente_clave = aldeas_previas[aldea_clave]
            if remitente_clave is not None:
                info_propagacion[aldea_clave]["recibe_de"] = remitente_clave
                
                # Solo agrega la aldea clave a la lista de 'envia_a' del remitente
                # si no ha sido agregada previamente (para evitar duplicados en caso de rutas múltiples equivalentes)
                if aldea_clave not in info_propagacion[remitente_clave]["envia_a"]:
                    info_propagacion[remitente_clave]["envia_a"].append(aldea_clave)

                # Sumamos el peso de la arista que forma parte del árbol de caminos más cortos
                remitente_obj = mi_grafo.obtenerVertice(remitente_clave)
                receptor_obj = mi_grafo.obtenerVertice(aldea_clave)
                
                if remitente_obj and receptor_obj:
                    costo_envio = remitente_obj.obtenerPeso(receptor_obj)
                    if costo_envio is not None:
                        suma_total_distancias_recorridas += costo_envio

    return aldeas_ordenadas, info_propagacion, suma_total_distancias_recorridas

# --- Lógica para leer el archivo y ejecutar el programa ---
if __name__ == "__main__":
    # Construye la ruta al archivo 'aldeas.txt' de forma relativa
    script_dir = os.path.dirname(__file__) # Directorio donde está main_aldeas.py
    file_path = os.path.join(script_dir, 'docs', 'aldeas.txt')

    contenido_aldeas = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contenido_aldeas = f.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        exit(1)
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        exit(1)

    aldeas_ordenadas_result, detalles_entrega_result, distancia_total_result = resolver_problema_aldeas(contenido_aldeas)

    print("### Lista de Aldeas (orden alfabético):")
    for aldea in aldeas_ordenadas_result:
        print(f"* {aldea}")

    print("\n### Ruta más Eficiente de Peligros a todas las Aldeas:")
    print("|      Aldea Receptora    |        Recibe de    |          Envía réplicas a |")
    print("| :---------------------- | :--------------------- | :------------------------ |")
    for aldea in aldeas_ordenadas_result:
        recibe_de = detalles_entrega_result[aldea]["recibe_de"] if detalles_entrega_result[aldea]["recibe_de"] != "ORIGEN" else ""
        envia_a = ", ".join(sorted(detalles_entrega_result[aldea]["envia_a"]))
        print(f"||||||||||| {aldea} |||||||||||| {recibe_de} |||||||||||| {envia_a} ||||||||||||")

    print(f"\n### Suma Total de Distancias Recorridas:")
    print(f"La suma de todas las distancias recorridas por todas las palomas enviadas para entregar el mensaje a todas las aldeas de la forma más eficiente es de **{distancia_total_result} leguas**.")
