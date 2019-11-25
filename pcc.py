import numpy as np


def djk(m: np.ndarray, deb: int):
    n = len(m)
    r = np.arange(n)
    p = np.zeros(n).astype(bool)
    d = np.array([10000 for i in r])
    d[deb] = 0
    while 0 in p:
        a = (d + np.array([10000 for i in r])*p).argmin()
        p[a] = True
        for b in r[p == False]:
            d[b] = min(d[b], d[a] + m[a, b])
    return d


if __name__ == "__main__":
    mat = np.zeros((5,5))
    line = 1
    print(djk(mat, line))
