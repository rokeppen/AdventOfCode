import numpy as np


def get_low_points(grid):
    return [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if
            all(grid[i, j] < grid[i + dx, j + dy] for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])]


def get_risk(file):
    grid = np.pad(np.genfromtxt(file, delimiter=1), 1, 'constant', constant_values=9)
    return sum(grid[i, j] + 1 for i, j in get_low_points(grid))


def increase(m, to_look):
    new = to_look.copy()
    for x, y in to_look:
        for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if m[x + xd, y + yd] != 9:
                new.add((x + xd, y + yd))
    return new if len(new) == len(to_look) else increase(m, new)


def get_basin(file):
    grid = np.pad(np.genfromtxt(file, delimiter=1), 1, 'constant', constant_values=9)
    return np.prod(sorted(len(increase(grid, {p})) for p in get_low_points(grid))[:-4:-1])


if __name__ == '__main__':
    print(get_risk("test.txt"))
    print(get_risk("input.txt"))
    print(get_basin("test.txt"))
    print(get_basin("input.txt"))
