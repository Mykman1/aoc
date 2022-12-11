import numpy as np
from aocd import get_data

data = get_data(year=2021, day=19)

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

confirmed_beacons = set()
for y in [tuple(x) for x in scanner_0]:
    confirmed_beacons.add(y)

abs_scanners = [scanner_0]
scanner_centers = [(0, 0, 0)]

while len(scanners) > 0:
    print(len(scanners))
    try:
        for i in range(len(scanners)):
            for r in rot_matrices:
                X = np.dot(scanners[i], r)
                for X_0_abs in abs_scanners:
                    for p in X:
                        for p_0_abs in X_0_abs[11:]:
                            center = p_0_abs - p
                            X_abs = X + center
                            common_pts = set(map(tuple, X_0_abs)).intersection(
                                set(map(tuple, X_abs))
                            )
                            if len(common_pts) >= 12:
                                raise StopIteration
    except StopIteration:
        del scanners[i]
        abs_scanners.append(X_abs)
        scanner_centers.append(center)
        for y in [tuple(x) for x in X_abs]:
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
