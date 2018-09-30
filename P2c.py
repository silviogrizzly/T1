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
