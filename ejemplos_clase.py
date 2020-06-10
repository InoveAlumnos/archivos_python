#!/usr/bin/env python
'''
Archivos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def translate(word, language):
    print(language[word])


def diccionario():
    # Crear diccionarios de idioma
    portugues = {}
    espanol = {}

    portugues['hello'] = 'oi'
    portugues['by'] = 'tchau'
    espanol['hello'] = 'hola'
    espanol['by'] = 'adios'

    translate('hello', espanol)  # print --> hola
    translate('by', portugues)   # print --> tchau

    key = 'hell'
    try:
        print(portugues[key])      # lanza una excepción
    except:
        print('No se ha encontrado la clave', key)
    print(portugues.get(key))      # print --> None


def read_txt():
    # Open file
    fi = open('texto.txt', 'r')

    # Leer totalidad o por cantidad
    contenido_completo = fi.read()
    contenido_parcial = fi.read(20)

    # Regresar el cursor al comienzo
    fi.seek(0)

    contenido_parcial = fi.read(20)

    # Regresar el cursor al comienzo
    fi.seek(0)

    # Lectura por línea
    line = fi.readline()
    print('Linea:', line)

    # Close file
    fi.close()

    # Iterar sobre todas las líneas
    with open('texto.txt') as fi:
        for line in fi:
            print('Linea:', line, end='')


def write_txt():
    # Open file para sólo escritura
    fo = open('reporte.txt', 'w')

    fo.write("resultado=4\n")

    fo.close()

    # Open file para añadir contenido
    fo = open('reporte.txt', 'a')

    lines = ["Hola Mundo!\n", "Inove Escuela de codigo\n"]
    fo.writelines(lines)

    fo.flush()  # Bajar contenido a disco (RAM --> FLASH)
    fo.close()  # Cerrar archivo


def read_csv():
    # Lectura de archivo CSV sin formato
    with open('propiedades.csv') as csvfile:
        data = list(csv.reader(csvfile))

    # Lectura de archivo CSV con diccionario
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

    row = data[0]
    print('Fila 0:', row)
    print('Fila 0, dato latitud:', row.get('latitud'))

    latitud = data[0].get('latitud')
    print('Latitud:', latitud)

    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        if i == 5:
            break
        row = data[i]
        latitud = float(row.get('latitud'))
        print('Fila', i, 'dato latitud:', latitud)


def write_csv():
    # Abrir archivo para escritura
    csvfile = open('agenda.csv', 'w', newline='')

    # Detallar los nombres de las columnas
    header = ['nombre', 'apellido', 'numero']
    # Crear el objeto para escribir las lineas de archivo
    # basado en los nombres de las columnas
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()
    writer.writerow({'nombre': 'Max', 'apellido': 'Power'})
    writer.writerow({'apellido': 'School', 'nombre': 'Inove', 'numero': '12345678'})

    csvfile.close()


def read_csv_vieja_escuela():
    # Leer archivos CSV como si fuera un lenguaje de bajo nivel
    data = []
    count = 0
    with open('propiedades.csv') as fi:
        for line in fi:
            line = re.sub('\n', '', line)
            row = line.split(',')
            print('Linea ', count, ': ', row, sep='')
            data.append(row)
            count += 1
            if count >= 5:
                break


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    diccionario()
    read_txt()
    write_txt()
    read_csv()
    write_csv()
    read_csv_vieja_escuela()
