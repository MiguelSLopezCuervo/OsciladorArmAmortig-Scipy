# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:24:43 2023

@author: Miguel Sánchez

Comparación de la solución exacta del Osc Arm Amortiguado y su aproximación 
por el método de las perturbaciones de primer orden
"""

import numpy as np
import matplotlib.pyplot as plt

Epsilon = 0.05

def Exacto(t):
    res = 1/(1-Epsilon**2) * np.exp(-Epsilon * t) * np.sin( np.sqrt( 1- Epsilon**2)*t)
    return res

def Perturb(t):
    res = np.sin(t) - Epsilon*t*np.sin(t)
    return res

x       = np.linspace(0, 20, 200)
y_ex    = Exacto(x)
y_pert  = Perturb(x)

plt.plot(x, y_ex, label='Exacto')
plt.plot(x, y_pert, label='Perturbado')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Valor Epsilon = ' + str(Epsilon))
plt.legend()

plt.show()


"""
COMENTARIO:
    
    PUES QUE SE PARECEN MUCHO Y TAL, QUE BAJANDO EL EPSILON SE PARECEN MÁS
    Y QUE CONFORME t CRECE LA DIFERENCIA SE HACE MAYOR COMO ES LÓGICO PORQ
    NOS VAMOS ALEJANDO DEL PUNTO EN EL QUE SE HA HECHO LA APROX QUE ES
    t=0

    QUE SE VE MUY BIEN COMO EL EXACTO ES AMORTIGUADO, EL PERTURBADO DECRECE
    PERO LUEGO CRECE ASÍ QUE NO SIRVE PARA NADA COMO APROXIMACIÓN PARA t 
    GRANDES

"""