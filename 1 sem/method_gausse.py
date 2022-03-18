import random
import numpy as np


def shuffle_rows(m, v):
    buf = np.array([*m.transpose(), v]).transpose()
    perm = [i for i in range(len(buf))]
    random.shuffle(perm)
    new_m = np.array([])
    new_v = []
    for i in range(len(v)):
        g = perm[i]
        new_m = np.array([*new_m, buf[g][:-1]])
        new_v.append(buf[g][-1])
    return new_m, new_v


def shuffle_lin_comb(m, v):
    if len(m) <= 1:
        return m, v

    while 1:
        new_m = np.copy(m)
        new_v = v.copy()
        for i in range(1):
            new_m, new_v = shuffle_rows(new_m, new_v)
            # new_m = shuffle_columns(new_m)
            for i in range(20):
                ind1 = random.randint(0, len(m) - 2)
                ind2 = random.randint(ind1 + 1, len(m) - 1)
                mn = random.randint(-2, 2)
                new_m[ind1] += new_m[ind2]
                new_v[ind1] += new_v[ind2]
        return new_m, new_v


print(shuffle_lin_comb(np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]), [1, 1, 1]))
