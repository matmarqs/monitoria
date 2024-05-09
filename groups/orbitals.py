from sympy import symbols, Poly, sqrt, latex
from sympy.matrices import Matrix, GramSchmidt

f1, f2, f3, f4, f5, f6 = symbols('varphi_1 varphi_2 varphi_3 varphi_4 varphi_5 varphi_6')

h = 24  # order of the group
dim = [1, 2, 1, 2]  # the dimensions of the irreps $B_{2g}$, $E_{1g}$, $A_{2u}$, $E_{2u}$

# chi is the 4x24 matrix for the characters from the irreps [B2g, E1g, A2u, E2u] and group D_6h
#         E  2 C_6    2 C_3    C_2    3 C_2'    3 C_2''   i   2 S_3   2 S_6   \sigma_h  3 \sigma_d  3 \sigma_v
chi = [ [ 1, -1,-1,    1, 1,   -1,  -1,-1,-1,  1, 1, 1,   1,  -1,-1,   1, 1,     -1,     -1,-1,-1,    1,1,1,   ],     #  $B_{2g}$, index 0
        [ 2,  1, 1,   -1,-1,   -2,   0, 0, 0,  0, 0, 0,   2,   1, 1,  -1,-1,     -2,      0, 0, 0,    0,0,0,   ],     #  $E_{1g}$, index 1
        [ 1,  1, 1,    1, 1,    1,  -1,-1,-1, -1,-1,-1,  -1,  -1,-1,  -1,-1,     -1,      1, 1, 1,    1,1,1,   ],     #  $A_{2u}$, index 2
        [ 2, -1,-1,   -1,-1,    2,   0, 0, 0,  0, 0, 0,  -2,   1, 1,   1, 1,     -2,      0, 0, 0,    0,0,0,   ], ]   #  $E_{2u}$, index 3

class Proj:     # element of symmetry from D_6h
    def __init__(self, Pf1, Pf2):
        self.P = [Pf1, Pf2]

# D6h is a list with 24 elements
#              E               C6             C6^5            C3            C3^2             C2
D6h = [ Proj( f1,  f2), Proj( f6,  f1), Proj( f2,  f3), Proj( f5,  f6), Proj( f3,  f4), Proj( f4,  f5),
#            C2'(1)          C2'(2)         C2'(3)         C2''(1)        C2''(2)          C2''(3)
        Proj(-f3, -f6), Proj(-f5, -f2), Proj(-f1, -f4), Proj(-f2, -f1), Proj(-f4, -f3), Proj(-f6, -f5),
#              i              S3             S3^2             S6           S6^5            sigma_h
        Proj(-f4, -f5), Proj(-f5, -f6), Proj(-f3, -f4), Proj(-f6, -f1), Proj(-f2, -f3), Proj(-f1, -f2),
#           sigma_d(1)    sigma_d(2)     sigma_d(3)      *sigma_v(1)*     sigma_v(2)      sigma_v(3)
        Proj( f2,  f1), Proj( f4,  f3), Proj( f6,  f5), Proj( f1,  f2), Proj( f3,  f4), Proj( f5,  f6),  ]

# irrep is the index 0, 1, 2, 3 for $B_{2g}$, $E_{1g}$, $A_{2u}$, $E_{2u}$
# phi is the index 0, 1 for phi_1 or phi_2
def proj_irrep(irrep, phi):
    soma = 0
    for R in range(len(D6h)):
        soma += chi[irrep][R] * D6h[R].P[phi]
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

def myappend(psis, proj):
    psi = Poly(proj).coeffs()
    normalize(psi)
    psis.append(Matrix(psi))

def get_var(coeffs, vars):
    var = 0
    for i in range(len(coeffs)):
        var += coeffs[i] * vars[i]
    return var

def main():
    vars = [f1, f2, f3, f4, f5, f6]
    psis = []
    myappend(psis, proj_irrep(0, 0))    # $\mathcal{P}^{B_{2g}} \varphi_1$
    myappend(psis, proj_irrep(1, 0))    # $\mathcal{P}^{E_{1g}} \varphi_1$
    myappend(psis, proj_irrep(1, 1))    # $\mathcal{P}^{E_{1g}} \varphi_2$
    myappend(psis, proj_irrep(2, 0))    # $\mathcal{P}^{A_{2u}} \varphi_1$
    myappend(psis, proj_irrep(3, 0))    # $\mathcal{P}^{E_{2u}} \varphi_1$
    myappend(psis, proj_irrep(3, 1))    # $\mathcal{P}^{E_{2u}} \varphi_2$

    print("B2g")
    print("$$")
    print(latex(get_var(psis[0], vars)))  # $\mathcal{P}^{B_{2g}} \varphi_1$
    print("$$")
    print()

    print("E1g")
    out_E1g = GramSchmidt(psis[1:3], orthonormal=True)
    print("$$")
    print(latex(get_var(out_E1g[0], vars)))  # $\mathcal{P}^{E_{1g}} \varphi_1$
    print("$$")
    print("$$")
    print(latex(get_var(out_E1g[1], vars)))  # $\mathcal{P}^{E_{1g}} \varphi_2$
    print("$$")
    print()

    print("A2u")
    print("$$")
    print(latex(get_var(psis[3], vars)))  # $\mathcal{P}^{B_{2g}} \varphi_1$
    print("$$")
    print()

    print("E2u")
    out_E2u = GramSchmidt(psis[4:6], orthonormal=True)
    print("$$")
    print(latex(get_var(out_E2u[0], vars)))  # $\mathcal{P}^{E_{2u}} \varphi_1$
    print("$$")
    print("$$")
    print(latex(get_var(out_E2u[1], vars)))  # $\mathcal{P}^{E_{2u}} \varphi_2$
    print("$$")

if __name__ == '__main__':
    main()
