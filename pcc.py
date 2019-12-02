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


def chemin(ch, a, b):
    """
    retourne le chemin de a vers b
    :param ch: vecteur ch de djk
    :param a: start
    :param b: end
    :return: liste d'arettes (tuple)
    """
    o: list = []
    while a != b:
        o.append((a, ch[a]))
        a = ch[a]
    return o


def af(ch: np.ndarray, m: np.ndarray, i: int, deb: int):
    """
    affichage du chemin entre i et deb avec le poid
    :param ch: vecteur ch de djk
    :param m: matrice
    :param i: start
    :param deb: stop
    :return: str
    """
    return "".join([f"{c[0]} =[{m[c]}]=> " for c in chemin(ch, i, deb)]) + str(deb)


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
    mat = abs(mat)
    _d, _ch = djk(mat, line)
    print(_d)
    print(_ch)
    print(af(_ch, mat, 0, line))
