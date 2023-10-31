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

hbar = 1
m = 0.5

# The trace is system dependent, in this example we use:
trace = np.array([[0, 0],       # Gamma
                  [0.5, 0],     # M_1
                  [1, 0],       # X
                  [1, 0.5],     # M_2
                  [1, 1],       # L
                  [0.5, 0.5],   # M_3
                  [0, 0]])      # Gamma
label_ticks = [r'$\Gamma$', r'$M_1$', r'$X$', r'$M_2$', r'$L$', r'$M_3$', r'$\Gamma$']

n_kpoints = 600
dispersion = lambda k: hbar**2 * np.linalg.norm(k)**2 / (2 * m)

def energy_k(trace, dispersion, n_kpoints=600, E_f=0):
    energies = []
    n_trace = int(n_kpoints / (len(trace) - 1))
    for path_num in range(len(trace) - 1):
        for i in range(n_trace):
            z = i / n_trace
            k = trace[path_num] * (1-z) + z * trace[path_num + 1]
            energies.append(dispersion(k))
    energies = np.array(energies)
    energies -= E_f
    return energies

energy = energy_k(trace, dispersion, n_kpoints)

n_trace = int(n_kpoints / (len(trace)-1))
normal_ticks = [i*n_trace for i in range(len(trace))]

plt.plot(range(n_kpoints), energy)

plt.xlim(normal_ticks[0], normal_ticks[-1])
plt.xticks(normal_ticks, label_ticks, fontsize=20)
plt.grid(True, axis='x')
plt.ylabel(r'energy$/\mathcal{E}$', fontsize=20)

ymin = 0; ymax = +2.10
plt.ylim(ymin, ymax);
plt.savefig("band_struct_square_free.png", dpi=300, format='png', bbox_inches="tight")
