import numpy as np
import matplotlib.pyplot as plt
from labfis import labfloat as lf
import statsmodels.api as sm

dados = np.loadtxt("P5\TabelaP5.txt")

L = (np.array([lf(N[0],N[1]) for N in dados]))
M = (np.array([lf(N[2],N[3]) for N in dados]))
P = (M*9.81)

y = P.astype(np.float64)
x = sm.add_constant(L.astype(np.float64))

modelo = sm.OLS (y, x)
resultado = modelo.fit ()
#print (resultado.summary())

c_lin, c_ang = resultado.params
inc_c_lin, inc_c_ang = resultado.bse
reta = c_ang * x + c_lin

x = x[:,1] 
reta = reta[:,1]

k= lf(c_ang, inc_c_ang)
L0 = lf(abs(c_lin), inc_c_lin)/k

print (f'K= {k}')
print (f'L0= {L0}')

L0_Medida = lf(29.7, 0.1)/100

print (f'L0 real = {L0_Medida}')
print (f'equivalentes ? = {L0==L0_Medida}')

plt.scatter (x, y, label = 'P(L)', color = 'Black')
plt.plot (x, reta, label = 'P = KL - KL0', color = 'Red')
plt.xlabel('L (m)')
plt.ylabel('P (N)')
plt.legend()
plt.show()
