# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


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

    # Obtener todos los datos de la fila 0
    row = data[0]
    print('Datos Fila 0:', row)
    print('Fila 0, dato latitud:', row['latitud'])

    # Obtener de la fila 0 la latitud
    latitud = data[0]['latitud']
    print('Latitud:', latitud)

    # Obtener la cantidad de filas del archivo
    # y recorrerlo    
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        # Cuando llegue a la fila 5 se detendrá el bucle
        # para no hacer muy largo el ejemplo
        if i == 5:
            break

        # Leer fila
        row = data[i]
        try:
            latitud = float(row['latitud'])
            print('Fila', i, 'dato latitud:', latitud)
        except:
            print('Error Fila', i, 'dato latitud faltante')


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
    read_csv()
    write_csv()
