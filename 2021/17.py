from aocd import get_data

data = get_data(year=2021, day=17)

inp = [
    [int(y) for y in x.split("..")]
    for x in data.replace("target area: x=", "").split(", y=")
]

max_inits = []
if inp[1][1] > 0:
    max_inits.append(inp[1][1])

if inp[1][0] < 0:
    max_inits.append(-inp[1][0] - 1)

max_y_init = max(max_inits)

print((max_y_init * (max_y_init + 1)) // 2)

min_y_init = min(inp[1][0], 0)

good_starts = []
for x_init in range(1, inp[0][1] + 1):
    for y_init in range(min_y_init, max_y_init + 1):
        x, y = 0, 0
        vel_x = x_init
        vel_y = y_init
        step = 0
        while x <= inp[0][1] + 1 and y >= min_y_init:
            step += 1
            x += vel_x
            y += vel_y
            if vel_x > 0:
                vel_x -= 1
            vel_y -= 1
            if (inp[0][0] <= x <= inp[0][1]) and (inp[1][0] <= y <= inp[1][1]):
                good_starts.append((x_init, y_init))
                break

print(len(good_starts))
