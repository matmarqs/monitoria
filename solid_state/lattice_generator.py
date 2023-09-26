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

    f = plt.figure()  # f = figure(n) if you know the figure number
    f.set_size_inches(11.69,8.27)
    rc('figure', figsize=(11.69,8.27))

    a1x, a1y = 2, 0
    #a2x, a2y = 0, 1
    #a2x, a2y = 0.3, 0.9
    a2x, a2y = 2/2, 2*np.sqrt(3)/2
    b1 = [1, 0]
    b2 = [1/2,  np.sqrt(3)/2]

    M = np.linspace(-20, 20, 41)
    N = np.linspace(-20, 20, 41)
    for x in M:
        for y in N:
            Rx = x * a1x + y * a2x
            Ry = x * a1y + y * a2y
            plt.plot([Rx], [Ry], marker='o', linewidth='5', color='#348ABD')
            plt.plot([Rx + b1[0]], [Ry + b1[1]], marker='o', linewidth='5', color='#A60628')
            plt.plot([Rx + b2[0]], [Ry + b2[1]], marker='o', linewidth='5', color='#7A68A6')
            # ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']
    #plt.xlabel(r'$x$', fontsize=20)
    #plt.ylabel(r'$y$', fontsize=20)
    plt.xlim(-10.6, 10.6)
    plt.ylim(-10.6, 10.6)
    #plt.legend(fontsize=12)
    plt.grid(False)
    plt.title(r'rede kagomé')
    plt.gca().set_aspect('equal')
    #plt.savefig("lattice.png", dpi=300, format='png', bbox_inches="tight")
    plt.savefig("lattice.pdf", dpi=300, format='pdf')
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
