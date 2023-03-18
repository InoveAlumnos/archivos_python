# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def open_csv():
    # Abrir un archivo CSV
    csvfile = open('stock.csv')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    stock = list(csv.DictReader(csvfile))

    # Una vez leido los datos, cerrar el archivo
    csvfile.close()

    # Imprimir todos los datos juntos
    print(stock)

    # Recorremos las filas del archivo
    # e imprimir en pantalla el stock de cada material (diccionario)
    # Creamos un bucle que va de 0 a la cantidad de
    # filas del archivo --> len(stock)
    for i in range(len(stock)):
        print("Fila", i)
        print(stock[i])

    # Acceder a la fila 2, columna tornillos
    print(stock[2]["tornillos"])


def with_open_csv():
    # Abrir un archivo CSV con with open
    with open('stock.csv') as csvfile:
        # Leer todos los datos y almacenarlos en una 
        # lista de diccionarios
        stock = list(csv.DictReader(csvfile))

    # No es necesario cerrar el archivo
    # "with open" ya hizo ese trabajo

    # Imprimir todos los datos juntos
    print(stock)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    open_csv()
    with_open_csv()
