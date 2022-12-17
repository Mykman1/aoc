from aocd import get_data

data = get_data(year=2022, day=10)

inp = [(x[:4], int(x[5:]) if x[5:] else None) for x in data.split("\n")]

X = 1
cycle = 0
out_1 = 0
for inst, val in inp:
    if inst == "noop":
        cycle += 1
        if cycle % 40 == 20:
            out_1 += cycle * X
    elif inst == "addx":
        for _ in range(2):
            cycle += 1
            if cycle % 40 == 20:
                out_1 += cycle * X
        X += val

print(out_1)

X = 1
cycle = 0
screen = []
for inst, val in inp:
    if inst == "noop":
        screen.append("#" if abs(X - (cycle % 40)) <= 1 else ".")
        cycle += 1
    elif inst == "addx":
        for _ in range(2):
            screen.append("#" if abs(X - (cycle % 40)) <= 1 else ".")
            cycle += 1
        X += val

out_2 = []
for i in range(len(screen) // 40):
    out_2.append("".join(screen[i * 40 : (i + 1) * 40]))
out_2 = "\n".join(out_2)

print(out_2)
