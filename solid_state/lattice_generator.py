#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
## comentar as 4 linhas abaixo caso nao tenha o LaTeX no matplotlib ###
from matplotlib import rc
plt.style.use('bmh')
#rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
#rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage{physics} \usepackage{bm}')
#matplotlib.verbose.level = 'debug-annoying'
#######################################################################
#from scipy.integrate import simpson

def main():
    a1x, a1y = 1, 0
    #a2x, a2y = 0, 1
    #a2x, a2y = 0.3, 0.9
    a2x, a2y = 1/2, np.sqrt(3)/2

    M = np.linspace(-20, 20, 41)
    N = np.linspace(-20, 20, 41)
    for x in M:
        Rx = x * a1x + N * a2x
        Ry = x * a1y + N * a2y
        for y in N:
            Rx = x * a1x + y * a2x
            Ry = x * a1y + y * a2y
            plt.plot([Rx], [Ry], marker='o', linewidth='5', color='#348ABD')
    plt.xlabel(r'$x$', fontsize=20)
    plt.ylabel(r'$y$', fontsize=20)
    plt.xlim(-1.6, 5.6)
    plt.ylim(-1.6, 5.6)
    #plt.legend(fontsize=12)
    plt.grid(False)
    plt.title(r'rede triangular')
    plt.gca().set_aspect('equal')
    plt.savefig("lattice.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
