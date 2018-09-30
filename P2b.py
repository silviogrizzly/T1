#Metodos de Integracion

from astropy import constants as const
import numpy as np
import matplotlib.pyplot as plt
import math

m=30
N=3*m
a=0
b=np.pi/2
h=(np.pi/(2*(N)))

P_an= (np.pi**(4))/15

def f(x):         #Funcion a integrar con el cambio de variable ya realizado
    n=(math.tan(x))**3
    d=(np.exp(math.tan(x))-1)*(math.cos(x)**2)
    y=n/d
    return y