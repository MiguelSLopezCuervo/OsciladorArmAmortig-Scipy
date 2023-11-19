# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:40:42 2023

@author: Miguel Sánchez

Solución numérica usando la librería scipy de un oscilador armónico amortiguado.

Cambiar el Epsilon para ver distintos comportamientos (subamortiguado y sobream)

Se representa el espacio fase. Ecuación Diferencial Ordinaria desacoplada
en sistema de dos EDO de 1er orden
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

t_final = 100
Epsilon = 0.05
def Dumping(t, z):
    x, y = z
    dxdt = y
    dydt = -x - 2*Epsilon*y
    return [dxdt, dydt]

# (fun, t_span, y0, method='RK45', t_eval=None, dense_output=False, 
#  events=None, vectorized=False, args=None, **options)
solution = solve_ivp(Dumping, [0, t_final], [0., 1.], dense_output=True)

t = np.linspace(0, t_final, 500)
z = solution.sol(t)

plt.plot(z[0], z[1])
plt.xlabel('x(t)')
plt.ylabel('y(t)=$\dot{x}(t)$')
plt.title('Phase portrait')
plt.show()
