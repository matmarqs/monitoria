#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
## comentar as 4 linhas abaixo caso nao tenha o LaTeX no matplotlib ###
from matplotlib import rc
plt.style.use('bmh')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{physics} \usepackage{bm}')
#matplotlib.verbose.level = 'debug-annoying'
#######################################################################
#from scipy.integrate import simpson

def main():
    a = 1
    m = 0.4
    Q = (np.pi/a, np.pi/a)

    X = np.linspace(0, 5*a, 6)
    Y = np.linspace(0, 5*a, 6)
    mx = m * np.cos((np.pi/a) * X[0] + (np.pi/a) * Y)
    #my = m * np.sin((np.pi/a) * X[0] + (np.pi/a) * Y)
    #print(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    #QV = plt.quiver(np.full(len(Y), X[0]), Y, mx, my, color='#A60628', angles='xy', scale_units='xy', scale=1, label=r'$m_j^z = m^z e^{i \bm{Q} \vdot \bm{R}_j}$')
    QV = plt.quiver(np.full(len(Y), X[0]), Y, np.full(len(mx), 0), mx, color='#A60628', angles='xy', scale_units='xy', scale=1)
    #plt.quiverkey(QV, 5, 2.2, 0.3, r'$m_j^z = m^z e^{i \bm{Q} \vdot \bm{R}_j}$', coordinates='data')
    for x in X:
        mx = m * np.cos((np.pi/a) * x + (np.pi/a) * Y)
        if x != X[0]:
            plt.quiver(np.full(len(Y), x), Y, np.full(len(mx), 0), mx, color='#A60628', angles='xy', scale_units='xy', scale=1)
        for y in Y:
            plt.plot([x], [y], marker='o', linewidth='5', color='#348ABD')
    #plt.quiver([0.5], [0.5], [0], [0.5], color='#A60628', angles='xy', scale_units='xy', scale=1)
    plt.xlabel(r'$x$', fontsize=20)
    plt.ylabel(r'$y$', fontsize=20)
    plt.xlim(-0.6, 5.6)
    plt.ylim(-0.6, 5.6)
    #plt.legend(fontsize=12)
    plt.grid(False)
    plt.title(r'Magnetização $m_j^z = \Re[m^z e^{i \bm{Q} \vdot \bm{R}_j}]$ no espaço real')
    plt.savefig("magnetization-real_space.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
