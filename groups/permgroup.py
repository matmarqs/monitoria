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
        print(')')

D3h =
