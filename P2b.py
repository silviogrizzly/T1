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
tol=np.exp(-7)

P_an= (np.pi**(4))/15

def f(x):         #Funcion a integrar con el cambio de variable ya realizado
    n=(math.tan(x))**3
    d=(np.exp(math.tan(x))-1)*(math.cos(x)**2)
    y=n/d
    return y

#Metodo trapezoidal
    
Suma=0
Sumb=0

x=a
for i in range(1, N):
    Suma=Suma+f(x+i*h)
for i in range(2, N-1):
    Sumb=Sumb+f(x+i*h)

It=(h/2)*(Suma+Sumb)


#Metodo Simpson 1/3


Spar=0
Simpar=0

n=(N/2)-1
for i in range(1, n):
    Spar=Spar+f(x+(2*i)*h)
for i in range(0, n):
    Simpar=Simpar+f(x+(2*i+1)*h)

Isu=(h/3)*(4*Simpar+2*Spar)
    
#Metodo de Simpson 3/8

Su=0
Sd=0

for i in range(0, m-1):
    Su=Su+f(x+(3*i+1)*h)+f((3*i+2)*h)
for i in range(1, m-1):
    Sd=Sd+f(x+3*i*h)
    
Ist=(3*h/8)*(3*Su+2*Sd)


#Tolerancia de error en metodos de integracion
tol=np.exp(-9)

if abs(P_an-It)<tol:
    print "It=", It
if abs(P_an-Isu)<tol:
    print "Isu=", Isu
if abs(P_an-Ist)<tol:
    print "Ist=", Ist
print tol
print P_an

#Metodo elegido: Metodo trapezoidal ya que con menor numero de particiones, se consigue mayor exactitud