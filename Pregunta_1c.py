# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 03:23:53 2021

@author: luish_000
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('heart.csv', index_col=())
dataset.info()

# Frecuencia de edades
plt.hist(dataset['age'], 15, color='yellow', ec = 'black')


# Cantidad de personaas que padecen alguna enfermedad cardiaca
# 1: Si padece una enfermedad
# 0: No padece ninguna enfermedad
sns.countplot(dataset['target'], palette = 'ocean')

# Clasificacion de Dolor en el Pecho de los pacientes segun su genero
#Patient sex
    #Value 0: female
    #Value 1: male

grafico = sns.countplot(x = 'sex', hue = 'cp', palette='hot_r', data=dataset)
grafico.set(title = 'Dolores a la altura del pecho por género', xlabel = 'Genero', ylabel='Dolor en el pecho')
plt.show()

#Chest pain type
    #Value 0: asymptomatic
    #Value 1: atypical angina
    #Value 2: pain without relation to angina
    #Value 3: typical angina
