from aocd import get_data

data = get_data(day=3)
in_1 = data.split("\n")

y = []
for x in in_1:
    y.append([int(z) for z in x])

rot = [x for x in zip(*y)]
gamma_bin = [max(set(x), key=x.count) for x in rot]
eps_bin = [min(set(x), key=x.count) for x in rot]

gamma = 0
for b in gamma_bin:
    gamma = 2 * gamma + b

eps = 0
for b in eps_bin:
    eps = 2 * eps + b

print(gamma * eps)

in_2 = in_1

y = []
for x in in_2:
    y.append([int(z) for z in x])

rot = [list(x) for x in zip(*y)]

ox_bin = []
for i in range(len(rot)):
    c1 = rot[i].count(1)
    c0 = rot[i].count(0)
    if c0 == c1:
        ox_bin.append(1)
    elif c1 >= c0:
        ox_bin.append(1)
    else:
        ox_bin.append(0)
    y = [x for x in y if x[i] == ox_bin[i]]
    rot = [x for x in zip(*y)]

ox = 0
for b in ox_bin:
    ox = 2 * ox + b


y = []
for x in in_2:
    y.append([int(z) for z in x])

rot = [list(x) for x in zip(*y)]

scr_bin = []
for i in range(len(rot)):
    cts = {v: rot[i].count(v) for v in set(rot[i])}
    m = min([y for x, y in cts.items()])
    scr_bin.append(sorted([x for x, y in cts.items() if y == m])[0])
    y = [x for x in y if x[i] == scr_bin[i]]
    rot = [x for x in zip(*y)]
scr = 0
for b in scr_bin:
    scr = 2 * scr + b

print(ox * scr)
