import numpy as np

INF = 100


def djk(m: np.ndarray, deb: int):
    n = len(m)
    r = np.arange(n).astype(int)
    p = np.zeros(n).astype(bool)
    d = INF * np.ones(n).astype(int)
    d[deb] = 0
    ch = np.zeros(n).astype(int)
    while 0 in p:
        a = np.where(p, INF, d).argmin()
        p[a] = True
        for b in r[p == False]:
            if d[b] > d[a] + m[a, b]:
                d[b] = d[a] + m[a, b]
                ch[b] = a + 1
    return d, ch


if __name__ == "__main__":
    mat = np.array(
        [
            [0, -3, 0, 3, 0],
            [-3, 0, 0, 2, 4],
            [0, 0, 0, 0, 1],
            [3, 2, 0, 0, -4],
            [0, 4, 1, -4, 0]
        ]
    ).astype(int)
    line = 2
    mat = np.where(mat == 0, INF, mat)
    print(djk(mat, line))
