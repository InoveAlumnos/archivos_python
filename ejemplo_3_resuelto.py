# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---

    csvfile = open('alturas.csv')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    alturas = list(csv.DictReader(csvfile))

    # Una vez leido los datos, cerrar el archivo
    csvfile.close()

    # Recorremos las filas del archivo
    # Acumular el stock de arandelas
    cantidad_alturas = 0
    suma_alturas = 0
    for i in range(len(alturas)):
        # ¡Ojo! Todos los datos de un CSV son texto
        # Hay que pasarlos a números (int o float)
        # si realizaremos operaciones matemáticas como la suma
        if alturas[i]["genero"] == genero:
            altura = float(alturas[i]["altura"])
            suma_alturas += altura
            cantidad_alturas += 1

    # Calcular promedio
    promedio = suma_alturas / cantidad_alturas

    # Imprimir valores
    print(f"Cantidad de personas de género {genero}: {cantidad_alturas}")
    print(f"Promedio de todas las alturas: {promedio}")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
