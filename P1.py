#Creando archivo para la pregunta 1
import math
import numpy as numpy
import matplotlib.pyplot as plt 

h=np.logspace(0,-15, 100, base=10)
dcosx1=(np.cos(1.191+h) - np.cos(1.191)) / h
a=(-1)*dcosx1

dcosx4=(-np.cos(1.191+2*h)+8*np.cos(1.191+h)-8*np.cos(1.191-h)+np.cos(1.191-2*h))/ (12*h)
b=(-1)*dcosx4

plt.clf()
plt.plot(h, a, color="g", label="Derivada Simple")
plt.plot(h, b, color="b", label="Derivada a 4to Orden de error")
plt.show()