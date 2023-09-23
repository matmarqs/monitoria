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

kB = 1
m = 1

def f(v, T):
    return 4 * np.pi * v**2 * np.exp(-m*v**2/(2*kB*T))*(2*np.pi*kB*T/m)**(-3/2)


def main():
    vmin = 0; vmax = 1.2
    vs = np.linspace(vmin, vmax, 400)
    plt.plot(vs, f(vs, 0.001), label=r'$T=0.001$')
    plt.plot(vs, f(vs, 0.005), label=r'$T=0.005$')
    plt.plot(vs, f(vs, 0.01), label=r'$T=0.01$')
    plt.plot(vs, f(vs, 0.1), label=r'$T=0.1$')
    #plt.plot(vs, f(vs, 1), label=r'$T=1$')
    plt.xlabel(r'$T$', fontsize=20)
    plt.ylabel(r'$f(v)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'Distribuição do módulo da velocidade para diferentes temperaturas')
    plt.savefig("distrib-vel-maxwell.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
