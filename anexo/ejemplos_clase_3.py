# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def agregar_datos():
    # El objetivo es abrir el archivo de edificio2.csv
    # y agregar más pisos al edificio, es decir, agregar más
    # filas a la planilla de cálculo

    # Este archivo ya tiene grabado el header (a, b, c) en
    # el archivo pero de todas formas debemos especificarlo
    header = ['a', 'b', 'c']

    # Este archivo ya tiene algunos pisos cargados, agregamos más
    # Abrir un archivo CSV con el flag "a"
    csvfile = open('edificio2.csv', 'a', newline='')

    # Generar un "escritor" para modificar el archivo
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Crear el nuevo piso
    nuevo_piso = {'a': 'San Luis', 'b': 'Corrientes', 'c': 'Salta'}

    # Escribirlo en el archivo
    writer.writerow(nuevo_piso)

    # Cerrar el archivo
    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    agregar_datos()
