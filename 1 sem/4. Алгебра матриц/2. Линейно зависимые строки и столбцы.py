from base import generate, operate_vec
import numpy as np
import random

L_first = generate.partial_generate_basis(5, ln = 2)
L = generate.create_span(np.array([L_first[0]]), ln = 5, zero = False)

# красивый print

print('наша матрица:')
for i in L_first:
    print(i, '<- линейно независимые строки')
for i in L[2:]:
    print(i)
"""
row = str(L[-1])[1:-1].split()
for i in range(len(row)):
    row[i] = f'*'.ljust(len(row[i]))
print(f'{" ".join(row)}')
row = str(L[-1])[1:-1].split()
for i in range(len(row)):
    f = ''
    if i < len(L_first):
        f = '=0'
    row[i] = f'b{i}{f}'.ljust(len(row[i]))
print(f'[{" ".join(row)}]')
row[0] = " " * (len(row[-1]) // len(row))
for i in range(1, len(row)):
    row[i] = f'+'.center(len(row[i]) + len(row[i]) // len(row))
print(f'{" ".join(row)}')
print('='.center(len(str(L).split('\n')[0])))
print(str(np.array([*L, np.zeros(L.shape[1])])).split('\n')[-1][1:-1])
"""

# нахождение нулевой нетривиальной комбинации для строк
basis = operate_vec.weeding(L)
b = np.zeros(L.shape[0])
for i in L:
    if i in basis:
        continue
    t = operate_vec.lin_comb_of_basis(basis, i)
    v = i
    break
else:
    assert False

for i in range(len(L)):
    if all(L[i] == v):
        b[i] = -1
for j in range(len(basis)):
    for i in range(len(L)):
        if all(L[i] == basis[j]):
            b[i] = t[j]

# нахождение нулевой нетривиальной комбинации для столбцов
L_ = L.transpose()
basis = operate_vec.weeding(L_[2:])
c = np.zeros(L_.shape[0])
for i in L_[2:]:
    if i in basis:
        continue
    t = operate_vec.lin_comb_of_basis(basis, i)
    v = i
    break
else:
    assert False

for i in range(len(L_)):
    if all(L_[i] == v):
        c[i] = -1
for j in range(len(basis)):
    for i in range(len(L_)):
        if all(L_[i] == basis[j]):
            c[i] = t[j]

print("a:")
print(b)
print(c)
# sum(sum(L.transpose() * b)) == 0

# первые k строк - лин независимые, остальные k-2 выражаются через них
# L(k+l) = sum(Ail * L(i))
# A(k+l)j = sum(Ail * Aij)

# рассмотрим для столбцов:
#
"""
линейно зависимая система
[1, 0, 2] a0
[1, 1, 0] a1
[2, 1, 2] a2 = (1, 2) b00*a0 + b01*a1 
[3, 1, 4] a3 = (2, 1) b10*a0 + b11*a1
нулевая комбинация = (-2, 2, 1)


отрезки столбцов:
[1, 0, 2] a0 - база строк
[1, 1, 0] a1 - база строк
[2, 1, 2] a2 = (1, 2) b00*a0 + b01*a1 



нулевая комбинация = (-2, 2, 1)





нулевая комбинация = (0, 1, -1)
хотим доказать
[1, 0, 2] = 
[2, 1, 2] = 



"""