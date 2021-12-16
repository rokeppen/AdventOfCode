import numpy as np
from collections import defaultdict
from heapq import heappop, heappush


def lowest_risk(file, miss=1):
    grid, start = np.genfromtxt(file, delimiter=1), (0, 0)
    xm, ym = grid.shape
    to_do, best, guess = [(0, start)], defaultdict(lambda: np.inf), defaultdict(lambda: np.inf)
    best[start], guess[start] = 0, xm * miss + ym * miss - 2
    while True:
        x, y = heappop(to_do)[1]
        if (x, y) == (xm * miss - 1, ym * miss - 1):
            return best[x, y]
        for n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if 0 <= n[0] < xm * miss and 0 <= n[1] < ym * miss:
                new_guess = best[x, y] + (grid[n[0] % xm, n[1] % ym] + n[0] // xm + n[1] // ym - 1) % 9 + 1
                if new_guess < best[n]:
                    best[n], guess[n] = new_guess, new_guess + xm + ym - n[0] - n[1]
                    heappush(to_do, (guess[n], n))


if __name__ == "__main__":
    print(lowest_risk("test.txt"))
    print(lowest_risk("input.txt"))
    print(lowest_risk("test.txt", 5))
    print(lowest_risk("input.txt", 5))
