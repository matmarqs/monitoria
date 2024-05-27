from sympy import symbols, sqrt, latex
from sympy.matrices import Matrix, GramSchmidt

f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 = symbols(
'varphi_1 varphi_2 varphi_3 varphi_4 varphi_5 varphi_6 varphi_7 varphi_8 varphi_9 varphi_10')

h = 8   # order of the group
dim = [1, 1, 1, 1]  # degeneracies of the irreps $B_{2g}$, $B_{3g}$, $A_{2u}$, $B_{1u}$

# chi is the 4x8 matrix for the characters of the irreps [B2g, B3g, A2u, B1u] of the group D_2h
#         $E$  $C_{2z}$  $C_{2y}$  $C_{2x}$   $i$   $\sigma_h$   $\sigma_{xz}$  $\sigma_{yz}$
chi = [ [ 1,     -1,        1,       -1,       1,       -1,           1,             -1,    ],     #  $B_{2g}$, index 0
        [ 1,     -1,       -1,        1,       1,       -1,          -1,              1,    ],     #  $B_{3g}$, index 1
        [ 1,      1,        1,        1,      -1,       -1,          -1,             -1,    ],     #  $A_{2u}$, index 2
        [ 1,      1,       -1,       -1,      -1,       -1,           1,              1,    ], ]   #  $B_{1u}$, index 3

class Proj:     # element of symmetry from D_2h
    def __init__(self, Pf1, Pf2, Pf9):
        self.P = [Pf1, Pf2, Pf9]

# D2h is a list with 8 elements of class Proj
#             $E$                   $C_{2z}$
D2h = [ Proj( f1,  f2, f9),   Proj( f5,  f6, f10),
#            $C_{2y}$               $C_{2x}$
        Proj(-f4, -f3, -f10), Proj(-f8, -f7, -f9),
#             $i$                    $\sigma_h$
        Proj(-f5, -f6, -f10), Proj(-f1, -f2, -f9),
#           $\sigma_{xz}$        $\sigma_{yz}$
        Proj( f8,  f7, f9),   Proj( f4,  f3, f10),  ]

# irrep is the index 0, 1, 2, 3 for $B_{2g}$, $B_{3g}$, $A_{2u}$, $B_{1u}$
# phi is the index 0, 1, 2 for phi_1, phi_2, phi_3
def proj_irrep(irrep, phi):
    soma = 0
    for R in range(len(D2h)):
        soma += chi[irrep][R] * D2h[R].P[phi]
    return soma * dim[irrep] / h

def norm(u):
    soma = 0
    for e in u:
        soma += e**2
    return sqrt(soma)

def normalize(L):
    norma = norm(L)
    for i in range(len(L)):
        L[i] /= norma

def myappend(vars, psis, proj):
    psi = []
    for v in vars:
        psi.append(proj.coeff(v))
    normalize(psi)
    psis.append(Matrix(psi))

def get_var(coeffs, vars):
    var = 0
    for i in range(len(coeffs)):
        var += coeffs[i] * vars[i]
    return var

def main():
    vars = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    # irrep is the index 0, 1, 2, 3 for $B_{2g}$, $B_{3g}$, $A_{2u}$, $B_{1u}$
    # phi is the index 0, 1, 2 for phi_1, phi_2, phi_3
    psis = []
    myappend(vars, psis, proj_irrep(irrep=0, phi=0))    # $\mathcal{P}^{B_{2g}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=0, phi=1))    # $\mathcal{P}^{B_{2g}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=0, phi=2))    # $\mathcal{P}^{B_{2g}} \varphi_9$
    myappend(vars, psis, proj_irrep(irrep=1, phi=0))    # $\mathcal{P}^{B_{3g}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=1, phi=1))    # $\mathcal{P}^{B_{3g}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=2, phi=0))    # $\mathcal{P}^{A_{2u}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=2, phi=1))    # $\mathcal{P}^{A_{2u}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=3, phi=0))    # $\mathcal{P}^{B_{1u}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=3, phi=1))    # $\mathcal{P}^{B_{1u}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=3, phi=2))    # $\mathcal{P}^{B_{1u}} \varphi_9$

    #print(psis[0])
    #print(psis[1])
    #print(psis[2])
    #print(psis[3])
    #print(psis[4])
    #print(psis[5])
    #print(psis[6])
    #print(psis[7])
    #print(psis[8])
    #print(psis[9])

    print("B2g")
    out_B2g = GramSchmidt(psis[0:3], orthonormal=True)
    print("$$")
    print(latex(get_var(out_B2g[0], vars)))  # $\Psi_{B_{2g}}^{(1)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_B2g[1], vars)))  # $\Psi_{B_{2g}}^{(2)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_B2g[2], vars)))  # $\Psi_{B_{2g}}^{(3)}$
    print("$$")
    print()

    print("B3g")
    out_B3g = GramSchmidt(psis[3:5], orthonormal=True)
    print("$$")
    print(latex(get_var(out_B3g[0], vars)))  # $\Psi_{B_{3g}}^{(1)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_B3g[1], vars)))  # $\Psi_{B_{3g}}^{(2)}$
    print("$$")
    print()

    print("A2u")
    out_A2u = GramSchmidt(psis[5:7], orthonormal=True)
    print("$$")
    print(latex(get_var(out_A2u[0], vars)))  # $\Psi_{A_{2u}}^{(1)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_A2u[1], vars)))  # $\Psi_{A_{2u}}^{(2)}$
    print("$$")
    print()

    print("B1u")
    out_B1u = GramSchmidt(psis[7:10], orthonormal=True)
    print("$$")
    print(latex(get_var(out_B1u[0], vars)))  # $\Psi_{B_{1u}}^{(1)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_B1u[1], vars)))  # $\Psi_{B_{1u}}^{(2)}$
    print("$$")
    print("$$")
    print(latex(get_var(out_B1u[2], vars)))  # $\Psi_{B_{1u}}^{(3)}$
    print("$$")
    print()

if __name__ == '__main__':
    main()
