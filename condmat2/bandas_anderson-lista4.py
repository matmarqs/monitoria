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

t = +5
V = 0
L = 7
a = 1

def Ek(n, k):
    pm = (-1)**n
    s = L - 2*t*np.cos(k*a)
    return (s + pm*np.sqrt(s**2 + 4*V**2)) / 2


def main():
    kmin = -np.pi/a; kmax = np.pi/a
    ks = np.linspace(kmin, kmax, 400)
    plt.plot(ks, Ek(2, ks), label=r'$E_+(k)$')
    plt.plot(ks, Ek(1, ks), label=r'$E_-(k)$')
    plt.xlabel(r'$k$', fontsize=20)
    plt.ylabel(r'$E(k)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'bandas $E_\pm(k)$: $t = %.0f, \lambda = %.0f, V = %.0f, a = %.0f$' % (t, L, V, a))
    plt.savefig("bandas-anderson.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
