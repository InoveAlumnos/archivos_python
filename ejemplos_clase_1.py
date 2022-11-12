# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


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

    # Armemos ahora el edificio de 2 pisos, 
    # el cual es una lista de diccionarios
    edificio = []
    edificio.append(piso_1)
    edificio.append(piso_2)

    # Imprimir las familias que viven
    # en cada departamento "a"
    for i in range(len(edificio)):
        print(f"Piso {i+1} depto a:", edificio[i]["a"])


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


def operador_in():
    # El operador "in" (en) devuelve True si
    # un elemento se encuentra dentro de otro

    # En diccionarios nos indica si existe
    # una clave (key) definido en su interior

    # En este diccionario almacenaremos
    # cuantos productos hay en stock
    stock_productos = {"monitor": 6, "teclado": 3, "mouse": 54}

    if "monitor" in stock_productos:
        print("En mi stock hay monitores")

    if "bicicleta" in stock_productos:
        print("En mi stock hay bicicletas")

    if "bicicleta" not in stock_productos:
        print("En mi stock NO hay bicicletas")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    diccionario()
    operador_in()
