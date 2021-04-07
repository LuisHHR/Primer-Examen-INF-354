# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 02:55:11 2021

@author: luish_000
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv("heart.csv")  #Leemos el dataset Heart.csv

x1 = np.asarray(dataset["age"])         #Lista de Edad del paciente
x2 = np.asarray(dataset["sex"])         #Lista de Sexo al que corresponde el paciente
x3 = np.asarray(dataset["trestbps"])    #Lista de Presion Arterial (mm Hg)
x4 = np.asarray(dataset["chol"])        #Lista de nivel de Colesterol (mg/dl)
x5 = np.asarray(dataset["thalach"])     #Lista de Frecuencia Cardiaca
x6 = np.asarray(dataset["oldpeak"])     #Lista de disminución del segmento ST

print("-----DATOS ESTADÍSTICOS-----")
print('COLUMNA EDAD')
print("\tMedia:               ", np.mean(x1))
print("\tMediana:             ", np.median(x1))
print("\tDesviación Estandar: ", np.std(x1))
print("**********************************************************************")
print()
print('COLUMNA SEXO')
print("\tMedia:               ", np.mean(x2))
print("\tMediana:             ", np.median(x2))
print("\tDesviación Estandar: ", np.std(x2))
print("**********************************************************************")
print()
print('COLUMNA PRESION ARTERIAL')
print("\tMedia:               ", np.mean(x3))
print("\tMediana:             ", np.median(x3))
print("\tDesviación Estandar: ", np.std(x3))
print("**********************************************************************")
print()
print('COLUMNA NIVEL DE COLESTEROL')
print("\tMedia:               ", np.mean(x4))
print("\tMediana:             ", np.median(x4))
print("\tDesviación Estandar: ", np.std(x4))
print("**********************************************************************")
print()
print('COLUMNA FRECUENCIA CARDIACA')
print("\tMedia:               ", np.mean(x5))
print("\tMediana:             ", np.median(x5))
print("\tDesviación Estandar: ", np.std(x5))
print("**********************************************************************")
print()
print('COLUMNA DISMINUCION SEGMENTO ST')
print("\tMedia:               ", np.mean(x6))
print("\tMediana:             ", np.median(x6))
print("\tDesviación Estandar: ", np.std(x6))
print("**********************************************************************")
print()
