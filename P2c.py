import numpy as np
import matplotlib.pyplot as plt
import math
from astropy import constants as const


File="firas_monopole_spec_v1.txt"

Data= np.loadtxt(File)

Data = np.array(Data)

Frec = Data[:,0]
Spec = Data[:,1]
ResS = Data[:,2]
UncS = Data[:,3]
GalS = Data[:,4]

#Como la discretizacion no es uniforme, se toma cada contribucion con su propio h para calculr la integral

N=43


def h(k):
    y=Frec[k+1]-Frec[k]
    return y
def f(k):
    z=Spec[k]
    return z


Suma=0
Sumi=0
for i in range(0, N-1):
    Sumi=Sumi+(h(i)/2)*(f(i)+f(i+1))
    
for i in range(1, N-1):
    if i%2!=0:
        Suma=Suma+(h(i)/3)*(f(i-1)+4*f(i)+f(i+1))
    
print Suma
print Sumi    
    
It= 6.493936937055461

T =1
P=((2*const.h)/(const.c)**2)*(((const.k_B*T)/const.h)**4)*It
print P