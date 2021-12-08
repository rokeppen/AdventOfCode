from itertools import permutations


def get_simple_count(file):
    return sum(1 for line in file for x in line.split('|')[1].strip().split(' ') if 1 < len(x) < 5 or len(x) == 7)


def decode(x, key):
    return ''.join(sorted(x.translate(x.maketrans(''.join(key), "abcdefg"))))


def get_count(file):
    table = {"abcdef": 0, "bc": 1, "abdeg": 2, "abcdg": 3, "bcfg": 4, "acdfg": 5, "acdefg": 6, "abc": 7, "abcdefg": 8, "abcdfg": 9}
    result, keys = 0, sorted(table.keys())
    for line in file:
        for per in permutations("abcdefg"):
            if sorted(decode(n, per) for n in line.split('|')[0].split()) == keys:
                result += int(''.join(str(table.get(decode(n, per))) for n in line.split('|')[1].split()))
                break
    return result


if __name__ == '__main__':
    print(get_simple_count(open("test.txt")))
    print(get_simple_count(open("input.txt")))
    print(get_count(open("test.txt")))
    print(get_count(open("input.txt")))
