class Group:    # lista de Element
    def __init__(self, elements, name):
        self.elements = elements
        self.name = name
    def find(self, perm):
        for g in self.elements:
            if perm == g.perm:
                return g
        return None
    def printtable(self):
        elem = self.elements
        group_name = self.name
        order = len(elem)
        def tabular_string(n):
            s = "|c|"
            while n > 0:
                s = s+"c " if n > 1 else s+"c |"
                n -= 1
            return s
        print(r'\begin{tabular} { %s }' % tabular_string(order))
        print(r'\hline')
        print(group_name+' ', end='')
        for j in range(order):
            if j < order-1:
                print(f'& {elem[j].eqname} ', end='')
            else:
                print(f'& {elem[j].eqname} \\\\')
        print(r'\hline')
        for i in range(order):
            print(f'{elem[i].eqname} & ', end='')
            for j in range(order):
                res = self.find(elem[i].perm * elem[j].perm)
                if j < order-1:
                    print(f'{res.eqname} & ', end='')
                else:
                    print(f'{res.eqname} \\\\')
        print(r'\hline')
        print(r'\end{tabular}')

class Element:  # Permutacao e o nome
    def __init__(self, perm, eqname):
        self.perm = perm
        self.name = eqname[1:-1]  # remove '$$' from latex equation
        self.eqname = eqname
    #### DEBUG #####
    def show(self):
        self.perm.show()

class Perm:     # permutacao C3 = Perm([2, 3, 1])
    def __init__(self, L):
        self.n = len(L)
        self.list = [i-1 for i in L]
    def __eq__(self, other):
        return self.list == other.list
    def __mul__(self, other):
        return Perm([self.list[i]+1 for i in other.list])
    def find(self, j):
        for i in range(self.n):
            if self.list[i] == j:
                return i
    def inv(self):
        return Perm([self.find(j)+1 for j in range(self.n)])
    #### DEBUG #####
    def show(self):
        print('( ', end='')
        for i in range(self.n):
            print(f'{i+1} ', end='')
        print(')\n( ', end='')
        for i in self.list:
            print(f'{i+1} ', end='')
        print(')\n')

def ident(n):
    return Perm([i for i in range(1, n+1)])

def generate_D3h():
    E = Element(ident(8), r'$E$')
    C3 = Element(Perm([3,4,5,6,1,2,7,8]), r'$C_3$')
    C32 = Element(C3.perm.inv(), r'$C_3^2$')
    Sigma_h = Element(Perm([2,1,4,3,6,5,8,7]), r'$\sigma_h$')
    C21 = Element(Perm([2,1,6,5,4,3,8,7]), r'$C_2^{(1)}$')
    C22 = Element(Perm([6,5,4,3,2,1,8,7]), r'$C_2^{(2)}$')
    C23 = Element(Perm([4,3,2,1,6,5,8,7]), r'$C_2^{(3)}$')
    S3 = Element(C3.perm * Sigma_h.perm, r'$S_3$')
    S32 = Element(C32.perm * Sigma_h.perm, r'$S_3^2$')
    Sigma_v1 = Element(C21.perm * Sigma_h.perm, r'$\sigma_v^{(1)}$')
    Sigma_v2 = Element(C22.perm * Sigma_h.perm, r'$\sigma_v^{(2)}$')
    Sigma_v3 = Element(C23.perm * Sigma_h.perm, r'$\sigma_v^{(3)}$')
    D3h = Group([E, C3, C32, C21, C22, C23, Sigma_v1, Sigma_v2, Sigma_v3, Sigma_h, S3, S32], r'$D_{3h}$')
    return D3h

def generate_D3d():
    E = Element(ident(8), r'$E$')
    C3 = Element(Perm([2,3,1,5,6,4,7,8]), r'$C_3$')
    C32 = Element(C3.perm.inv(), r'$C_3^2$')
    I = Element(Perm([6,4,5,2,3,1,8,7]), r'$i$')
    C21 = Element(Perm([6,5,4,3,2,1,8,7]), r'$C_2^{(1)}$')
    C22 = Element(Perm([5,4,6,2,1,3,8,7]), r'$C_2^{(2)}$')
    C23 = Element(Perm([4,6,5,1,3,2,8,7]), r'$C_2^{(3)}$')
    S6 = Element(C3.perm * I.perm, r'$S_6$')
    S65 = Element(C32.perm * I.perm, r'$S_6^5$')
    Sigma_d1 = Element(C21.perm * I.perm, r'$\sigma_d^{(1)}$')
    Sigma_d2 = Element(C22.perm * I.perm, r'$\sigma_d^{(2)}$')
    Sigma_d3 = Element(C23.perm * I.perm, r'$\sigma_d^{(3)}$')
    D3d = Group([E, C3, C32, C21, C22, C23, Sigma_d1, Sigma_d2, Sigma_d3, I, S6, S65], r'$D_{3d}$')
    return D3d

def conjugacy_classes(group):
    classes = set()
    for g in group.elements:
        g_class = set()
        for A in group.elements:
            g_class.add(group.find(A.perm.inv() * g.perm * A.perm))
        g_class = frozenset(g_class)
        classes.add(g_class)
    return classes

def print_conjclass(cl):
    string = r"\{ "
    for g in cl:
        string += "%s, " % g.name
    string = string[:-2] + r" \}"   # delete last two characters ", " and append " \}"
    print(string)

def main():
    group = generate_D3d()
    #group = generate_D3h()
    group.printtable()

    classes = conjugacy_classes(group)
    for cl in classes:
        print_conjclass(cl)

if __name__ == '__main__':
    main()
