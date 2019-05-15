import math
import random
import sys
import time


def get_ints():
    return [int(x) for x in input().split(' ')]


def contract(edge, edges, nodes_groups, keep_left=True):
    left, right = edge
    if not keep_left:
        tmp = left
        left = right
        right = tmp
    new_edges = []
    for e in edges:
        if not e == edge:
            if right in e:
                l, r = e
                new_edges.append({r, left} if l == right else {l, left})
            else:
                new_edges.append(e)

    nodes_groups[left] = nodes_groups[left] | nodes_groups[right]
    del nodes_groups[right]
    return new_edges, nodes_groups


def contract_n(edges, n, nodes_groups):
    nodes_groups = nodes_groups.copy()
    for _ in range(n):
        idx = random.randint(0, len(edges) - 1)
        edge = edges[idx]
        edges, nodes_groups = contract(edge, edges, nodes_groups, keep_left=idx % 2 == 0)
    return edges, nodes_groups


def fast_min_cut(edges, n_nodes, nodes_groups=None):
    if nodes_groups is None:
        nodes_groups = {n: frozenset([n]) for n in range(1, n_nodes + 1)}

    if n_nodes <= 2:
        nodes_groups = set(nodes_groups.values())
        return len(edges), nodes_groups
    else:
        rec = 2
        n = min(n_nodes - 2, math.ceil(1 + n_nodes / math.sqrt(rec)))

        smallest_min_cut = sys.maxsize
        groups = []
        for _ in range(rec):
            rec_edges, rec_nodes_groups = contract_n(edges, n, nodes_groups)
            min_cut, min_cut_groups = fast_min_cut(rec_edges, n_nodes - n, rec_nodes_groups)
            if min_cut < smallest_min_cut:
                smallest_min_cut = min_cut
                groups = min_cut_groups
            elif min_cut == smallest_min_cut:
                groups.update(min_cut_groups)

        return smallest_min_cut, groups


def find_num_min_cuts(edges, n_nodes, start_time, max_time):
    smallest_min_cut = len(edges)
    all_nodes_groups = set()

    while not started_since(start_time, max_time):
        min_cut, nodes_groups = fast_min_cut(edges, n_nodes)

        if min_cut < smallest_min_cut:
            smallest_min_cut = min_cut
            all_nodes_groups = nodes_groups

        elif min_cut == smallest_min_cut:
            all_nodes_groups.update(nodes_groups)

    return smallest_min_cut, len(all_nodes_groups) // 2


def started_since(start_time, max_time_sec):
    return (time.time() - start_time) > max_time_sec


def main():
    start_time = time.time()
    random.seed(start_time + 4)
    n_nodes, n_edges = get_ints()
    edges = [set(get_ints()) for _ in range(n_edges)]
    min_cut, n = find_num_min_cuts(edges, n_nodes, start_time=start_time, max_time=14.7)
    print(min_cut, n)


main()
