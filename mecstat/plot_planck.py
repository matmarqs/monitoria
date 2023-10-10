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

h = 1
c = 1
kB = 1

def u(L, T):
    beta = 1/(kB * T)
    return 8*np.pi*h*c/L**5 * 1/(np.exp(beta*h*c/L)-1)


def main():
    Lmin = 0.001; Lmax = 0.4
    Ls = np.linspace(Lmin, Lmax, 1000)
    plt.plot(Ls, u(Ls, 4), label=r'$T = 4$')
    plt.plot(Ls, u(Ls, 5), label=r'$T = 5$')
    plt.plot(Ls, u(Ls, 6), label=r'$T = 6$')
    plt.plot(Ls, u(Ls, 7), label=r'$T = 7$')
    plt.xlabel(r'$\lambda$', fontsize=20)
    plt.ylabel(r'$u(\lambda)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'$u(\lambda) \times \lambda$')
    plt.savefig("planck-lambda.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
