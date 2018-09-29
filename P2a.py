#Inicio P2a, creacion de script para crear listas a partir de las columnas de la matriz del archivo firas_monopole_spec_v1.txt
import numpy as np

File="firas_monopole_spec_v1.txt"

Data= np.loadtxt(File)

Data = np.array(Data)

Frec = Data[:,0]
Spec = Data[:,1]
ResS = Data[:,2]
UncS = Data[:,3]
GalS = Data[:,4]