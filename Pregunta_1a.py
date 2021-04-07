# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:57:40 2021

@author: luish_000
"""

import numpy as np
import pandas as pd
from math import sqrt

def media (lista):          #Funcion para la calcular la MEDIA
    suma = 0
    for valor in lista:
        suma += valor
    
    return suma / len(lista)

def mediana (lista):        #Función para crear la MEDIANA
    lista.sort()
    if len(lista) % 2 != 0:
        middle = int ((len(lista) - 1) / 2)
        return lista[middle]
    elif len (lista) % 2 == 0:
        middle_1 = int(len(lista) / 2)
        middle_2 = int(len(lista) / 2) - 1
        return media([lista[middle_1], lista[middle_2]])

def desviacion_estandar (lista, valor_media):   #Función para crear la 
    suma = 0                                    #DESVIACION ESTANDAR
    
    for valor in lista:
        suma += (valor - valor_media) ** 2
    
    fraccion = suma / (len(lista) - 1)
    
    return sqrt(fraccion)

dataset = pd.read_csv("heart.csv")  #Leemos el dataset Heart.csv

x1 = dataset["age"].tolist()        #Lista de Edad del paciente
x2 = dataset["sex"].tolist()        #Lista de Sexo al que corresponde el paciente
x3 = dataset["trestbps"].tolist()   #Lista de Presion Arterial (mm Hg)
x4 = dataset["chol"].tolist()       #Lista de nivel de Colesterol (mg/dl)
x5 = dataset["thalach"].tolist()    #Lista de Frecuencia Cardiaca
x6 = dataset["oldpeak"].tolist()    #Lista de disminución del segmento ST

print("-----DATOS ESTADÍSTICOS-----")
print('COLUMNA EDAD')
print("\tMedia:               ", media(x1))
print("\tMediana:             " , mediana(x1))
print("\tDesviación Estandar: ", desviacion_estandar(x1, media(x1)))
print("**********************************************************************")
print()
print('COLUMNA SEXO')
print("\tMedia:               ", media(x2))
print("\tMediana:             " , mediana(x2))
print("\tDesviación Estandar: ", desviacion_estandar(x2, media(x2)))
print("**********************************************************************")
print()
print('COLUMNA PRESION ARTERIAL')
print("\tMedia:               ", media(x3))
print("\tMediana:             " , mediana(x3))
print("\tDesviación Estandar: ", desviacion_estandar(x3, media(x3)))
print("**********************************************************************")
print()
print('COLUMNA NIVEL DE COLESTEROL')
print("\tMedia:               ", media(x4))
print("\tMediana:             " , mediana(x4))
print("\tDesviación Estandar: ", desviacion_estandar(x4, media(x4)))
print("**********************************************************************")
print()
print('COLUMNA FRECUENCIA CARDIACA')
print("\tMedia:               ", media(x5))
print("\tMediana:             " , mediana(x5))
print("\tDesviación Estandar: ", desviacion_estandar(x5, media(x5)))
print("**********************************************************************")
print('COLUMNA DISMINUCION SEGMENTO ST')
print("\tMedia:               ", media(x6))
print("\tMediana:             " , mediana(x6))
print("\tDesviación Estandar: ", desviacion_estandar(x6, media(x6)))
print("**********************************************************************")





