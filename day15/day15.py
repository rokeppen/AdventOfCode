import numpy as np
from collections import defaultdict
from heapq import heappop, heappush


def lowest_risk(file, miss=1):
    grid, start = np.genfromtxt(file, delimiter=1), (0, 0)
    xm, ym = grid.shape
    to_do, origin, best, guess = [(0, start)], dict(), defaultdict(lambda: np.inf), defaultdict(lambda: np.inf)
    best[start], guess[start] = 0, xm * miss + ym * miss - 2
    while len(to_do):
        c = heappop(to_do)[1]
        if c == (xm * miss - 1, ym * miss - 1):
            risk = 0
            while c != start:
                risk += (grid[c[0] % xm, c[1] % ym] + c[0] // xm + c[1] // ym - 1) % 9 + 1
                c = origin[c]
            return risk
        for n in [(c[0] + 1, c[1]), (c[0], c[1] + 1), (c[0] - 1, c[1]), (c[0], c[1] - 1)]:
            if 0 <= n[0] < xm * miss and 0 <= n[1] < ym * miss:
                new_guess = best[c] + (grid[n[0] % xm, n[1] % ym] + n[0] // xm + n[1] // ym - 1) % 9 + 1
                if new_guess < best[n]:
                    origin[n], best[n] = c, new_guess
                    guess[n] = new_guess + xm + ym - n[0] - n[1]
                    if n not in to_do:
                        heappush(to_do, (guess[n], n))


if __name__ == "__main__":
    print(lowest_risk("test.txt"))
    print(lowest_risk("input.txt"))
    print(lowest_risk("test.txt", 5))
    print(lowest_risk("input.txt", 5))
