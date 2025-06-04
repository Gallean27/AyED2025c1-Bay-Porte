# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6]

# Usaremos un contador global para el id de llegada
_next_id = 0 # Inicializar el contador

class Paciente:
    def __init__(self):
        global _next_id # Declarar que vamos a modificar la variable global
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__id_llegada = _next_id # Asigna el id de llegada actual
        _next_id += 1 # Incrementa el contador para el próximo paciente

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo

    def get_descripcion_riesgo(self):
        return self.__descripcion

    def get_id_llegada(self): # Nuevo método para obtener el id de llegada
        return self.__id_llegada

    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += f' (ID Llegada: {self.__id_llegada})' # Añadir el ID de llegada para visualización
        return cad