from itertools import takewhile
from functools import reduce


def read_file(file):
    return set((int(line.split(',')[0]), int(line.split(',')[1])) for line in takewhile(lambda x: x != "\n", file)), \
           [(0 if line.split()[2].startswith('x') else 1, int(line.split()[2].split('=')[1])) for line in file]


def fold(points, inst):
    return set(tuple(2 * inst[1] - p[i] if inst[0] == i and p[i] > inst[1] else p[i] for i in range(2)) for p in points)


def fold_once(file):
    points, instructions = read_file(file)
    return len(fold(points, instructions[0]))


def fold_and_read(file):
    points, instructions = read_file(file)
    points = reduce(fold, instructions, points)
    return '\n'.join(''.join('#' if (x, y) in points else ' ' for x in range(max(p[0] for p in points) + 1)) for y in range(max(p[1] for p in points) + 1))


if __name__ == "__main__":
    print(fold_once(open("test.txt")))
    print(fold_once(open("input.txt")))
    print(fold_and_read(open("test.txt")))
    print(fold_and_read(open("input.txt")))
