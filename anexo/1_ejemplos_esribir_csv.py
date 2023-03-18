# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def write_csv():
    # Abrir archivo para escritura
    csvfile = open('agenda.csv', 'w', newline='')

    # Detallar los nombres de las columnas
    header = ['nombre', 'apellido', 'numero']
    # Crear el objeto para escribir las lineas de archivo
    # basado en los nombres de las columnas
    writer = csv.DictWriter(csvfile, fieldnames=header)

    # Escribir el encabezado en el archivo (nombres columnas)
    writer.writeheader()
   
    nueva_fila = {'nombre': 'Max', 'apellido': 'Power'}
    writer.writerow(nueva_fila)

    nueva_fila = {'apellido': 'Escuela', 'nombre': 'Inove', 'numero': '12345678'}
    writer.writerow(nueva_fila)

    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    write_csv()
