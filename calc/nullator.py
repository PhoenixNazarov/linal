from fractions import Fraction
from prettytable import PrettyTable
from base.operate_vec import *

BORDERS = True

# from
V = np.array([
    [-2, 1, -8, -4],
    [4, 1, -16, 4],
    [3, 3, -15, 0],
    [0, -3, 4, -10],
])

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
