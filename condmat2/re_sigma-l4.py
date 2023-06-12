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

def ReSigma(w, t):
    return t / (1 + (w*t)**2)


def main():
    ws = np.linspace(-0.25, 0.25, 300)
    plt.plot(ws, ReSigma(ws, 10), label=r'$\tau = 10$')
    plt.plot(ws, ReSigma(ws, 20), label=r'$\tau = 20$')
    plt.plot(ws, ReSigma(ws, 50), label=r'$\tau = 50$')
    plt.plot(ws, ReSigma(ws, 80), label=r'$\tau = 80$')
    plt.plot(ws, ReSigma(ws, 100), label=r'$\tau = 100$')
    plt.xlabel(r'$\omega$', fontsize=20)
    plt.ylabel(r'$\Re[\sigma(\omega)]$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'$\omega \times \Re[\sigma(\omega)]$')
    plt.savefig("resigma.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
