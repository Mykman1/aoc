from collections import Counter

from aocd import get_data

data = get_data(day=8)
in_1 = [[y.split(" ") for y in x.split(" | ")] for x in data.split("\n")]

print(len([y for x in in_1 for y in x[1] if len(y) in (2, 3, 4, 7)]))

in_2 = in_1

decoded_int_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

out = []
for x in in_2:
    cnt = Counter([z for y in x[0] for z in y])
    decode_map = {}
    decode_map[[x[0] for x in cnt.items() if x[1] == 6][0]] = "b"
    decode_map[[x[0] for x in cnt.items() if x[1] == 4][0]] = "e"
    decode_map[[x[0] for x in cnt.items() if x[1] == 9][0]] = "f"

    d_or_g = [x[0] for x in cnt.items() if x[1] == 7]
    encoded_4 = [y for y in x[0] if len(y) == 4][0]
    decode_map[[x for x in d_or_g if x in encoded_4][0]] = "d"
    decode_map[[x for x in d_or_g if x not in encoded_4][0]] = "g"

    a_or_c = [x[0] for x in cnt.items() if x[1] == 8]
    encoded_6 = [
        y
        for y in x[0]
        if len(set(y).difference(decode_map.keys())) == 1
        and set(y).intersection(decode_map.keys()) == set(decode_map.keys())
    ][0]
    decode_map[[x for x in a_or_c if x in encoded_6][0]] = "a"
    decode_map[[x for x in a_or_c if x not in encoded_6][0]] = "c"

    num = 0
    for y in range(4):
        decoded_list = "".join(sorted([decode_map[z] for z in x[1][y]]))
        num += (10 ** (3 - y)) * decoded_int_map[decoded_list]

    out.append(num)

print(sum(out))
