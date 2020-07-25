class DisjointSet:
    def __init__(self, N):
        self.p = list(range(N)) # parent lookup
        self.r = [0]*N # rank lookup

    def find(self, u):
        while self.p[u] != u:
            u, self.p[u] = self.p[u], self.p[self.p[u]]
        return u

    def union(self, u, v):
        uroot, vroot = self.find(u), self.find(v)

        if uroot == vroot:
            return False

        if self.r[uroot] < self.r[vroot]:
            uroot, vroot = vroot, uroot

        self.p[vroot] = uroot
        if self.r[uroot] == self.r[vroot]:
            self.r[uroot] += 1

        return True

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
        
    
def test():
    N = 10
    dj = DisjointSet(N)
    parent = list(range(N))
    dj.union(0, 1)
    dj.union(0, 5)
    dj.union(3, 5)
    dj.union(4, 6)
    assert dj.is_connected(1, 3)
    assert dj.is_connected(3, 0)
    assert not dj.is_connected(3, 6)


if __name__ == '__main__':
	test()