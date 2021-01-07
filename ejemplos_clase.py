#!/usr/bin/env python
'''
Archivos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

import csv
import re


def diccionario():
    # Crear un diccionario de inquilinos del primero piso
    piso_1 = {'a': 'Gutierrez', 'b': 'Naon', 'c': 'Palermo'}
  
    piso_2 = {}  # Diccionario vacio del segundo piso
    piso_2['a'] = 'Tucuman'  # 1a
    piso_2['b'] = 'Mendoza'  # 1b
    piso_2['c'] = 'Cordoba'  # 1c

    # Imprimir los diccionarios
    print(piso_1)
    print(piso_2)

    # Ahora digamos que se mundo "Mendoza"
    # y viene la familia Neuquen en su lugar:
    piso_2['b'] = 'Neuquen'  # 2b

    # ¿Quíen vive en el 1b?
    print(piso_1['b'])  # Naon

    # En que departamento del segundo piso vive Cordoba
    # Realizar un bucle de diccionarios
    # k --> key
    # v --> value
    for k,v in piso_2.items():
        if v == "Cordoba":
            print(v, "se encuentra en el departamento", k)

    # Armemos ahora el edificio de 2 pisos, el cual
    # es una lista de diccionarios
    edificio = []
    edificio.append(piso_1)
    edificio.append(piso_2)

    # Recorrer todo el edificio en búsqueda de la familia Tucuman:
    for i in range(len(edificio)):  # --> recorre los pisos
        piso = edificio[i]
        for k,v in piso.items():    # --> recorre los departamentos
            if v == "Tucuman":
                print(v, "se encuentra en el piso", i, "departamento", k)

    # Acceso seguro a los datos
    # ¿Quíen vive en el 1e?
    # ¿Cómo podemos acceder a un valor que no existe
    # y que no explite el programa --> Utilizando "get":
    print(piso_1.get('e'))


def read_csv():
    # Abrir un archivo CSV
    csvfile = open('edificio.csv')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    edificio = list(csv.DictReader(csvfile))

    # Recorremos la lista de departamentos (diccionarios)
    # e imprimir en pantalla quienes viven en los departamentos a
    for piso in edificio:
        print(piso['a'])

    csvfile.close()

    # Abrir un archivo CSV con with open
    with open('propiedades.csv') as csvfile:
        # Leer todos los datos y almacenarlos en una 
        # lista de diccionarios
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

    mi_nombre = 'Max'
    mi_apellido = 'Power'

    writer.writeheader()
    fila = {'nombre': mi_nombre, 'apellido': mi_apellido}
    fila['nombre'] = mi_nombre
    writer.writerow(fila)
    writer.writerow({'apellido': 'School', 'nombre': 'Inove', 'numero': '12345678'})

    csvfile.close()


def agregar_datos():
    # El objetivo es abrir el archivo de edificio2.csv
    # y agregar más pisos al edificio, es decir, agregar más
    # filas a la planilla de cálculo

    # Este archivo ya tiene grabado el header (a, b, c) en
    # el archivo pero de todas formas debemos especificarlo
    header = ['a', 'b', 'c']

    # Este archivo ya tiene algunos pisos cargados, agregamos más
    # Abrir un archivo CSV con el flag "a"
    csvfile = open('edificio2.csv', 'a')

    # Generar un "escritor" para modificar el archivo
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Crear el nuevo piso
    nuevo_piso = {'a': 'San Luis', 'b': 'Corrientes', 'c': 'Salta'}

    # Escribirlo en el archivo
    writer.writerow(nuevo_piso)

    # Cerrar el archivo
    csvfile.close()


def modificar_datos():
    # Los archivos CSV no tiene una función para modificar
    # un valor ya ingresado, las operaciones que pueden
    # realizarse son las nombradas hasta ahora
    # --> leer el contenido (sin editar el archivo)
    # --> crear un archivo vacio y sumarle contenido
    # --> sumar contenido a un archivo existente (agregar)

    # Para poder modificar los datos es necesario realizar
    # el siguiente proceso
    # --> leer todo el archivo y almacenar los datos en una variable
    # --> cerrar el archivo (close)
    # --> crear un archivo nuevo con el flag 'w' con el mismo nombre
    # del archivo deseado, esto destruirá el archivo anterior
    # --> agregar

    # Abrir un archivo CSV
    csvfile = open('edificio2.csv')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    edificio = list(csv.DictReader(csvfile))

    # Modificar el departamento 'b' del segundo piso:
    edificio[1]['b'] = 'Neuquen'  # 2b

    # Cerrar el archivo
    csvfile.close()

    # Almacenar los cambios en edificio2.csv
    # Abrir archivo para escritura
    csvfile = open('edificio2.csv', 'w', newline='')

    # Detallar los nombres de las columnas
    header = ['a', 'b', 'c']

    # Generar un "escritor" para modificar el archivo
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Escribir los nombres de las columnas
    writer.writeheader()

    # Escribir todos los pisos/lineas juntas
    writer.writerows(edificio)

    # Cerrar el archivo
    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    diccionario()
    read_csv()
    write_csv()
    agregar_datos()
    modificar_datos()
