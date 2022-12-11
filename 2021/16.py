from math import prod

from aocd import get_data

data = get_data(year=2021, day=16)

inp = bin(int("0x" + data, 16))[2:].zfill(4 * len(data))

msg = inp

version_sum = 0


def parse_packet(msg):
    ver = int("0b" + msg[:3], 2)
    op = int("0b" + msg[3:6], 2)
    msg = msg[6:]
    global version_sum
    version_sum += ver
    if op == 4:
        leftover = msg
        int_str = ""
        while leftover[0] == "1":
            int_str += leftover[1:5]
            leftover = leftover[5:]
        int_str += leftover[1:5]
        leftover = leftover[5:]
        out = int("0b" + int_str, 2)
    else:
        op_mode = int(msg[0])
        msg = msg[1:]
        out = []
        if op_mode == 0:
            subp_len = int("0b" + msg[:15], 2)
            msg = msg[15:]
            tmp = msg[:subp_len]
            while len(tmp) > 0:
                x, tmp = parse_packet(tmp)
                out.append(x)
            leftover = msg[subp_len:]
        else:
            subp_num = int("0b" + msg[:11], 2)
            msg = msg[11:]
            tmp = msg
            for i in range(subp_num):
                x, msg = parse_packet(msg)
                out.append(x)
            leftover = msg
        if type(out) != list:
            out = [out]
        if op == 0:
            out = sum(out)
        elif op == 1:
            out = prod(out)
        elif op == 2:
            out = min(out)
        elif op == 3:
            out = max(out)
        elif op == 5:
            out = 1 * (out[0] > out[1])
        elif op == 6:
            out = 1 * (out[0] < out[1])
        elif op == 7:
            out = 1 * (out[0] == out[1])
        else:
            raise Exception
    return out, leftover


out, leftover = parse_packet(msg)

print(version_sum)
print(out)
