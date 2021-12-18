import re
from math import ceil, floor

from aocd import get_data
from requests.api import get

data = get_data(day=18)

inp = data.split("\n")


def find_explode(s):
    cnt, found_exp, br_start, br_end = 0, False, None, None
    for i in range(len(s)):
        if not found_exp:
            if s[i] == "[":
                cnt += 1
                br_start = i
            elif s[i] == "]":
                cnt -= 1
            if cnt >= 5:
                found_exp = True
        else:
            if s[i] == "[":
                br_start = i
            elif s[i] == "]":
                br_end = i + 1
                break
    if br_end:
        m = re.search(r"^\[(\d+),(\d+)\]$", s[br_start:br_end])
        s_left, s_right, i_left, i_right = (
            s[:br_start],
            s[br_end:],
            int(m.group(1)),
            int(m.group(2)),
        )
        m_left, m_right = re.search(r"(\d+)(\D+)$", s_left), re.search(
            r"^(\D+)(\d+)", s_right
        )
        if m_left:
            d = m_left.group(1)
            loc = s_left.rfind(d)
            i = int(d)
            s_left = s_left[:loc] + str(i + i_left) + s_left[(loc + len(d)) :]
        if m_right:
            d = m_right.group(2)
            loc = s_right.find(d)
            i = int(d)
            s_right = (
                s_right[:loc] + str(i + i_right) + s_right[(loc + len(d)) :]
            )
        s_mod = s_left + "0" + s_right
        return s_mod, True
    return s, False


def find_split(s):
    m = re.search(r"\d{2,}", s)
    if m:
        d = m.group(0)
        loc = s.find(d)
        i = int(d)
        s_mod = (
            s[:loc]
            + "["
            + str(floor(i / 2))
            + ","
            + str(ceil(i / 2))
            + "]"
            + s[(loc + len(d)) :]
        )
        return s_mod, True
    return s, False


def get_magnitude(s):
    if type(s) != list:
        return s
    else:
        return 3 * get_magnitude(s[0]) + 2 * get_magnitude(s[1])


def simplify_list(inp):
    for i in range(len(inp)):
        if i == 0:
            s = inp[i]
        else:
            s = "[" + s + "," + inp[i] + "]"
        while True:
            s, retry = find_explode(s)
            if retry:
                continue
            s, retry = find_split(s)
            if retry:
                continue
            break
    return s


print(get_magnitude(eval(simplify_list(inp))))

m = 0
for i in range(len(inp)):
    for j in range(len(inp)):
        if j == i:
            continue
        mag = get_magnitude(eval(simplify_list([inp[i], inp[j]])))
        if mag > m:
            m = mag
        mag = get_magnitude(eval(simplify_list([inp[j], inp[i]])))
        if mag > m:
            m = mag

print(m)
