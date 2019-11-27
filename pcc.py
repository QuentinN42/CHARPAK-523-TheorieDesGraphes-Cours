import numpy as np

INF = 10000


def djk(m: np.ndarray, deb: int):
    n = len(m)
    r = np.arange(n)
    p = np.zeros(n).astype(bool)
    d = np.array([INF for i in r])
    d[deb] = 0
    while 0 in p:
        a = (d + np.array([INF for i in r]) * p).argmin()
        p[a] = True
        for b in r[p == False]:
            d[b] = min(d[b], d[a] + m[a, b])
    return d


if __name__ == "__main__":
    mat = np.array(
        [
            [0, -3, 0, 3, 0],
            [-3, 4, 0, 0, 0],
            [0, 0, 0, 0, 5],
            [3, 0, 0, 0, -4],
            [0, 4, 1, -4, 0]
        ]
    )
    line = 3
    print(djk(mat, line))
