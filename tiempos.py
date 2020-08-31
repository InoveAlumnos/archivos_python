'''
Las siguientes funciones retornan los tiempos minimo, maximo y promedio
pertienente con datos string de formato hh:mm:ss 

Funciones y parametros:
    maximo(tiempo_run)
    minimo(tiempo_run)
    promedio(tiempo_run)
'''

import time
from datetime import datetime

def seg(tiempo):
    tiempo_segundos = []
    
    for i in tiempo:
        if i == '':
            continue
        
        format_segundos = datetime.strptime(i, '%H:%M:%S')
        segundos = format_segundos.hour * 3600 + format_segundos.minute * 60 + format_segundos.second
        tiempo_segundos.append(segundos)
    return tiempo_segundos

def maximo(tiempo):
    max_ = seg(tiempo)
    return max(max_)

def minimo(tiempo):
    min_ = seg(tiempo)
    return min(min_)

def promedio(tiempo):
    sum_promedio = 0
    
    promedio_ = seg(tiempo)
    
    for i in promedio_:
        sum_promedio += i
    return sum_promedio/len(promedio_)