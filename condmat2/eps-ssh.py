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

N = 300
alpha = 0.0
a, t = 1, 1
w = t * (1 + alpha)
v = t * (1 - alpha)
e1 = lambda k: -np.sqrt(w**2 + v**2 + 2*v*w*np.cos(2*k*a))
e2 = lambda k:  np.sqrt(w**2 + v**2 + 2*v*w*np.cos(2*k*a))

ks = np.linspace(-np.pi/(2*a), np.pi/(2*a), N)

def main():
    #plt.plot(ks,  e1(ks), label=r'$\epsilon_{-}(k)$', linestyle='dotted', linewidth=4)
    #plt.plot(ks,  e2(ks), label=r'$\epsilon_{+}(k)$', linestyle='dotted', linewidth=4)
    plt.plot(ks,  e2(ks), label=r'$\epsilon_{+}(k)$', linewidth=2)
    plt.plot(ks,  e1(ks), label=r'$\epsilon_{-}(k)$', linewidth=2)
    plt.xlabel(r'$k$', fontsize=20)
    plt.ylabel(r'$\epsilon(k)$', fontsize=20)
    plt.legend(fontsize=16)
    plt.title(r'relação de dispersão para o modelo SSH, $\alpha = %.1f$' % (alpha), fontsize=18)
    plt.savefig("eps_ssh.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
