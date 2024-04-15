class Group:
    def __init__(self, elements):
        self.elements = elements
    def find(self, perm):
        for g in self.elements:
            if perm == g.perm:
                return g
        return None

class Element:
    def __init__(self, perm, name):
        self.perm = perm
        self.name = name
    #### DEBUG #####
    def show(self):
        self.perm.show()

class Perm:
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
    D3h = Group([E, C3, C32, C21, C22, C23, Sigma_v1, Sigma_v2, Sigma_v3, Sigma_h, S3, S32])
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
    D3d = Group([E, C3, C32, C21, C22, C23, Sigma_d1, Sigma_d2, Sigma_d3, I, S6, S65])
    return D3d

def print_MultiplicationTable(group, group_name):
    elem = group.elements
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
        print(f'& {elem[j].name} ', end='') if j < order-1 else print(f'& {elem[j].name} \\\\')
    print(r'\hline')
    for i in range(order):
        print(f'{elem[i].name} & ', end='')
        for j in range(order):
            res = group.find(elem[i].perm * elem[j].perm)
            print(f'{res.name} & ', end='') if j < order-1 else print(f'{res.name} \\\\')
    print(r'\hline')
    print(r'\end{tabular}')


def main():
    #D3h = generate_D3h()
    #print_MultiplicationTable(D3h, r'$D_{3h}$')

    D3d = generate_D3d()
    print_MultiplicationTable(D3d, r'$D_{3d}$')

if __name__ == '__main__':
    main()
