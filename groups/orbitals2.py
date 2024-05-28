from sympy import symbols, sqrt, latex, pprint, simplify, print_latex
from sympy.matrices import Matrix, GramSchmidt

f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 = symbols(
'varphi_1 varphi_2 varphi_3 varphi_4 varphi_5 varphi_6 varphi_7 varphi_8 varphi_9 varphi_10')

h = 8   # order of the group
dim = [1, 1, 1, 1]  # degeneracies of the irreps $B_{2g}$, $B_{3g}$, $A_{u}$, $B_{1u}$

# chi is the 4x8 matrix for the characters of the irreps [B2g, B3g, Au, B1u] of the group D_2h
#         $E$  $C_{2z}$  $C_{2y}$  $C_{2x}$   $i$   $\sigma_h$   $\sigma_{xz}$  $\sigma_{yz}$
chi = [ [ 1,     -1,        1,       -1,       1,       -1,           1,             -1,    ],     #  $B_{2g}$, index 0
        [ 1,     -1,       -1,        1,       1,       -1,          -1,              1,    ],     #  $B_{3g}$, index 1
        [ 1,      1,        1,        1,      -1,       -1,          -1,             -1,    ],     #  $A_{u}$, index 2
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

# irrep is the index 0, 1, 2, 3 for $B_{2g}$, $B_{3g}$, $A_{u}$, $B_{1u}$
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

def print_eig(D, strS, P, S, vars):
    mdim = len(D[0,:])
    for i in range(mdim):
        orb = P[0, i] * S[0]
        for j in range(1, mdim):
            orb += P[j, i] * S[j]
        orb_var = get_var(orb, vars)
        if orb_var.coeff(f1) < 0 or orb_var.coeff(f2) < 0:  # get pretty signal
            orb_var *= -1
        print(r'\; E_{%s}^{(%d)} &\approx %s, & \Psi_{%s}^{(%d)} &= %s \\' % (strS, i+1,
            latex(D[i,i].evalf(2)), strS, i+1, latex(orb_var.evalf(2))))

def main():
    vars = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    # irrep is the index 0, 1, 2, 3 for $B_{2g}$, $B_{3g}$, $A_{u}$, $B_{1u}$
    # phi is the index 0, 1, 2 for phi_1, phi_2, phi_3
    psis = []
    myappend(vars, psis, proj_irrep(irrep=0, phi=0))    # $\mathcal{P}^{B_{2g}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=0, phi=1))    # $\mathcal{P}^{B_{2g}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=0, phi=2))    # $\mathcal{P}^{B_{2g}} \varphi_9$
    myappend(vars, psis, proj_irrep(irrep=1, phi=0))    # $\mathcal{P}^{B_{3g}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=1, phi=1))    # $\mathcal{P}^{B_{3g}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=2, phi=0))    # $\mathcal{P}^{A_{u}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=2, phi=1))    # $\mathcal{P}^{A_{u}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=3, phi=0))    # $\mathcal{P}^{B_{1u}} \varphi_1$
    myappend(vars, psis, proj_irrep(irrep=3, phi=1))    # $\mathcal{P}^{B_{1u}} \varphi_2$
    myappend(vars, psis, proj_irrep(irrep=3, phi=2))    # $\mathcal{P}^{B_{1u}} \varphi_9$

    out_B2g = GramSchmidt(psis[0:3], orthonormal=True)
    out_B3g = GramSchmidt(psis[3:5], orthonormal=True)
    out_Au = GramSchmidt(psis[5:7], orthonormal=True)
    out_B1u = GramSchmidt(psis[7:10], orthonormal=True)
    subspaces = [out_B2g, out_B3g, out_Au, out_B1u]
    subsp_latex = [r'B_{2g}', r'B_{3g}', r'A_{u}', r'B_{1u}']
    for s in range(len(subspaces)):
        for i in range(len(subspaces[s])):
            S = subspaces[s]; strS = subsp_latex[s]
            print(r'$$')
            print(r'\psi_{%s}^{(%d)} = ' % (strS, i+1), end='')
            print_latex(get_var(S[i], vars))
            print(r'$$')


    alpha, beta = symbols('alpha beta')

    H = Matrix( [ [ alpha, beta, 0, 0, 0, 0, 0, 0, beta, 0,    ],
                  [ beta, alpha, beta, 0, 0, 0, 0, 0, 0, 0,    ],
                  [ 0, beta, alpha, beta, 0, 0, 0, 0, 0, 0,    ],
                  [ 0, 0, beta, alpha, 0, 0, 0, 0, 0, beta,    ],
                  [ 0, 0, 0, 0, alpha, beta, 0, 0, 0, beta,    ],
                  [ 0, 0, 0, 0, beta, alpha, beta, 0, 0, 0,    ],
                  [ 0, 0, 0, 0, 0, beta, alpha, beta, 0, 0,    ],
                  [ 0, 0, 0, 0, 0, 0, beta, alpha, beta, 0,    ],
                  [ beta, 0, 0, 0, 0, 0, 0, beta, alpha, beta, ],
                  [ 0, 0, 0, beta, beta, 0, 0, 0, beta, alpha, ], ] )

    for s in range(len(subspaces)):
        S = subspaces[s]; strS = subsp_latex[s]
        mat = []
        for vec_i in S:
            row = []
            for vec_j in S:
                res = vec_i.T * H * vec_j
                row.append(simplify(res[0,0]))
            mat.append(row)
        mmat = Matrix(mat)
        P, D = mmat.diagonalize(normalize=True)
        print(r'\normalsize')
        print(r'$$')
        print(r'H_{%s} = ' % (strS), end='')
        print_latex(mmat, mat_str='pmatrix', mat_delim='')
        print(r'\Rightarrow')
        print(r'$$')
        print(r'\footnotesize')
        print(r'\begin{align*}')
        print_eig(D, strS, P, S, vars)
        print(r'\end{align*}')

if __name__ == '__main__':
    main()
