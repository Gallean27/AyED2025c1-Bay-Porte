import datetime
from modules.Temperaturas_db import Temperaturas_DB
from modules.ArbolAVL import NodoAVL
from modules.ArbolAVL import ArbolAVL

# --- INICIO DEL CÓDIGO DE PRUEBA ---
def probar_temperaturas_db():
    print("--- Probando Temperaturas_DB ---")
    db = Temperaturas_DB()

    # 1. Guardar temperaturas con 6 fechas consecutivas, como vimos en la practica para probar
    print("\n--- Guardando temperaturas con 6 fechas consecutivas ---")
    start_date = datetime.datetime(2023, 3, 1)
    for i in range(6):
        current_date = start_date + datetime.timedelta(days=i)
        date_str = current_date.strftime("%d/%m/%Y")
        temperature = 20.0 + i * 0.5 # Temperaturas ascendentes para visualización
        db.guardar_temperatura(temperature, date_str)
        print(f"Guardando {date_str}: {temperature} ºC")

    print(f"\nCantidad de muestras después de guardar 6 fechas consecutivas: {db.cantidad_muestras()}")

    print("\n--- Representación del árbol AVL después de la inserción ---")
    print(db) # Esto llama a db.__str__()

    # 2. Devolver temperatura
    print("\n--- Devolviendo temperaturas específicas ---")
    print(f"Temperatura el 01/03/2023: {db.devolver_temperatura('01/03/2023')} ºC")
    print(f"Temperatura el 03/03/2023: {db.devolver_temperatura('03/03/2023')} ºC")
    print(f"Temperatura el 06/03/2023: {db.devolver_temperatura('06/03/2023')} ºC")
    print(f"Temperatura el 07/03/2023 (no existe): {db.devolver_temperatura('07/03/2023')}")

    # 3. Max/Min temperatura en rango
    print("\n--- Max/Min temperaturas en rangos ---")
    print(f"Máxima temp entre 01/03/2023 y 06/03/2023: {db.max_temp_rango('01/03/2023', '06/03/2023')} ºC")
    print(f"Mínima temp entre 01/03/2023 y 06/03/2023: {db.min_temp_rango('01/03/2023', '06/03/2023')} ºC")

    min_max_temp = db.temp_extremos_rango('02/03/2023', '05/03/2023')
    print(f"Extremos temp entre 02/03/2023 y 05/03/2023: Min={min_max_temp[0]}ºC, Max={min_max_temp[1]}ºC")

    # 4. Devolver temperaturas en rango
    print("\n--- Temperaturas en rango ---")
    rango_completo = db.devolver_temperaturas('01/03/2023', '06/03/2023')
    print("Temperaturas entre 01/03/2023 y 06/03/2023:")
    for temp_str in rango_completo:
        print(temp_str)

    # 5. Borrar temperatura
    print("\n--- Borrando temperaturas ---")
    print(f"Cantidad de muestras antes de borrar: {db.cantidad_muestras()}")

    db.borrar_temperatura("03/03/2023")
    print(f"Cantidad de muestras después de borrar 03/03/2023: {db.cantidad_muestras()}")
    print(f"Temperatura el 03/03/2023 (después de borrar): {db.devolver_temperatura('03/03/2023')}")

    db.borrar_temperatura("01/03/2023")
    print(f"Cantidad de muestras después de borrar 01/03/2023: {db.cantidad_muestras()}")

    db.borrar_temperatura("15/03/2023") # Intentar borrar una fecha que no existe
    print(f"Cantidad de muestras después de intentar borrar fecha inexistente: {db.cantidad_muestras()}")

    # 6. Re-verificar rangos después de borrar
    print("\n--- Re-verificando rangos después de borrar ---")
    print(f"Máxima temp entre 01/03/2023 y 06/03/2023: {db.max_temp_rango('01/03/2023', '06/03/2023')} ºC")
    print(f"Mínima temp entre 01/03/2023 y 06/03/2023: {db.min_temp_rango('01/03/2023', '06/03/2023')} ºC")

    rango_despues_borrado = db.devolver_temperaturas('01/03/2023', '06/03/2023')
    print("Temperaturas entre 01/03/2023 y 06/03/2023 (después de borrar):")
    for temp_str in rango_despues_borrado:
        print(temp_str)

    print("\n--- Pruebas completadas ---")

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_temperaturas_db()