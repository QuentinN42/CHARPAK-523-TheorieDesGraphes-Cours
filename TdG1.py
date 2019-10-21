import numpy as np
import math

n: int = int(input("n = "))
m = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        v = 2
        while v not in [0, 1]:
            v = int(input(f"m[{i},{j}] = "))
            if v not in [0, 1]:
                print("value must be 0 or 1")
            else:
                m[i, j] = v

print(m)

di = sum(m)
do = sum(m.transpose())
d = di + do

for i in range(n):
    print(f"s{i+1} : di = {di[i]} do = {do[i]}")
