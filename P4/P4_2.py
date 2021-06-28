from labfis.uncertainty import labfloat
import numpy as np
from labfis import labfloat as lf

massa = lf(72.72, 0.01)
m2 = massa/1000
alpha = lf(46, 1)
gama = lf(58, 1)
g = 9.81

t1 = (m2* g * np.sin(gama*np.pi/180))/np.sin((alpha+gama)*np.pi/180)
t3 = (m2* g * np.sin(alpha*np.pi/180))/np.sin((alpha+gama)*np.pi/180)

m1 = t1/g
m3 = t3/g

massa_e = lf(62.89,0.01) 
m1_e= lf(62.89,0.01)/1000


print (f'O valor obtido experimentalmente M1= {m1}')
print (f'O valor teorico de M1 = {m1_e}')
print (f'M1 experimental é igual ao M1 teórico? : {m1==m1_e}')