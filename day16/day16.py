from itertools import count
from numpy import prod


ops = {0: sum, 1: prod, 2: min, 3: max, 5: lambda x: int(x[0] > x[1]), 6: lambda x: int(x[0] < x[1]), 7: lambda x: int(x[0] == x[1])}


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


def parse(string, rec):
    return rec(read_subs(bin(int(string, 16))[2:].zfill(len(string) * 4))[0])


def sum_versions(expr):
    return expr[0] if expr[1] == 4 else expr[0] + sum(map(sum_versions, expr[2]))


def evaluate(expr):
    return expr[2] if expr[1] == 4 else ops[expr[1]](list(map(evaluate, expr[2])))


if __name__ == '__main__':
    data = open("input.txt").read().strip()
    print(parse("8A004A801A8002F478", sum_versions))
    print(parse("620080001611562C8802118E34", sum_versions))
    print(parse("C0015000016115A2E0802F182340", sum_versions))
    print(parse("A0016C880162017C3686B18A3D4780", sum_versions))
    print(parse(data, sum_versions))
    print(parse("C200B40A82", evaluate))
    print(parse("04005AC33890", evaluate))
    print(parse("880086C3E88112", evaluate))
    print(parse("CE00C43D881120", evaluate))
    print(parse("D8005AC2A8F0", evaluate))
    print(parse("F600BC2D8F", evaluate))
    print(parse("9C005AC2F8F0", evaluate))
    print(parse("9C0141080250320F1802104A08", evaluate))
    print(parse(data, evaluate))
