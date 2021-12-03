from statistics import mode
import numpy as np

def get_product():
    values = np.array([list(x.strip()) for x in open("input.txt", "r")])
    gamma = ''.join(mode(values[:, i]) for i in range(len(values[0])))
    epsilon = gamma.replace('1', '2').replace('0', '1').replace('2', '0')
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    print(get_product())
