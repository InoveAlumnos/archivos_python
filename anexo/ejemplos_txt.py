#!/usr/bin/env python
'''
Archivos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import csv
import re


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


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    read_txt()
    write_txt()
