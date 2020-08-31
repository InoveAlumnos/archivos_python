#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pablo Ruiz Diaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.2"

import csv
import tiempos

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''

    with open('texto.txt', 'r') as texto:
        lineas = texto.readlines()

        for i in range(len(lineas)):
            cantidad_letras += len(lineas[i])
        
        print(cantidad_letras)


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''

    with open('texto2.txt', 'w') as texto2:
        while True:
            linea = str(input('Ingrese texto: '))

            if linea == '':
                break
            
            texto2.write(linea)
            texto2.write('\n')

            cantidad_letras += len(linea)
    
    print(cantidad_letras)


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''

    ARS = 0
    ARS_cant = 0
    ARS_min = None
    ARS_max = None
    USD = 0
    USD_cant = 0
    USD_min = None
    USD_max = None
    no_moneda = 0

    tipo_inmueble = list()
    cantidad_ambientes = list()

    with open('propiedades.csv', 'r', newline='') as propiedades:
        inmueble = list(csv.DictReader(propiedades))
        
        for row in inmueble:
            tipo = row.get('tipo_propiedad')
            if tipo in tipo_inmueble:
                continue
            else:
                tipo_inmueble.append(tipo)
        
        print('Ingrese el numero de inmueble que quiere revisar:')
        for i in range(len(tipo_inmueble)):
            print('\t', i, '->', tipo_inmueble[i])
        
        inmueble_buscado = int(input('Inmueble: '))

        for row in inmueble:
            ambientes = row.get('ambientes')
            if tipo_inmueble[inmueble_buscado] == row.get('tipo_propiedad'):
                if ambientes in cantidad_ambientes:
                    continue
                else:
                    if ambientes == '':
                        continue

                    cantidad_ambientes.append(ambientes)
            else:
                continue

        if cantidad_ambientes == []:
            print('Sin informacion de ambientes')
        else:
            cantidad_ambientes.sort()
            
            print('Ingrese el numero posicion de cantidad de ambientes que quiere revisar:')
            
            for i in range(len(cantidad_ambientes)):
                print('\t', i, '->', cantidad_ambientes[i])

        ambientes_buscado = int(input('Cantidad de ambientes: '))

        print('El siguiente listado es la informacion de acuerdo a las condiciones ingresadas')

        for moneda in inmueble:
            moneda_ = moneda.get('moneda')

            if moneda_ == 'ARS':
                ARS += 1
            elif moneda_ == 'USD':
                USD += 1
            else:
                no_moneda += 1
        
        print('Su inmueble tiene una cantidad de {} en AR$, {} en U$D y {} no definido' .format(ARS, USD, no_moneda))

        for moneda in inmueble:
            if moneda.get('moneda') == 'ARS':
                ARS += int(moneda.get('precio'))
                ARS_cant += 1
                
                if (ARS_min == None or ARS_min > int(moneda.get('precio'))):
                    ARS_min = int(moneda.get('precio'))
                
                if (ARS_max == None or ARS_max < int(moneda.get('precio'))):
                    ARS_max = int(moneda.get('precio'))
            elif moneda.get('moneda') == 'USD':
                USD += int(moneda.get('precio'))
                USD_cant += 1
                if (USD_min == None or USD_min > int(moneda.get('precio'))):
                    USD_min = int(moneda.get('precio'))
                
                if (USD_max == None or USD_max < int(moneda.get('precio'))):
                    USD_max = int(moneda.get('precio'))
        
        print('Promedio de precios:\n\tAR$ {}\n\tU$D {}' .format(ARS/ARS_cant, USD/USD_cant))
        print('El precio minimo y maximos son:\n\tAR$ -> Minimo {}\tMaximo {}\n\tU$D -> Minimo {}\tMaximo {}' .format(ARS_min, ARS_max, USD_min, USD_max))


def ejercicio_extra():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.
    '''

    tipo_division = []
    tiempo_swim = []
    tiempo_run = []
    tiempo_bike = []

    with open('2019 Ironman World Championship Results.csv', 'r') as ironman:
        iron_man = list(csv.DictReader(ironman))

        for row in iron_man:
            division = row.get('Division')
            if division in tipo_division:
                continue
            else:
                tipo_division.append(division)
        
        print('Ingrese posicion de division atletica deseada:')
        for i in range(len(tipo_division)):
            print('\t', i, '->', tipo_division[i])
        
        division_buscada = int(input('Division: '))

        print('Escriba que categorgia quiere analizar\n\tSwim\n\tBike\n\tRun')
        categoria = str(input('-> '))

        for row in iron_man:
            tiempo_swim.append(row.get('Swim'))
            tiempo_run.append(row.get('Run'))
            tiempo_bike.append(row.get('Bike'))
        
        if categoria == 'Swim':
            maximo_ = tiempos.maximo(tiempo_swim)
            minimo_ = tiempos.minimo(tiempo_swim)
            promedio_ = tiempos.promedio(tiempo_swim)
        elif categoria == 'Run':
            maximo_ = tiempos.maximo(tiempo_run)
            minimo_ = tiempos.minimo(tiempo_run)
            promedio_ = tiempos.promedio(tiempo_run)
        elif categoria == 'Bike':
            maximo_ = tiempos.maximo(tiempo_bike)
            minimo_ = tiempos.minimo(tiempo_bike)
            promedio_ = tiempos.promedio(tiempo_bike)
        else:
            print('Error en la categoria seleccionada')
            
        print('Promedio de {} es: {}' .format(categoria, promedio_))
        print('Los tiempos minimo y maximo son:\n\t-> Minimo {}\tMaximo {}' .format(minimo_, maximo_))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ejercicio_extra()
