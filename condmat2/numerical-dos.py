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

#m, L, A, V = 1, 1, 1, 1
#r1 = lambda x: (2*m*L) / np.pi * 1 / (np.sqrt(2*m*x))
#r2 = lambda x: m*A / np.pi + 0*x
#r3 = lambda x: m*V / np.pi**2 * np.sqrt(2*m*x)

L = 500
N = L * L
Gamma = 0.1
a, t = 1, 1

def dirac(x):
    return Gamma / (np.pi * (x**2 + Gamma**2))

def eps(kx, ky):
    return -2 * t * ( np.cos(kx * a) + np.cos(ky * a) )

def dos(E):
    rho = 0
    for i in range(L):
        kx = 2 * np.pi * i / L
        for j in range(L):
            ky = 2 * np.pi * j / L
            rho = dirac(E - eps(kx, ky))
    return rho / N

def main():
    a = -2.5*t; b = 2.5*t
    xs = np.linspace(a, b, 300)
    plt.plot(xs,  r(xs), label=r'$\rho(\epsilon) = \frac{1}{\pi a t \sqrt{1-\qty(\frac{\epsilon}{2t})^2}}$')
    plt.xlabel(r'$\epsilon$', fontsize=20)
    plt.ylabel(r'$\rho(\epsilon)$', fontsize=20)
    plt.legend(fontsize=16)
    plt.title(r'densidade de estados tight-binding $d=1$')
    plt.savefig("dos.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
