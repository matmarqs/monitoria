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

v, L, A, V = 1, 1, 1, 1
r1 = lambda x: (2*L) / (np.pi * v) + 0*x
r2 = lambda x: (A * x) / (np.pi * v**2)
r3 = lambda x: (V * x**2) / (np.pi**2 * v**3)

def main():
    a = 0.1; b = 10
    xs = np.linspace(a, b, 500)
    plt.plot(xs,  r1(xs), label=r'$\rho_1(\epsilon) = \frac{2 L}{\pi v}$')
    plt.plot(xs,  r2(xs), label=r'$\rho_2(\epsilon) = \frac{A}{\pi v^2} \, \epsilon$')
    plt.plot(xs,  r3(xs), label=r'$\rho_3(\epsilon) = \frac{V}{\pi^2 v^3} \, \epsilon^2$')
    plt.xlabel(r'$\epsilon$', fontsize=20)
    plt.ylabel(r'$\rho_d(\epsilon)$', fontsize=20)
    plt.legend(fontsize=16)
    plt.title(r'densidade de estados $\rho_d(\epsilon)$ para a dispersão $E(\vb{k}) = vk$')
    plt.savefig("dos.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
