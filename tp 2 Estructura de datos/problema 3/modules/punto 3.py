import collections
import heapq # Implementación de montículo de mínimos (min-heap) incorporada de Python para la cola de prioridad

# Archivo aldeas.txt simulado como una cadena de texto
aldeas_file_content = """
Lomaseca, Pepino, 3
Lomaseca, Los Infiernos, 2
Lomaseca, El Cerrillo, 5
Lomaseca, Peligros, 7
El Cerrillo, Lomaseca, 5
El Cerrillo, Los Infiernos, 5
El Cerrillo, Malcocinado, 6
Hortijos, Humilladero, 5
Hortijos, Villaviciosa, 10
Hortijos, Cebolla, 20
Torralta, Silla, 4
Torralta, Villaviciosa, 8
Torralta, Humilladero, 9
Humilladero, Hortijos, 5
Humilladero, Torralta, 9
La Pera, Los Infiernos, 3
La Pera, Pepino, 4
La Pera, Espera, 3
Pepino, Espera, 4
Pepino, Lomaseca, 3
Pepino, La Pera, 4
Elciego, Diosleguarde, 7
Elciego, Melón, 3
Villaviciosa, Hortijos, 10
Villaviciosa, Torralta, 8
Consuegra, Malcocinado, 1
Malcocinado, El Cerrillo, 6
Malcocinado, Consuegra, 1
Malcocinado, Aceituna, 2
Malcocinado, Peligros, 8
Malcocinado, Diosleguarde, 9
Peligros, Lomaseca, 7
Peligros, Malcocinado, 8
Peligros, La Aparecida, 5
Silla, Torralta, 4
Silla, Pancrudo, 6
Silla, La Aparecida, 5
Cebolla, Hortijos, 20
Cebolla, Buenas Noches, 2
Cebolla, Pancrudo, 2
La Aparecida, Peligros, 5
La Aparecida, Silla, 5
La Aparecida, Pancrudo, 8
La Aparecida, Buenas Noches, 3
Melón, Elciego, 3
Melón, Diosleguarde, 11
Melón, Buenas Noches, 20
Los Infiernos, Lomaseca, 2
Los Infiernos, La Pera, 3
Los Infiernos, El Cerrillo, 5
Espera, Pepino, 4
Espera, La Pera, 3
Aceituna, Malcocinado, 2
Pancrudo, Silla, 6
Pancrudo, Cebolla, 2
Pancrudo, La Aparecida, 8
Diosleguarde
Diosleguarde, Elciego, 7
Diosleguarde, Malcocinado, 9
Diosleguarde, Melón, 11
Buenas Noches, Cebolla, 2
Buenas Noches, La Aparecida, 3
Buenas Noches, Melón, 20
"""

def parse_aldeas_data(file_content):
    graph = collections.defaultdict(list)
    aldeas_set = set()
    lines = file_content.strip().split('\n')
    for line in lines:
        parts = line.split(', ')
        if len(parts) == 3:
            start_aldea = parts[0].strip()
            end_aldea = parts[1].strip()
            distance = int(parts[2].strip())

            graph[start_aldea].append((end_aldea, distance))
            graph[end_aldea].append((start_aldea, distance)) # Bidireccional

            aldeas_set.add(start_aldea)
            aldeas_set.add(end_aldea)
        elif len(parts) == 1 and parts[0].strip(): # Manejar casos donde una línea podría ser solo el nombre de una aldea y no está vacía
            aldeas_set.add(parts[0].strip())
    return graph, sorted(list(aldeas_set))

