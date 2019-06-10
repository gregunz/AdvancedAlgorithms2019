# Authors: Mario Bucev, Grégoire Clément, Lucas Ramirez

def line_to_ints():
    return [int(x) for x in input().split(' ')]

# Reading inputs
n, m = line_to_ints()
costs = dict(enumerate(line_to_ints(), 1))
edges = [line_to_ints() for _ in range(m)]


# Useful variables
vertices = list(range(1, n+1))
edges = [set(t) for t in edges]
edges_set = set(range(1, m+1))
edges_of = {v:{i for i,e  in enumerate(edges, 1) if v in e} for v in vertices}

# Useful functions
def w(v):
    return costs[v]

def cover():
    return [v for v in vertices if sum(y[e] for e in edges_of[v]) == w(v)]

def is_a_vertex_cover(C):
    return len({e for v in C for e in edges_of[v]}) == len(edges)

# Algorithm
y = {e:0 for e in edges_set}
C = cover()

while not is_a_vertex_cover(C):
    not_covered_e = edges_set - {e for v in C for e in edges_of[v]}
    for new_e_idx in not_covered_e:
        new_e = edges[new_e_idx - 1]
        diff = min([w(v) - sum([y[e] for e in edges_of[v]]) for v in new_e])
        if diff > 0:
            y[new_e_idx] += diff
            break
    C = cover()

print(len(C))
print(*C)
print(*y.values())