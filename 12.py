from collections import defaultdict, deque

from aocd import get_data

data = get_data(day=12)

inp = data.split("\n")

nbrs_orig = defaultdict(set)

for row in inp:
    nodes = row.split("-")
    if nodes[1] != "start" and nodes[0] != "end":
        nbrs_orig[nodes[0]].add(nodes[1])
    if nodes[0] != "start" and nodes[1] != "end":
        nbrs_orig[nodes[1]].add(nodes[0])


def find_paths(node, found_paths, path):
    if node == node.lower():
        if path.count(node) > 1:
            path.pop()
            return found_paths, path
    if node == "end":
        found_paths.append(path.copy())
        path.pop()
        return found_paths, path
    for nbr in nbrs_orig[node]:
        path.append(nbr)
        found_paths, path = find_paths(nbr, found_paths, path)
    path.pop()
    return found_paths, path


out, p = find_paths("start", [], deque(["start"]))

print(len(out))


def find_paths_2(node, found_paths, path):
    if node == node.lower():
        if path.count(node) > 1:
            if path[0] == "X":
                path.pop()
                return found_paths, path
            else:
                path.appendleft("X")
    if node == "end":
        found_paths.append(path.copy())
        path.pop()
        return found_paths, path
    for nbr in nbrs_orig[node]:
        path.append(nbr)
        found_paths, path = find_paths_2(nbr, found_paths, path)
    pc = path.count(node)
    path.pop()
    if node == node.lower() and pc == 2:
        path.popleft()
    return found_paths, path


out, p = find_paths_2("start", [], deque(["start"]))

print(len(out))
