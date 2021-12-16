from itertools import count
from functools import reduce
from operator import add, mul, gt, lt, eq


def read_subs(binary):
    version, type_id = int(binary[:3], 2), int(binary[3:6], 2)
    if type_id == 4:
        literal = ''
        for i in count(6, 5):
            literal += binary[i + 1:i + 5]
            if not int(binary[i]):
                return (version, type_id, int(literal, 2)), binary[i + 5:]
    expr = []
    if int(binary[6]):
        to_do, binary = int(binary[7:18], 2), binary[18:]
        for i in range(to_do):
            term, binary = read_subs(binary)
            expr.append(term)
    else:
        to_do, binary = len(binary[22:]) - int(binary[7:22], 2), binary[22:]
        while len(binary) > to_do:
            term, binary = read_subs(binary)
            expr.append(term)
    return (version, type_id, expr), binary


def parse(file, rec):
    string = open(file).read().strip()
    return rec(read_subs(bin(int(string, 16))[2:].zfill(len(string) * 4))[0])


def sum_versions(exp):
    return exp[0] if exp[1] == 4 else exp[0] + sum(map(sum_versions, exp[2]))


def evaluate(exp):
    return exp[2] if exp[1] == 4 else reduce([add, mul, min, max, 0, gt, lt, eq][exp[1]], list(map(evaluate, exp[2])))


if __name__ == '__main__':
    print(parse("input.txt", sum_versions))
    print(parse("input.txt", evaluate))
