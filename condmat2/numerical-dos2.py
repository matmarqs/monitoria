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

from scipy.integrate import simpson as integral
from scipy.optimize import brentq as root

L = 500
N = L * L
Gamma = 1/40
t = 1

def dirac(x):
    return Gamma / (np.pi * (x**2 + Gamma**2))

def eps(kx, ky):
    return -2 * t * ( np.cos(kx) + np.cos(ky) )

def dos(E):
    rho = 0
    for i in range(1, L+1):
        kx = 2 * np.pi * i / (L)
        for j in range(1, L+1):
            ky = 2 * np.pi * j / (L)
            rho += dirac(E - eps(kx, ky))
    return rho / N

def dos_approx(w):
    return 1/(4*np.pi*t**2) * np.log(t/np.abs(w))


def n(Ef):
    ws = np.linspace(-4*t, Ef, 200)
    return 2 * integral(dos(ws), ws)

def main():
    r = root(lambda x: n(x) - 1.7, -4*t, 4*t)
    print(r)

    #a = -4.5*t; b = 4.5*t
    #xs = np.linspace(a, b, 1000)
    #plt.plot(xs,  dos(xs), label=r'$\rho_{\text{numerical}}(\epsilon)$')
    #plt.xlabel(r'$\epsilon$', fontsize=20)
    #plt.ylabel(r'$\rho(\epsilon)$', fontsize=20)
    #plt.legend(fontsize=16)
    #plt.title(r'densidade de estados tight-binding $d=2$')
    #plt.savefig("num_dos.png", dpi=300, format='png', bbox_inches="tight")
    #plt.clf()

if __name__ == '__main__':
    main()
