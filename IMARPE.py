#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:23:50 2022

@author: ronald
"""

import math 
import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd


# Capacidad de carga
K=700

# Tasa de crecimiento poblacional
r=1.8


# Datos de capturas en cada tiempo
# Solo como prueba se considera el siguiente vector con datos
C=[ 2, 5, 18 , 29, 32]


N = np.zeros(shape=len(C))

# Población inicial
N[0]=357

for i in range(0,len(C)-1):
    N[i+1]=N[i]+r*N[i]*(1-N[i]/K)-C[i]
    i=i+1
    
print(N)

plt.plot(C, N)
plt.show()


#Exportamos a un excel para el tratamiento de los datos
df = pd.DataFrame([C,N])
df.to_excel('data.xlsx')