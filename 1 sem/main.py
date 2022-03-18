import time
import numpy as np


def generator(n, _range):
    def gen_ind():
        for t in range(n):
            for tt in range(n + 1):
                yield t, tt

    cnt = n * n + n
    g = np.array([[_range[0]] * cnt]).reshape((n, n + 1))
    for i in range(cnt ** (_range[1] - _range[0])):
        yield g
        s_ind = gen_ind()
        ind = next(s_ind)
        while ind[1] * n + ind[0] <= n ** 2 - 1:
            g[ind] += 1
            if g[ind] >= _range[1]:
                g[ind] = _range[0]
                ind = next(s_ind)
            else:
                break

    yield np.array([[_range[1] - 1] * cnt]).reshape((n, n + 1))


def gen_izi(n, _range):
    def gen_ind():
        u = 0
        for t in range(n):
            for tt in range(n + 1):
                yield t, tt
                u += 1

    count = (n * n + n)
    g = np.zeros(count).reshape((n, n + 1))
    for i in range((_range[1] - _range[0]) ** count):
        g_ind = gen_ind()
        ind = next(g_ind)
        yield g
        while 1:
            if g[ind] >= _range[1] - 1:
                g[ind] = 0
                ind = next(g_ind)
            else:
                g[ind] += 1
                break


# h = gen_izi(3, (-6, 7))
# for i in range(999999):
#     print(next(h))
# next(h)
# n = 1
# _range = [0, 2]
# for n in range(1, 5):
#     s_generator = generator(n, _range)
#     n1 = time.time()
#     print('next', (n * n + n) ** (_range[1] - _range[0]))
#     for i in range((n * n + n) ** (_range[1] - _range[0])):
#         s = next(s_generator)
#         print(s,i, end = '\n\n')
#         pass
#     time.sleep(1)
import timeit
import time

c = timeit.timeit(lambda : time.sleep(1), number=2)
print(c)
