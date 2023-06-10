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
from scipy.integrate import quad

#m, L, A, V = 1, 1, 1, 1
#r1 = lambda x: (2*m*L) / np.pi * 1 / (np.sqrt(2*m*x))
#r2 = lambda x: m*A / np.pi + 0*x
#r3 = lambda x: m*V / np.pi**2 * np.sqrt(2*m*x)

infinitesimal = 1e-16
Delta = 0.3
dos_metal = lambda e: (4/np.pi) * np.sqrt(1-np.clip(e**2, 0, 1))
dos_semimetal = lambda e: 2 * np.abs(e) * (np.abs(e) <= 1)
dos_semicondu = lambda e: np.abs(e) / np.sqrt(np.clip(e**2, (Delta+infinitesimal)**2, 1) - Delta**2) * (np.abs(e) > Delta) * (np.abs(e) < 1)

def sigma(rho, T):
    if (T > 10**(-2.55)):
        fdv = lambda e, T: (1/T) * np.exp(e/T) / (np.exp(e/T) + 1)**2
        result = quad(lambda e: rho(e) * fdv(e, T), -1, 1, points=(Delta, -Delta))
        return result[0]
    else:
        return rho(0)

def main():
    a = -1; b = 1
    #xs = np.linspace(a, b, 100000)
    #metal = dos_metal(xs)
    #semimetal = dos_semimetal(xs)
    #semicondu = dos_semicondu(xs)
    #integral_metal = simpson(metal, xs); print("integral_metal =", integral_metal)
    #integral_semimetal = simpson(semimetal, xs); print("integral_semimetal =", integral_semimetal)
    #integral_semicondu = simpson(semicondu, xs); print("integral_semicondu =", integral_semicondu)
    quad_metal = quad(dos_metal, -1, 1); integral_metal     = quad_metal[0]; print("integral_metal =", integral_metal)
    quad_semimetal = quad(dos_semimetal, -1, 1); integral_semimetal = quad_semimetal[0]; print("integral_semimetal =", integral_semimetal)
    quad_semicondu = quad(dos_semicondu, -1, 1, points=(-Delta, Delta)); integral_semicondu = quad_semicondu[0]; print("integral_semicondu =", integral_semicondu)
    xs = np.linspace(a, b, 400)
    metal = dos_metal(xs)
    semimetal = dos_semimetal(xs)
    semicondu = dos_semicondu(xs)
    plt.plot(xs,      metal, label=r'$\rho_{\text{metal}}(\epsilon), \int \rho(\epsilon) d\epsilon = %.3f$' % (integral_metal))
    plt.plot(xs,  semimetal, label=r'$\rho_{\text{semimetal}}(\epsilon), \int \rho(\epsilon) d\epsilon = %.3f$' % (integral_semimetal))
    plt.plot(xs,  semicondu, label=r'$\rho_{\text{semicondutor}}(\epsilon), \Delta = %.2f, \int \rho(\epsilon) d\epsilon = %.3f$' % (Delta, integral_semicondu))
    plt.xlabel(r'$\epsilon$', fontsize=20)
    plt.ylabel(r'$\rho(\epsilon)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'densidade de estados para diferentes sistemas físicos')
    plt.savefig("dos.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

    Ts = np.logspace(-6, -0.3, 400)
    sigma_metal, sigma_semimetal, sigma_semicondu = [], [], []
    for T in Ts:
        sigma_metal.append(sigma(dos_metal, T))
        sigma_semimetal.append(sigma(dos_semimetal, T))
        sigma_semicondu.append(sigma(dos_semicondu, T))
    plt.plot(Ts, sigma_metal, label=r'$\sigma_{\text{metal}}(T)$')
    plt.plot(Ts, sigma_semimetal, label=r'$\sigma_{\text{semimetal}}(T)$')
    plt.plot(Ts, sigma_semicondu, label=r'$\sigma_{\text{semicondutor}}(T)$')
    plt.xlabel(r'$T$', fontsize=20)
    plt.ylabel(r'$\sigma(T)$', fontsize=20)
    plt.legend(fontsize=12)
    plt.title(r'condutividade $\sigma(T)$ para diferentes sistemas físicos')
    plt.savefig("sigma.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
