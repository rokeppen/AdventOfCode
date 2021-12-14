from collections import defaultdict
from math import ceil


def insert(p, dic, c):
    new = defaultdict(int)
    for key, value in p.items():
        new[key[0] + dic[key]] += value
        new[dic[key] + key[1]] += value
    return p if not c else insert(new, dic, c - 1)


def get_polymer(file, steps):
    start, start_dict, occur = file.readline(), defaultdict(int), defaultdict(int)
    for i in range(len(start) - 2):
        start_dict[start[i:i+2]] += 1
    file.readline()
    for key, value in insert(start_dict, {l[:2]: l[6] for l in file}, steps).items():
        occur[key[0]] += value / 2
        occur[key[1]] += value / 2
    return ceil(max(occur.values())) - ceil(min(occur.values()))


if __name__ == "__main__":
    print(get_polymer(open("test.txt"), 10))
    print(get_polymer(open("input.txt"), 10))
    print(get_polymer(open("test.txt"), 40))
    print(get_polymer(open("input.txt"), 40))
