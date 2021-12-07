from statistics import median, mean
from math import ceil, floor


def get_constant_fuel(file):
    values = list(map(int, file.readline().split(',')))
    return sum(abs(median(values) - x) for x in values)


def get_increasing_fuel(file):
    values = list(map(int, file.readline().split(',')))
    o1, o2 = ceil(mean(values)), floor(mean(values))
    return min(sum(abs(x-o1)*(abs(x-o1)+1)/2 for x in values), sum(abs(x-o2)*(abs(x-o2)+1)/2 for x in values))


if __name__ == '__main__':
    print(get_constant_fuel(open("input.txt")))
    print(get_increasing_fuel(open("input.txt")))
