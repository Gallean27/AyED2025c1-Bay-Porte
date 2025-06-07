# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
from modules.Paciente import Paciente
from modules.ColaDePrioridad import ColaDePrioridad # Importar nuestra nueva cola de prioridad
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaDePrioridad() # ¡Cambiamos a nuestra ColaDePrioridad!

# Ciclo que gestiona la simulación
for i in range(n):
   
    ahora = datetime.datetime.now()  
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S') # Fecha y hora de entrada de un paciente
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    
    
    paciente = Paciente() # Se crea un paciente un paciente por segundo.La criticidad del paciente es aleatoria
    # Insertar el paciente en la cola de prioridad junto con su ID de llegada
    cola_de_espera.insertar(paciente, paciente.get_id_llegada())

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # Se atiende el paciente de MAYOR PRIORIDAD (más crítico, o el más antiguo si tienen igual criticidad)
        if not cola_de_espera.esta_vacia(): # Asegurarse de que hay pacientes para atender
            paciente_atendido = cola_de_espera.extraer_minimo() # Extrae el paciente de mayor prioridad
            print('*'*40)
            print('Se atiende el paciente (Prioridad):', paciente_atendido)
            print('*'*40)
        else:
            print('No hay pacientes en la cola para atender en este ciclo.')
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass

    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    # Para mostrar los pacientes en orden de prioridad (simulando una vista de la cola real)
    # podríamos extraerlos todos y volver a insertarlos, o acceder a una copia ordenada.
    # Para no alterar la cola, simplemente imprimimos el contenido del heap interno.
    # Esto no estará ordenado por prioridad, pero mostrará qué pacientes están en la cola.
    print(cola_de_espera) # Usamos el método __str__ de ColaDePrioridad

    print()
    print('-*-'*15)

    time.sleep(1)