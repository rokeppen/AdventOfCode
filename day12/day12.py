from collections import defaultdict


def extend_paths(paths, system, small_twice):
    new = []
    for path in paths:
        if path[-1] != "end":
            new.extend(path + [x] for x in system[path[-1]] if x not in path or x.isupper() or (small_twice and
                path.count(x) == 1 and x != "start" and all(path.count(y) == 1 for y in path if not y.isupper() and x != y)))
        else:
            new.append(path)
    return new if all(p[-1] == "end" for p in new) else extend_paths(new, system, small_twice)


def get_paths(file, small_twice):
    system = defaultdict(list)
    for line in file:
        v1, v2 = line.strip().split('-')
        system[v1].append(v2)
        system[v2].append(v1)
    return len(extend_paths([["start"]], system, small_twice))


if __name__ == '__main__':
    print(get_paths(open("test.txt"), False))
    print(get_paths(open("test2.txt"), False))
    print(get_paths(open("test3.txt"), False))
    print(get_paths(open("input.txt"), False))
    print(get_paths(open("test.txt"), True))
    print(get_paths(open("test2.txt"), True))
    print(get_paths(open("test3.txt"), True))
    print(get_paths(open("input.txt"), True))
