import numpy as np
from fractions import Fraction
from prettytable import PrettyTable

BORDERS = False

# from
V = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])

# to
L = [
    np.array([
        [4 / 3, 1],
        [4 / 3, -1],
        [1, 0],
        [0, 1]
    ]),
    np.array([
        [5 / 3, 4 / 3],
        [4 / 3, -4 / 3],
        [1, 0],
        [0, 1]
    ])
]


def mprint(name, matrix):
    p = PrettyTable()
    p.title = name
    for i in range(len(matrix)):
        _matr = []
        for j in range(len(matrix[0])):
            _matr.append(str(Fraction(matrix[i][j]).limit_denominator()))
        p.add_row(_matr)
    print(p.get_string(header=False, border=BORDERS))

# SOLVE
V2 = L[0]
for i in L[1:]:
    V2 = np.column_stack((V2, i))
assert np.linalg.matrix_rank(V2) == np.linalg.matrix_rank(V)

# T V->V2 = V2' * V
T = np.dot(np.linalg.inv(V2), V)

mprint("V'", V2)
print('*')
mprint("T", T)
print('=')
mprint("E", V)

print('\n')

# find proctors
Pls = []
index = 0
print('\n----PROCTORS----')
for i in range(len(L)):
    print(f'P{i+1}: E -> L{i+1}')
    Pi = np.array(V.copy()).transpose()
    Tl = T[index: index + len(L[i][0])]
    index += len(L[i][0])
    mprint(f"L{i+1}", L[i])
    print('*')
    mprint(f"TL{i+1}", Tl)
    print('=')
    P = np.dot(L[i], Tl)
    mprint(f'P{i}', P)
    Pls.append(P)
    print()


# CHECK
print('\n----CHECK----')
mprint('sum', sum(Pls))

# ANSWER
print('\n----ANSWER----')
for i in range(len(Pls)):
    mprint(f'P{i+1}', Pls[i])

# CUSTOM
print("\n----CUSTOM----")
p1 = Pls[0]
p2 = Pls[1]
mprint("sum a", -7 * p1 + -6 * p2)

