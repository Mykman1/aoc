from aocd import get_data

data = get_data(year=2022, day=13)

inp_1 = [tuple([eval(y) for y in x.split("\n")]) for x in data.split("\n\n")]


def comp(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return "<"
        elif left > right:
            return ">"
        else:
            return "="
    elif type(left) == list and type(right) == list:
        if len(left) == 0 and len(right) > 0:
            return "<"
        elif len(left) > 0 and len(right) == 0:
            return ">"
        elif len(left) == 0 and len(right) == 0:
            return "="
        else:
            el_comp = comp(left[0], right[0])
            return comp(left[1:], right[1:]) if el_comp == "=" else el_comp
    else:
        left = [left] if type(left) == int else left
        right = [right] if type(right) == int else right
        return comp(left, right)


out_1 = 0
which_pair = 1
for left, right in inp_1:
    if comp(left, right) == "<":
        out_1 += which_pair
    which_pair += 1

print(out_1)

divider_packets = [[[2]], [[6]]]
inp_2 = [
    eval(y) for x in data.split("\n\n") for y in x.split("\n")
] + divider_packets

sorted_packets = []

for packet in inp_2:
    idx = 0
    for sorted_packet in sorted_packets:
        if comp(sorted_packet, packet) == "<":
            idx += 1
        else:
            break
    sorted_packets = sorted_packets[:idx] + [packet] + sorted_packets[idx:]

out_2 = (sorted_packets.index(divider_packets[0]) + 1) * (
    sorted_packets.index(divider_packets[1]) + 1
)

print(out_2)
