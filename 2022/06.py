from aocd import get_data

data = get_data(year=2022, day=6)

last_4 = [""] + list(data[:3])
for x in range(len(data[3:])):
    last_4.pop(0)
    last_4.append(data[3 + x])
    if len(set(last_4)) == 4:
        out_1 = x + 4
        break

print(out_1)

last_14 = [""] + list(data[:13])
for x in range(len(data[13:])):
    last_14.pop(0)
    last_14.append(data[13 + x])
    if len(set(last_14)) == 14:
        out_2 = x + 14
        break

print(out_2)
