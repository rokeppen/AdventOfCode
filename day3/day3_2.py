from numpy import array


def reduce(v, f):
    i = 0
    while len(v) > 1:
        v = v[v[:, i] == f(v[:, i], key=lambda c: ((v[:, i] == c).sum(), c))]
        i += 1
    return int(''.join(v[0]), 2)


def get_product():
    values = array([list(x.strip()) for x in open("input.txt")])
    return reduce(values, min) * reduce(values, max)


if __name__ == '__main__':
    print(get_product())
