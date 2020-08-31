#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''

    with open('notas.txt', 'r') as fi:
        for line in fi:
            cantidad_lineas += 1
    
    print(cantidad_lineas)


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    fi = open('notas.txt', 'r')
    fo = open('notas_copy.txt', 'w')

    for line in fi.readlines():
        fo.write(line)
    
    # Recuerde cerrar los archivos al final ;)
    fi.close()
    fo.close()
    

def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''

    cant_dpto_2amb = 0
    cant_dpto_3amb = 0

    with open('propiedades.csv', 'r') as fi:
        data = list(csv.DictReader(fi))
    
    for i in range(len(data)):
        ambientes = data[i]
        if ambientes.get('ambientes') == '2':
            cant_dpto_2amb += 1
        if ambientes.get('ambientes') == '3':
            cant_dpto_3amb += 1
    
    print('Cantidad de Departamentos\n > con 2 ambientes {}\n > con 3 ambientes {}' .format(cant_dpto_2amb, cant_dpto_3amb))
    

def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    fruta = {}
    
    while True:
        fruta_nueva = str(input('Ingresar nueva fruta ("Fin" para finalizar): '))
        
        if fruta_nueva == 'Fin':
            break
        
        if fruta_nueva in inventario:
            fruta_existente = str(input('Esta fruta ya se encuentra en el inventario. Desea cambiar la cantidad total? Y/N\n'))
            
            if fruta_existente == 'Y':
                cant_fruta_nueva = int(input('Cantidad total de {}: ' .format(fruta_nueva)))
                
                inventario.pop(str(fruta_nueva))
                
                fruta = {str(fruta_nueva): str(cant_fruta_nueva)}
                
                inventario.update(fruta)
            else:
                continue

            continue

        cant_fruta_nueva = int(input('Cantidad de {}: ' .format(fruta_nueva)))

        fruta = {str(fruta_nueva): str(cant_fruta_nueva)}

        inventario.update(fruta)
    
    print('Fruta > Cantidad')
   
    for i, j in inventario.items():
        print(i, ' > ', j)


def ej5():
    # Ejercicios con archivos CSV
    inventario = {}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    with open('csv_verduleria.csv', 'w', newline='') as inventario_verduleria:
        header = ['Fruta Verdura', 'Cantidad']
        writer = csv.DictWriter(inventario_verduleria, fieldnames=header)
        writer.writeheader()
        
        while True:
            fruta_nueva = str(input('Ingresar nueva fruta ("Fin" para finalizar): '))
        
            if fruta_nueva == 'Fin':
                break
            
            cant_fruta_nueva = int(input('Cantidad de {}: ' .format(fruta_nueva)))

            fruta = {'Fruta Verdura': str(fruta_nueva), 'Cantidad': str(cant_fruta_nueva)}

            writer.writerow(fruta)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
