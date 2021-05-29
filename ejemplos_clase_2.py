# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

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
    print('Fila 0, dato latitud:', row.get('latitud'))

    latitud = data[0].get('latitud')
    print('Latitud:', latitud)

    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        if i == 5:
            break
        row = data[i]
        try:
            latitud = float(row.get('latitud'))
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

    mi_nombre = 'Max'
    mi_apellido = 'Power'

    writer.writeheader()
    fila = {'nombre': mi_nombre, 'apellido': mi_apellido}
    fila['nombre'] = mi_nombre
    writer.writerow(fila)
    writer.writerow({'apellido': 'School', 'nombre': 'Inove', 'numero': '12345678'})

    csvfile.close()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    read_csv()
    write_csv()
