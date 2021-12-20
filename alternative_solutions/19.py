import numpy as np
from aocd import get_data

data = get_data(day=19)

inp = [x.split("\n") for x in data.split("\n\n")]

scanner_0 = np.array([[int(y) for y in x.split(",")] for x in inp[0][1:]])
scanners = [
    np.array([[int(y) for y in x.split(",")] for x in i[1:]]) for i in inp[1:]
]

base_rot_matrices = [
    np.array(x)
    for x in [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
        [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
        [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
        [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
        [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
    ]
]
rot_around_x_matrices = [
    np.array(x)
    for x in [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
        [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
        [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
    ]
]
rot_matrices = []
for m1 in base_rot_matrices:
    for m2 in rot_around_x_matrices:
        rot_matrices.append(np.dot(m1, m2))

R = np.array(rot_matrices)

confirmed_beacons = set()
for y in [tuple(x) for x in scanner_0]:
    confirmed_beacons.add(y)

abs_scanners = [scanner_0]
scanner_centers = [(0, 0, 0)]
scanners_multi = [np.einsum("ij,kjl->kil", x, R) for x in scanners]

while len(scanners_multi) > 0:
    print(len(scanners_multi))
    try:
        for i in range(len(scanners_multi)):
            X = scanners_multi[i]
            for X_0_abs in abs_scanners:
                centers_abs = np.einsum(
                    "ri,jx->rjix",
                    np.ones(X.shape[0:2], dtype=int),
                    X_0_abs,
                    optimize="greedy",
                ) - np.einsum(
                    "rix,j->rjix",
                    X,
                    np.ones(X_0_abs.shape[0], dtype=int),
                    optimize="greedy",
                )
                centers_abs = centers_abs.reshape(
                    (
                        centers_abs.shape[0],
                        centers_abs.shape[1] * centers_abs.shape[2],
                        centers_abs.shape[3],
                    )
                )
                centers_exp = np.einsum(
                    "rjx,i->rjix",
                    centers_abs,
                    np.ones(X.shape[1], dtype=int),
                    optimize="greedy",
                )
                centers_exp = centers_exp.reshape(
                    (
                        centers_exp.shape[0] * centers_exp.shape[1],
                        centers_exp.shape[2],
                        centers_exp.shape[3],
                    )
                )
                X_exp = np.einsum(
                    "rix,j->rjix",
                    X,
                    np.ones(centers_abs.shape[1], dtype=int),
                    optimize="greedy",
                )
                X_exp = X_exp.reshape(
                    (
                        X_exp.shape[0] * X_exp.shape[1],
                        X_exp.shape[2],
                        X_exp.shape[3],
                    )
                )
                X_abs = X_exp + centers_exp
                centers_abs = centers_abs.reshape(
                    (
                        centers_abs.shape[0] * centers_abs.shape[1],
                        centers_abs.shape[2],
                    )
                )
                for j in range(len(X_abs)):
                    common_pts = set(map(tuple, X_0_abs)).intersection(
                        set(map(tuple, X_abs[j]))
                    )
                    if len(common_pts) >= 12:
                        raise StopIteration
    except StopIteration:
        del scanners_multi[i]
        abs_scanners.append(X_abs[j])
        scanner_centers.append(tuple(centers_abs[j]))
        for y in [tuple(x) for x in X_abs[j]]:
            confirmed_beacons.add(y)

print(len(confirmed_beacons))

print(
    max(
        [
            abs(a - x) + abs(b - y) + abs(c - z)
            for x, y, z in scanner_centers
            for a, b, c in scanner_centers
        ]
    )
)
