import datetime

from Temperaturas import Temperaturas_DB


from Temperaturas import NodoAVL




# Las clases NodoAVL y Temperaturas_DB se asumen definidas previamente

def probar_temperaturas_db():
    print("--- Probando Temperaturas_DB ---")
    db = Temperaturas_DB()

    # 1. Guardar temperaturas
    print("\n--- Guardando temperaturas ---")
    db.guardar_temperatura(25.5, "01/01/2023")
    db.guardar_temperatura(28.0, "15/01/2023")
    db.guardar_temperatura(22.3, "05/01/2023")
    db.guardar_temperatura(30.1, "20/01/2023")
    db.guardar_temperatura(19.8, "10/01/2023")
    db.guardar_temperatura(26.7, "02/02/2023")
    db.guardar_temperatura(24.0, "25/01/2023")
    db.guardar_temperatura(27.5, "03/02/2023") # Fecha repetida, debería actualizar
    db.guardar_temperatura(27.0, "03/02/2023") # Actualizar temp para 03/02/2023

    print(f"Cantidad de muestras después de guardar: {db.cantidad_muestras()}") # Debería ser 7

    # 2. Devolver temperatura
    print("\n--- Devolviendo temperaturas específicas ---")
    print(f"Temperatura el 01/01/2023: {db.devolver_temperatura('01/01/2023')} ºC") # Esperado: 25.5
    print(f"Temperatura el 10/01/2023: {db.devolver_temperatura('10/01/2023')} ºC") # Esperado: 19.8
    print(f"Temperatura el 03/02/2023: {db.devolver_temperatura('03/02/2023')} ºC") # Esperado: 27.0
    print(f"Temperatura el 04/02/2023 (no existe): {db.devolver_temperatura('04/02/2023')}") # Esperado: None

    # 3. Max/Min temperatura en rango
    print("\n--- Max/Min temperaturas en rangos ---")
    print(f"Máxima temp entre 01/01/2023 y 31/01/2023: {db.max_temp_rango('01/01/2023', '31/01/2023')} ºC") # Esperado: 30.1
    print(f"Mínima temp entre 01/01/2023 y 31/01/2023: {db.min_temp_rango('01/01/2023', '31/01/2023')} ºC") # Esperado: 19.8
    print(f"Máxima temp entre 01/02/2023 y 28/02/2023: {db.max_temp_rango('01/02/2023', '28/02/2023')} ºC") # Esperado: 27.0
    print(f"Mínima temp entre 01/02/2023 y 28/02/2023: {db.min_temp_rango('01/02/2023', '28/02/2023')} ºC") # Esperado: 26.7

    min_max_temp = db.temp_extremos_rango('01/01/2023', '31/01/2023')
    print(f"Extremos temp entre 01/01/2023 y 31/01/2023: Min={min_max_temp[0]}ºC, Max={min_max_temp[1]}ºC") # Esperado: Min=19.8, Max=30.1

    # 4. Devolver temperaturas en rango
    print("\n--- Temperaturas en rango ---")
    rango_completo = db.devolver_temperaturas('01/01/2023', '28/02/2023')
    print("Temperaturas entre 01/01/2023 y 28/02/2023:")
    for temp_str in rango_completo:
        print(temp_str)
    # Esperado (ordenado por fecha):
    # 01/01/2023: 25.5 ºC
    # 05/01/2023: 22.3 ºC
    # 10/01/2023: 19.8 ºC
    # 15/01/2023: 28.0 ºC
    # 20/01/2023: 30.1 ºC
    # 25/01/2023: 24.0 ºC
    # 02/02/2023: 26.7 ºC
    # 03/02/2023: 27.0 ºC


    # 5. Borrar temperatura
    print("\n--- Borrando temperaturas ---")
    print(f"Cantidad de muestras antes de borrar: {db.cantidad_muestras()}") # Esperado: 7

    db.borrar_temperatura("10/01/2023")
    print(f"Cantidad de muestras después de borrar 10/01/2023: {db.cantidad_muestras()}") # Esperado: 6
    print(f"Temperatura el 10/01/2023 (después de borrar): {db.devolver_temperatura('10/01/2023')}") # Esperado: None

    db.borrar_temperatura("01/01/2023")
    print(f"Cantidad de muestras después de borrar 01/01/2023: {db.cantidad_muestras()}") # Esperado: 5

    db.borrar_temperatura("15/03/2023") # Intentar borrar una fecha que no existe
    print(f"Cantidad de muestras después de intentar borrar fecha inexistente: {db.cantidad_muestras()}") # Esperado: 5

    # 6. Re-verificar rangos después de borrar
    print("\n--- Re-verificando rangos después de borrar ---")
    print(f"Máxima temp entre 01/01/2023 y 31/01/2023: {db.max_temp_rango('01/01/2023', '31/01/2023')} ºC") # Esperado: 30.1
    print(f"Mínima temp entre 01/01/2023 y 31/01/2023: {db.min_temp_rango('01/01/2023', '31/01/2023')} ºC") # Esperado: 22.3 (antes era 19.8)

    rango_despues_borrado = db.devolver_temperaturas('01/01/2023', '28/02/2023')
    print("Temperaturas entre 01/01/2023 y 28/02/2023 (después de borrar):")
    for temp_str in rango_despues_borrado:
        print(temp_str)
    # Esperado (ordenado por fecha, sin 01/01/2023 y 10/01/2023):
    # 05/01/2023: 22.3 ºC
    # 15/01/2023: 28.0 ºC
    # 20/01/2023: 30.1 ºC
    # 25/01/2023: 24.0 ºC
    # 02/02/2023: 26.7 ºC
    # 03/02/2023: 27.0 ºC

    print("\n--- Pruebas completadas ---")

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_temperaturas_db()