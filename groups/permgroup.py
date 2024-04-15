class Element:
    def __init__():

class Perm:
    def __init__(self, L):
        self.n = len(L)
        self.perm = [i-1 for i in L]
    def __eq__(self, other):
        return self.perm == other.perm
    def __mul__(self, other):
        return Perm([self.perm[i]+1 for i in other.perm])
    def find(self, j):
        for i in range(self.n):
            if self.perm[i] == j:
                return i
    def inv(self):
        return Perm([self.find(j)+1 for j in range(self.n)])
    def show(self):
        print('( ', end='')
        for i in range(self.n):
            print(f'{i+1} ', end='')
        print(')\n( ', end='')
        for i in self.perm:
            print(f'{i+1} ', end='')
        print(')\n')

def ident(n)
    return Perm([i for i in range(1, n+1)])

def

def main():
    E = ident(n)
    C3 = Perm([3,4,5,6,1,2,7,8])
    C32 = C3.inv()
    Sigma_h = Perm([2,1,4,3,6,5,8,7])
    C21 = Perm([2,1,6,5,4,3,8,7])
    C22 = Perm([6,5,4,3,2,1,8,7])
    C23 = Perm([4,3,2,1,6,5,8,7])
    S3 = C3 * Sigma_h
    S32 = C32 * Sigma_h
    Sigma_v1 = C21 * Sigma_h
    Sigma_v2 = C22 * Sigma_h
    Sigma_v3 = C23 * Sigma_h

    D3h = [E, C3, C32, C21, C22, C23, Sigma_v1, Sigma_v2, Sigma_v3, Sigma_h, S3, S32]

if __name__ == '__main__':
    main()
