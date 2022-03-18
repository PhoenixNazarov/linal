from base import generate, operate_vec
import numpy as np


# размер пространства
n_v = 3

# basis = generate.generate_basis(n_v)
basis = generate.partial_generate_basis(n_v, 2)
v = generate.gen_lin_comb(basis)


# алгоритм для нахождения координат для неполного базисе
# проверим, что v является линейной комбинацией basis
if not operate_vec.is_lin_comb(basis, v):
    raise 'miss'

# наш basis имеет длину векторов n_v, но в нашем случае допускается dim(basis) != dim(V)
# делаем аналог прополки, только в нашем случае, убираем линейно зависимые координаты векторов базиса
matr_up = np.array([*basis, v]).transpose()
matr_up = np.array([*matr_up, np.zeros(matr_up.shape[1])])
matr_new = []

# по итогу мы добавим только те строчки СЛНУ, которые не являются линейной комбинацией других
# т.к. эти строчки всегда исполнятся, если исполнятся их линейные комбинации, Метод Гаусса
for i in range(len(matr_up) - 1):
    if not operate_vec.is_lin_comb(matr_up[i + 1:], matr_up[i]):
        matr_new = np.array([*matr_new, matr_up[i]])
new_v = matr_new.transpose()[-1].copy()
# print(matr_new)
matr_new = matr_new.transpose()[:-1].transpose()
coords = np.linalg.solve(matr_new, new_v)
print('basis: ', basis)
print('coords: ', coords)
print('vector: ', v)
print('check : ', np.dot(basis.transpose(), coords))