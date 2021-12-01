import math


def count_increase():
    height, prev_prev, prev, result = math.inf, math.inf, math.inf, 0
    for x in open("input.txt", "r"):
        new_height = prev_prev + prev + int(x)
        result += 1 if new_height > height else 0
        height, prev_prev, prev = new_height, prev, int(x)
    return result


if __name__ == '__main__':
    print(count_increase())
