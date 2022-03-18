from fractions import Fraction
from prettytable import PrettyTable
from base.operate_vec import *

BORDERS = False

# from
F = np.array([
    [-2, 1, -8, -4],
    [4, 1, -16, 4],
    [3, 3, -15, 0],
    [0, -3, 4, -10],
])

G = np.array([
    [11, 10, 8, 7],
    [-16, -17, -8, -12],
    [4, 3, 5, 2],
    [8, 12, 0, 9],
])

P = np.array([
    [6, 2, -2, -1],
    [0, 7, 0, -2],
    [1, 2, 3, -1],
    [1, 2, -2, 4],
])

Q = np.array([
    [0, 2, 1, 1],
    [-6, -7, -2, -2],
    [6, 4, -1, 2],
    [-3, -2, -1, -4],
])

_V = np.array([
    [1, 1, 0, 0],
    [-8, 5, 4, 8],
    [0, 1, 1, -1],
    [6, -3, -3, -5],
])

W = np.array([
    [-8, 3, 10, -9],
    [4, -8, -12, 14],
    [-8, 3, 10, -10],
    [-4, 0, 4, -4],

])

V = W

E = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])

# to
L = [
    np.array([
        [1],
        [0],
        [0],
        [0]
    ]),
    np.array([
        [0],
        [1],
        [0],
        [0]
    ]),
    np.array([
        [0],
        [0],
        [1],
        [0]
    ]),
    np.array([
        [0],
        [0],
        [0],
        [1]
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
    print(p.get_string(header = False, border = BORDERS))


# SOLVE
print('----ANNIHILATOR----')
for i in L:
    print('\n')
    mprint('e', i)

    m = 0
    basis = np.array([])
    while 1:
        V2 = np.linalg.matrix_power(V, m)
        # mprint(f'Generated{m}:', V2)
        m += 1
        va = np.dot(V2, i)
        mprint(f'add{m}:', va)
        s = np.linalg.matrix_rank(basis)
        basis = np.array([*basis, va.transpose()[0]])
        if np.linalg.matrix_rank(basis) == s:
            basis = weeding(basis.transpose()).transpose()
            coeff = np.linalg.solve(basis[:-1].transpose(), basis[-1])
            break
    coeff *= -1
    coeff = np.array([*coeff, 1])
    print("FindCoeff", coeff[::-1])

    add = np.zeros(V.shape)
    for j in range(len(coeff) - 1, -1, -1):
        mprint(f'^{j} coef {coeff[j]}', coeff[j] * np.linalg.matrix_power(V, j))
        add += coeff[j] * np.linalg.matrix_power(V, j)
    mprint(f'final', add)
