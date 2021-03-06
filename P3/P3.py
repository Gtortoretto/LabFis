import numpy as np
import matplotlib.pyplot as plt
from labfis import labfloat as lf
import statsmodels.api as sm

# L = Comprimento do pêndulo
# ΔL = Incerteza de L
# t_10 = Tempo para 10 oscilações
# Δt_10 = incerteza de t_10 
# T = Período do pêndulo
# ΔT = Incerteza de T
# T2 = Período do pêndulo ao quadrado
# ΔT2 = Incerteza de T2
# g = Aceleração gravitacional terrestre
# Δg = Incerteza de g
# No arquivo Tablela1.txt colocamos os dados para os experimentos na seguinte configuração: Uma coluna com dados, logo sua incerteza separados por um /T (tab)


dados = np.loadtxt('Tabela1.txt')

L = (np.array([lf(N[0],N[1]) for N in dados])/100)
t_10 = (np.array([lf(N[2],N[3]) for N in dados]))
T = t_10 / 10
T2 = T ** 2 
print (L)

Y = T2.astype(np.float64)
X = sm.add_constant(L.astype(np.float64))

modelo = sm.OLS(Y, X)
resultado = modelo.fit()
print (resultado.summary())

coef_lin, coef_ang = resultado.params
inc_coef_lin, inc_coef_ang = resultado.bse
reta = coef_ang * X + coef_lin

X = X[:,1] 
reta = reta[:,1]

plt.scatter(X, Y, label='T²(L)')
plt.plot(X, reta, label='Regressão linear', color='Red')
plt.xlabel('L')
plt.ylabel('T²')
plt.legend()
plt.show()

g = 4 *(np.pi**2)/lf(coef_ang, inc_coef_ang)
print (f'O valor da aceleração gravitacional é de: {g}')

