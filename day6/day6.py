from math import comb


def series(n):
    return 1 + sum(comb(i + j, j) for j in range(n//9+1) for i in range((n-9*j)//7+1))


def get_fish(file, days):
    return sum(series(days - int(x) - 1) for x in file.readline().split(','))


if __name__ == '__main__':
    print(get_fish(open("test.txt"), 80))
    print(get_fish(open("input.txt"), 80))
    print(get_fish(open("test.txt"), 256))
    print(get_fish(open("input.txt"), 256))
