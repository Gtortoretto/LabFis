import numpy as np
from labfis import labfloat as lf
import statsmodels.api as sm

g = 9.81
alpha, gamma = np.array(input("Ângulos α° e γ° : ").split( )).astype(np.float64)
if alpha + gamma > 180 :
    print ('Valores incorretos de α e γ')
    exit()
beta = 180 - alpha - gamma

input_massa2 = np.array(input("Massa de M2 e sua incerteaza Δm2 :").split()).astype(np.float64)
m2 = lf(input_massa2[0], input_massa2[1])
p2 = m2 * g

T_ab = np.sin(alpha) * p2 / np.sin(beta)    
T_ac = np.sin(gamma) * p2 / np.sin(beta)

m1 = T_ac / g
m3 = T_ab / g

print (f'Os valores das tensões são: Tab= {T_ab} e Tac= {T_ac} ')
print (f'Os valores das massas são: massa1= {m1} , massa 2= {m2} e massa 3= {m3}')

massas = np.array(list(input("Massas M1, M2 e M3 em g medidos diretamente (utilizando a balança): ").split( ))).astype(np.float64)
Δm_2 = float(input("Incerteza Δm das massas (incerteza da balança) :"))
if Δm_2 != 0.01 :
    print ('A incerteza das massas é 0.01 eu acho ...')
    exit()
m1_2 = lf((massas[0]),Δm_2)
m2_2 = lf((massas[1]),Δm_2)
m3_2 = lf((massas[2]),Δm_2)
# m1, m2, m3 = np.array(lf((massas[a] for a in massas),Δm_2))

if abs(m1 - m1_2) < 2 * (input_massa2 + Δm_2):
    print (f'As massas obtidas experimentalmente do corpo 1 são equivalentes as esperadas, portanto, {m1} = {m1_2}')
else : print (f'As massas obtidas experimentalmente do corpo 1 não são equivalentes as esperadas, portanto, {m1} != {m1_2}')










