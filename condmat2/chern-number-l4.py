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
from scipy.integrate import dblquad

def func(ky, kx, D):
    a = D * np.cos(kx)* np.cos(ky) - np.cos(kx) - np.cos(ky)
    b = (D**2 + 2*(1 + np.cos(kx)*np.cos(ky) - D*(np.cos(kx)+np.cos(ky))))**(3/2)
    return a/b

def chern(D):
    i = dblquad(func, -np.pi, np.pi, -np.pi, np.pi, args=(D,), epsabs=1e-16, epsrel=1e-16)
    return i[0] / (4*np.pi)

def main():
    Deltas = np.linspace(-4, 4, 47)
    cherns = []
    for d in Deltas:
        cherns.append(chern(d))
    plt.plot(Deltas, cherns, 'o', linewidth='5', label=r'chern number')
    plt.xlabel(r'$\Delta$', fontsize=20)
    plt.ylabel(r'$C$', fontsize=20)
    plt.legend(fontsize=12)
    #plt.title(r'número de Chern')
    plt.savefig("chern.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
