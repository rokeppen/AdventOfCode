import math


def count_increase():
    height, result = math.inf, 0
    for x in open("input.txt", "r"):
        result += 1 if int(x) > height else 0
        height = int(x)
    return result


if __name__ == '__main__':
    print(count_increase())
