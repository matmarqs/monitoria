#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
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

L = 1000
N = L * L
Gamma = 1/400
t = 1
a = 1

def dirac(x):
    return Gamma / (np.pi * (x**2 + Gamma**2))

def gamma(kx, ky):
    return -t * np.exp(-1j*kx*a) * (1 + 2 * np.exp(-3*1j*kx*a/2) * np.cos(np.sqrt(3)*ky*a/2))

def eps(kx, ky):
    return np.abs(gamma(kx,ky))

def dos(E):
    rho = 0
    for i in range(1, L+1):
        kx = 2 * np.pi * i / (L)
        for j in range(1, L+1):
            ky = 2 * np.pi * j / (L)
            rho += dirac(E - eps(kx, ky)) + dirac(E + eps(kx, ky))
    return rho / N

def main():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X = np.linspace(-4*t, 4*t, 200)
    Y = np.linspace(-4*t, 4*t, 200)
    X, Y = np.meshgrid(X, Y)
    Z = eps(X, Y)

    # Plot the surface.
    surf1 = ax.plot_surface(X, Y, +Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    surf2 = ax.plot_surface(X, Y, -Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    tmp_planes = ax.zaxis._PLANES
    ax.zaxis._PLANES = ( tmp_planes[2], tmp_planes[3],
                         tmp_planes[0], tmp_planes[1],
                         tmp_planes[4], tmp_planes[5])
    ax.xaxis.set_rotate_label(False)
    ax.set_xlabel(r'$k_x$', fontsize=20, rotation=0)
    ax.yaxis.set_rotate_label(False)
    ax.set_ylabel(r'$k_y$', fontsize=20, rotation=0)
    ax.zaxis.set_rotate_label(False)
    ax.set_zlabel(r'$\epsilon(\vb{k})$', fontsize=20, rotation=0)
    ax.set_title('relação de dispersão para o grafeno', fontsize=20)

    # Customize the z axis.
    ax.set_zlim(-3*t, 3*t)
    ax.zaxis.set_major_locator(LinearLocator(5))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.1f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf1, shrink=0.5, aspect=20)

    #plt.savefig("graphene_eps.png", dpi=300, format='png', bbox_inches='tight')
    plt.savefig("graphene_eps.png", dpi=300, format='png')
    #plt.show()
    plt.clf()

if __name__ == '__main__':
    main()
