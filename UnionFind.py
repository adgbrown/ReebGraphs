# Union Find Algorithm with collapsing and rank optimization

class UnionFind:
    parent = {}
    # parent: dictionary assigning to each node a parent, which is the unique label of a cluster
    rank = {}
    # rank: dictionary assigning to each node the size of the most recent cluster for which that node was the parent

    def __init__(self, node_set):
        for i in node_set:
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, a):
        i = a
        while self.parent[i] != i:
            i = self.parent[i]
        self.parent[a] = i
        return self.parent[a]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[b] = self.parent[parent_b] = parent_a
            self.rank[parent_a] = self.rank[parent_a] + self.rank[parent_b]
        else:
            self.parent[a] = self.parent[parent_a] = parent_b
            self.rank[parent_b] = self.rank[parent_a] + self.rank[parent_b]


# Example
V = [0, 1, 2, 3, 4]
uf = UnionFind(V)
uf.union(0, 1)
print('Union 0 and 1')
print('parents: ', uf.parent)
print('cluster size: ', uf.rank)
uf.union(2, 3)
print('Union 2 and 3')
print('parents: ', uf.parent)
print('cluster size: ', uf.rank)
uf.union(0, 3)
print('Union 0 and 3')
print('parents: ', uf.parent)
print('cluster size: ', uf.rank)
uf.union(4, 0)
print('Union 4 and 0')
print('parents: ', uf.parent)
print('cluster size: ', uf.rank)
