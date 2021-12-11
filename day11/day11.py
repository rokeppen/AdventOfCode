import numpy as np
from itertools import product, count
from math import inf


def increase(m, to_look):
    new = set()
    for x, y in to_look:
        for xd, yd in product([-1, 0, 1], [-1, 0, 1]):
            m[x + xd, y + yd] += 1
            if m[x + xd, y + yd] == 10:
                new.add((x + xd, y + yd))
    return m if len(new) == 0 else increase(m, new)


def get_flashes(file):
    grid = np.pad(np.genfromtxt(file, delimiter=1), 1, 'constant', constant_values=-inf)
    result = 0
    for _ in range(100):
        grid = increase(grid + 1, zip(np.where(grid == 9)[0], np.where(grid == 9)[1]))
        result += np.count_nonzero(grid > 9)
        grid[grid > 9] = 0
    return result


def get_sync(file):
    grid = np.pad(np.genfromtxt(file, delimiter=1), 1, 'constant', constant_values=-inf)
    for i in count():
        grid = increase(grid + 1, zip(np.where(grid == 9)[0], np.where(grid == 9)[1]))
        grid[grid > 9] = 0
        if np.count_nonzero(grid == 0) == np.count_nonzero(grid > -1):
            return i + 1


if __name__ == '__main__':
    print(get_flashes("test.txt"))
    print(get_flashes("input.txt"))
    print(get_sync("test.txt"))
    print(get_sync("input.txt"))
