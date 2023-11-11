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

r  = 1
u4 = -1

def f(m, u6):
    return 1/2 * r * m**2 + u4 * m**4 + u6 * m**6


def main():
    xmin = -1.8; xmax = 1.8
    xs = np.linspace(xmin, xmax, 1000)
    plt.plot(xs, f(xs, 2),   label=r'$u_6 = 2$')
    plt.plot(xs, f(xs, 1),   label=r'$u_6 = 1$')
    plt.plot(xs, f(xs, 0.5), label=r'$u_6 = 0.5$')
    plt.plot(xs, f(xs, 0.4), label=r'$u_6 = 0.4$')
    plt.plot(xs, f(xs, 0.3), label=r'$u_6 = 0.3$')
    plt.plot(xs, 0 * xs, '--', linewidth=2, color='k')
    plt.xlabel(r'$m$', fontsize=20)
    plt.ylabel(r'$f$', fontsize=20)
    plt.legend(fontsize=12)
    plt.xlim(xmin, xmax)
    plt.ylim(-0.65, 2)
    plt.title(r'densidade de energia livre de Landau')
    plt.savefig("landau-free_energy.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
