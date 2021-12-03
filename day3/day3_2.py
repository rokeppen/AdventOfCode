from numpy import array


def reduce(v, is_scrubber):
    i = 0
    while len(v) > 1:
        most_common = min(v[:, i], key=lambda c: (is_scrubber * (v[:, i] == c).sum(), is_scrubber * int(c)))
        v = array(list(filter(lambda x: x[i] == most_common, v)))
        i += 1
    return int(''.join(v[0]), 2)


def get_product():
    values = array([list(x.strip()) for x in open("input.txt")])
    return reduce(values, -1) * reduce(values, 1)


if __name__ == '__main__':
    print(get_product())
