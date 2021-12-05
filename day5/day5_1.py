from re import findall


def get_multiples(field_dim, file):
    grid = [[0]*field_dim for _ in range(field_dim)]
    for line in file:
        x1, y1, x2, y2 = map(int, findall('[0-9]+', line))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
    return sum(1 for line in grid for value in line if value > 1)


if __name__ == '__main__':
    print(get_multiples(10, open("test.txt")))
    print(get_multiples(1000, open("input.txt")))
