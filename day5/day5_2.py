from re import findall
from itertools import cycle


def my_range(x, y):
    return cycle([x]) if x == y else range(x, y + 1) if x < y else range(x, y - 1, -1)


def get_multiples(field_dim, file):
    grid = [[0]*field_dim for _ in range(field_dim)]
    for line in file:
        x1, y1, x2, y2 = map(int, findall('[0-9]+', line))
        for x, y in zip(my_range(x1, x2), my_range(y1, y2)):
            grid[y][x] += 1
    return sum(1 for line in grid for value in line if value > 1)


if __name__ == '__main__':
    print(get_multiples(10, open("test.txt")))
    print(get_multiples(1000, open("input.txt")))
