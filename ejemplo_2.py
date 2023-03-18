# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def sumar_stock():
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
    # Acumular el stock de arandelas
    cantidad_total_arandelas = 0
    for i in range(len(stock)):
        # ¡Ojo! Todos los datos de un CSV son texto
        # Hay que pasarlos a números (int o float)
        # si realizaremos operaciones matemáticas como la suma
        cantidad_arandelas = int(stock[i]["arandelas"])
        cantidad_total_arandelas += cantidad_arandelas

    # Imprimir cantidad total de arandelas
    print("Cantidad total de arandelas:", cantidad_total_arandelas)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    sumar_stock()
