#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
## comentar as 4 linhas abaixo caso nao tenha o LaTeX no matplotlib ###
from matplotlib import rc
plt.style.use('bmh')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{physics}')
#matplotlib.verbose.level = 'debug-annoying'
#######################################################################

from scipy.integrate import quad
from scipy.optimize import brentq as root

debye = 10
N = 1
kB = 1
g0 = 1

def phi(d, T):
    quad_res = quad(lambda e: np.tanh(1/(2*T) * np.sqrt(e**2+d**2))/np.sqrt(e**2+d**2), 0, debye)
    return 1 - g0 * N * quad_res[0]

def main():
    Temps = []
    #Temps = np.logspace(-5, -0.37, 100)
    Delts = []
    T = 1e-6
    dx = 0.0001 * debye
    Delta = 1
    Delta0 = root(phi, -0.01, 2*debye, args=(T))
    while True:
        Delta = root(phi, -0.01, 2*debye, args=(T))
        if Delta < 0.2:
            break
        T += dx
        Temps.append(T)
        Delts.append(Delta)
        print('T =', T)
        print('Delta =', Delta)

    TempsLess = Temps[:]
    Tc = T
    Temps.append(Tc)
    Delts.append(0)
    for i in range(50):
        T += 0.01
        Temps.append(T)
        Delts.append(0)


    print('Tc =', Tc)
    print('razao =', Delta0 / Tc)
    plt.plot(Temps, Delts, label=r'$\Delta(T)$')
    plt.plot(TempsLess, 1.74 * Delta0 * np.sqrt(1 - np.array(TempsLess)/Tc), label=r'$1.74 \cdot \Delta_0 \, (1 - T/T_c)^{1/2}$')
    plt.xlabel(r'$T$', fontsize=20)
    plt.ylabel(r'$\Delta$', fontsize=20)
    plt.legend(fontsize=16)
    plt.title(r'Cálculo numérico do gap')
    plt.savefig("num_gap.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

if __name__ == '__main__':
    main()
