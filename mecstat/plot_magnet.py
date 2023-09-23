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

mu = 1
B = 1
kB = 1
S = 1/2

coth = lambda x: 1 / np.tanh(x)
L = lambda x: coth(x) - 1/x

def m(T):
    beta = 1/(kB*T)
    return mu * L(beta*mu*B)

def m_quant(T, J):
    x = B / (kB * T)
    BJ = (2*J+1)/(2*J) * coth(x*(2*J+1)/(2*J)) - 1/(2*J) * coth(x/(2*J))
    return BJ


def main():
    Tmin = 0.0001; Tmax = 20
    Ts = np.linspace(Tmin, Tmax, 400)
    plt.plot(Ts, m(Ts), label=r'clássico')
    plt.plot(Ts, m_quant(Ts, 1/2), label=r'quântico $J = 1/2$')
    plt.plot(Ts, m_quant(Ts, 1), label=r'quântico $J = 1$')
    plt.plot(Ts, m_quant(Ts, 7), label=r'quântico $J = 7$')
    plt.xlabel(r'$T$', fontsize=20)
    plt.ylabel(r'$\frac{m}{N}$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'Magnetização $m(T)$')
    plt.savefig("magnetiz.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
