

def mostBalancedPartition(parent, files_size):
    def size_tree(i):
        size_sums[i] = files_size[i] + \
            sum(size_tree(j) for j in child[i])
        return size_sums[i]

    n = len(parent)

    child = [[] for i in range(n)]

    for i in range(1, n):
        child[parent[i]].append(i)
        
    size_sums = [None for i in range(n)]

    size_tree(0)
    return min(abs(size_sums[0] - 2 * ss) for ss in size_sums[1:])
