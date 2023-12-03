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

J = 1
a = 1

def wk(k, g):
    return 2*J*np.sqrt(1 + g**2 - 2*g*np.cos(k*a)) / (2*J)

def main():
    kmin = -np.pi/a; kmax = np.pi/a
    ks = np.linspace(kmin, kmax, 400)
    plt.plot(ks, wk(ks, 0.20), label=r'$g = 0.20$')
    plt.plot(ks, wk(ks, 0.50), label=r'$g = 0.50$')
    plt.plot(ks, wk(ks, 1.00), label=r'$g = 1.00$')
    plt.plot(ks, wk(ks, 1.25), label=r'$g = 1.25$')
    plt.plot(ks, wk(ks, 1.50), label=r'$g = 1.50$')
    plt.xlabel(r'$ka$', fontsize=20)
    plt.ylabel(r'$E_k / 2J$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'Dispersão Ising campo transverso')
    plt.savefig("transv_ising.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
