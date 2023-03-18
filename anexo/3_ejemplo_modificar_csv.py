# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

import csv


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
    modificar_datos()
