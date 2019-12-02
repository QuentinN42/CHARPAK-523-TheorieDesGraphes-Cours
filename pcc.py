import numpy as np

INF = 100


def djk(m: np.ndarray, deb: int):
    n = len(m)
    r = np.arange(n, dtype=int)
    p = np.zeros(n, dtype=bool)
    d = INF * np.ones(n, dtype=int)
    d[deb] = 0
    ch = np.zeros(n, dtype=int)
    while 0 in p:
        a = np.where(p, INF, d).argmin()
        p[a] = True
        for b in r[p == False]:
            if d[b] > d[a] + m[a, b]:
                d[b] = d[a] + m[a, b]
                ch[b] = a
    return d, ch


def af(ch: np.ndarray, m: np.ndarray, i: int, deb: int):
    o: str = ""
    while i != deb:
        o += f"{i} =[{m[i,ch[i]]}]=> "
        i = ch[i]
    return o + str(deb)


if __name__ == "__main__":
    mat = np.array(
        [
            [0, -3, 0, 3, 0],
            [-3, 0, 0, 2, 4],
            [0, 0, 0, 0, 1],
            [3, 2, 0, 0, -4],
            [0, 4, 1, -4, 0]
        ],
        dtype=int)
    line = 2
    mat = np.where(mat == 0, INF, mat)
    _d, _ch = djk(mat, line)
    print(_d)
    print(_ch)
    print(af(_ch, mat, 0, line))
