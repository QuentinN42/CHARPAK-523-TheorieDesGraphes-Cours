import numpy as np


def int_bool(m: np.ndarray) -> np.ndarray:
    return np.array([np.array([int(bool(x)) for x in l]) for l in m])


def chem(m: np.ndarray) -> np.ndarray:
    n = len(m)
    k = 2
    m = m @ m
    while k < n:
        m = m @ m
        k = k ** 2
    return int_bool(m)


def warshall(m: np.ndarray) -> np.ndarray:
    r = range(len(m))
    for k in r:
        for i in r:
            for j in r:
                m[i, j] = m[i, j] or m[i, k] * m[k, j]
    return m


if __name__ == "__main__":
    s = 5
    M = np.random.randint(2, size=(s, s))
    M = int_bool(M + np.identity(s))
    print(chem(M), "\n\n", warshall(M))
