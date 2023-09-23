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
#from scipy.integrate import simpson

#m, L, A, V = 1, 1, 1, 1
#r1 = lambda x: (2*m*L) / np.pi * 1 / (np.sqrt(2*m*x))
#r2 = lambda x: m*A / np.pi + 0*x
#r3 = lambda x: m*V / np.pi**2 * np.sqrt(2*m*x)

hbar = 1
w = 1
kB = 1

def CV_N(T):
    return (hbar*w)**2/(4*kB*T**2) * 1/np.sinh(hbar*w/(2*kB*T))**2


def main():
    Tmin = 0.01; Tmax = 5
    Ts = np.linspace(Tmin, Tmax, 400)
    plt.plot(Ts, CV_N(Ts), label=r'$\frac{C_V}{N}$')
    plt.xlabel(r'$T$', fontsize=20)
    plt.ylabel(r'$\frac{C_V}{N}$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'Calor específico para o conjunto de $N$ osciladores quânticos')
    plt.savefig("cv_quant-osc.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
