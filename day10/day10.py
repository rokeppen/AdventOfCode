from statistics import median
from functools import reduce


def get_score(file):
    dic_corr = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
    dic_comp = {'(': 1, '[': 2, '{': 3, '<': 4}
    corr_score, comp_score, stack = 0, [], []
    for line in file:
        for char in list(line.strip()):
            if char in dic_corr.keys():
                if stack.pop() != dic_corr[char][0]:
                    corr_score += dic_corr[char][1]
                    stack.clear()
                    break
            else:
                stack.append(char)
        if len(stack) != 0:
            comp_score.append(reduce(lambda x, y: x*5+dic_comp[y], stack[::-1], 0))
            stack.clear()
    return corr_score, median(comp_score)


if __name__ == '__main__':
    print(get_score(open("test.txt")))
    print(get_score(open("input.txt")))