def prim_mst_with_parent_map(graph, start_node):
    min_span_tree_edges = [] # Lista de (origen, destino, distancia)
    total_distance = 0
    visited = set()
    # la cola de prioridad almacena tuplas: (distancia, destino, origen)
    priority_queue = [(0, start_node, None)] # (distancia a la aldea_actual, aldea_actual, aldea_origen)

    # Diccionario para almacenar la mejor arista encontrada hasta ahora para alcanzar un nodo: {nodo: (distancia, nodo_origen)}
    min_edge_to_node = {node: (float('inf'), None) for node in graph}
    min_edge_to_node[start_node] = (0, None)

    while priority_queue:
        distance, current_aldea, source_aldea = heapq.heappop(priority_queue)

        if current_aldea in visited:
            continue

        visited.add(current_aldea)
        total_distance += distance

        if source_aldea is not None: # No agregar la arista para el nodo de inicio mismo
            min_span_tree_edges.append((source_aldea, current_aldea, distance))

        for neighbor, weight in graph[current_aldea]:
            if neighbor not in visited:
                # Si este camino hacia el vecino es mejor que lo que conocemos actualmente
                if weight < min_edge_to_node[neighbor][0]:
                    min_edge_to_node[neighbor] = (weight, current_aldea)
                    # Empujar o actualizar en el montículo. heapq no soporta la actualización, así que empujamos entradas duplicadas.
                    # La comprobación `if neighbor in visited` maneja las entradas más antiguas y peores.
                    heapq.heappush(priority_queue, (weight, neighbor, current_aldea))

    return min_span_tree_edges, total_distance, visited

# Procesar los datos
graph, all_aldeas = parse_aldeas_data(aldeas_file_content)

# Ejecutar el algoritmo de Prim
start_aldea = "Peligros"
mst_edges, total_cost, connected_aldeas = prim_mst_with_parent_map(graph, start_aldea)

# Verificar que las 22 aldeas esperadas estén conectadas
# Primero, asegurarse de que 'Diosleguarde' esté en all_aldeas, ya que aparece solo en el archivo
# Esta comprobación asume que all_aldeas tendrá 22 entradas según la descripción del problema
expected_num_aldeas = 22
if len(connected_aldeas) != expected_num_aldeas:
    print(f"Advertencia: Se conectaron {len(connected_aldeas)} aldeas, se esperaban {expected_num_aldeas}.")
    print("Aldeas conectadas:", sorted(list(connected_aldeas)))
    print("Aldeas no conectadas:", sorted(list(set(all_aldeas) - connected_aldeas)))


# Construir las relaciones padre-hijo para la salida
aldea_info = collections.defaultdict(lambda: {'recibe_de': None, 'envia_a': []})

# Inicializar todas las aldeas encontradas al parsear con la estructura básica, asegurándose de que estén en el diccionario
for aldea in all_aldeas:
    if aldea in connected_aldeas: # Solo procesar aldeas conectadas
        aldea_info[aldea] = {'recibe_de': None, 'envia_a': []}


# Llenar basándose en las aristas del MST
for u, v, _ in mst_edges:
    # u envía a v en la construcción del MST
    aldea_info[v]['recibe_de'] = u
    aldea_info[u]['envia_a'].append(v)

# Para Peligros, no recibe de nadie dentro del MST, es el origen
aldea_info[start_aldea]['recibe_de'] = 'Nadie (es el origen)'

# Ordenar las listas 'envia_a' para una salida consistente
for aldea in aldea_info:
    aldea_info[aldea]['envia_a'].sort()


# --- ENTREGABLES ---

# 1. Mostrar la lista de aldeas en orden alfabético.
print("--- Lista de Aldeas en orden alfabético ---")
for aldea in all_aldeas:
    print(aldea)
print("\n")

# 2. Para cada aldea, mostrar de qué vecina debería recibir la noticia, y a qué vecinas debería enviar réplicas.
print("--- Rutas de Envío y Recepción de Noticias (Forma más Eficiente) ---")
# Asegurarse de imprimir la información solo para las aldeas conectadas y en orden alfabético
for aldea in sorted(aldea_info.keys()):
    info = aldea_info[aldea]
    recibe = info['recibe_de']
    envia = ", ".join(info['envia_a']) if info['envia_a'] else "Nadie"

    print(f"Aldea: {aldea}")
    print(f"  Debería recibir la noticia de: {recibe}")
    print(f"  Debería enviar réplicas a: {envia}")
    print("-" * 40)
print("\n")

# 3. Para el envío de una noticia, mostrar la suma de todas las distancias recorridas por todas las palomas enviadas.
print("--- Suma Total de Distancias Recorridas ---")
print(f"Distancia total mínima para enviar el mensaje a todas las aldeas: {total_cost} leguas.")