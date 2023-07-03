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

def n(mu, U, T):
    b = 1/T
    return 2*(np.exp(b*mu)+np.exp(b*(2*mu-U))) / (1+2*np.exp(b*mu)+np.exp(b*(2*mu-U)))


def main():
    mu = np.linspace(-0.3, 3, 300)
    plt.plot(mu, n(mu, 0.5, 0.01), label=r'$U = 0.5$, $T = 0.01$')
    plt.plot(mu, n(mu, 0.5, 0.05), label=r'$U = 0.5$, $T = 0.05$')
    plt.plot(mu, n(mu, 1.0, 0.01), label=r'$U = 1.0$, $T = 0.01$')
    plt.plot(mu, n(mu, 1.0, 0.05), label=r'$U = 1.0$, $T = 0.05$')
    plt.plot(mu, n(mu, 2.0, 0.01), label=r'$U = 2.0$, $T = 0.01$')
    plt.plot(mu, n(mu, 2.0, 0.05), label=r'$U = 2.0$, $T = 0.05$')
    plt.xlabel(r'$\mu$', fontsize=20)
    plt.ylabel(r'$n(\mu)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'$\mu \times n(\mu, U, T)$')
    plt.savefig("occup.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
