from base import generate, operate_vec
import numpy as np


def is_generative(_basis, _span):
    for i in _span:
        if not operate_vec.is_lin_comb(_basis, i):
            print(i)
            return False
    return True


def is_linear_dependent(_basis):
    for i in range(len(_basis)):
        basis_without = np.append(_basis[:i], _basis[i + 1:]).reshape(_basis.shape[0] - 1, _basis.shape[1])
        v = _basis[i]
        if operate_vec.is_lin_comb(basis_without, v):
            return False
    return False


def create_basis():
    return operate_vec.weeding(generate.generate_V(5))


vec = generate.generate_vectors(5, 3)
basis = operate_vec.weeding(vec)

# порождающая, можно представить любой вектор в базисе:
if is_generative(basis, vec):
    print('basis - порождающая система: Любой вектор из vec можно представить в векторах из basis')
else:
    print(f'basis - не порождающая система: k-й вектор нельзя представить в basis')

# линейно независимая, любой вектор в базисе нельзя представить через другие вектора в базисе
if not is_linear_dependent(basis):
    print('basis - линейно независимая система: Любой вектор из basis, нельзя представить через другие вектора из basis')
else:
    print(f'basis - линейно зависимая система: k-й вектор из basis, можно представить через другие вектора из basis')


# 1. — порождающая и линейно независимая система
# 2. — максимальная (по числу элементов) линейно независимая систем
# 3. — минимальная (по числу элементов) порождающая система


# 1 -> 2
# basis_n - порождающая и линейно независимая
# basis_m - линейно независимая
basis_n = create_basis()
basis_m = create_basis()

# докажем, что в basis_m и basis_n нельзя добавить хоть какой вектор
# потому что это нарушит условие линейной независимости
# если никакой вектор нельзя добавить, значит система максимально линейно независимая

# для этого, будем добавлять элементы из basis_m в basis_n и полоть
for i in basis_m:
    check_n = len(basis_n)
    up_vec = np.append(i, basis_n).reshape(-1, basis_n.shape[1])

    if not is_linear_dependent(up_vec): raise 'miss'
    # наша система vi + basis_n линейно зависимая
    # значит после прополки размер этой системы будет <= n
    basis_n = operate_vec.weeding(up_vec)
    if len(basis_n) > check_n:
        raise "miss"

    # при этом вектор vi не будет удален, как и все другие вектора vm, добавленные в basis_n
    # потому что что прополке нашей новой системы (v0, v1 .. vm, u... un) не удалит (v0 ... vm)
    # ведь эти вектора уже линейно независимые, значит будет удален вектор из (u .. un)
    # значит basis_m[:i] ⊂ basis_n, то есть в конечном итоге basis_n превратится в basis_m,
    # todo
    if not operate_vec.is_subset(basis_m[:i], basis_n):
        raise 'miss'
else:
    print('ok 1 -> 2')


# 2 -> 1
# basis - максимально линейно независимая система
# докажем, что basis - порождающая
basis = create_basis()

# максимально линейно независимая - значит, что добавив любой вектор, она станет линейно зависимой
for i in generate.generate_vectors(20, basis.shape[1]):
    # если она становится линейно зависимой, значит для этого вектора есть линейная комбинация
    # следуют, что через basis можно выразить любой вектор из V -> basis - порождающая система
    if not operate_vec.is_lin_comb(basis, i):
        raise 'miss'
else:
    print('ok 2 -> 1')


# 1 -> 3
# basis_n линейно независимая и порождающая
# basis_m порождающая
# докажем, что basis_n минимально порождающая, то есть n <= m
basis_n = operate_vec.weeding(generate.generate_V(5, ln = 5))
basis_m = operate_vec.weeding(generate.generate_V(5, ln = 2))

# для этого пройдемся по vn и будем добавлять их в basis_m
for i in basis_n:
    check_m = len(basis_m)
    up_vec = np.append(i, basis_m).reshape(-1, basis_n.shape[1])
    basis_m = operate_vec.weeding(up_vec)

    # как и в 1 -> 2, мы удалим минимум один вектор
    # значит наша новая система имеет размер <= m
    # в итоге получим подсистему basis_n, которая по размеру <= m
    # значит размер basis_n <= m
    if len(basis_m) < check_m:
        raise 'miss'
else:
    print('ok 1 -> 3')


# 3 -> 1
# basis - минимальная порождающая
basis = operate_vec.weeding(generate.generate_V(5, ln = 5))
# докажем, что она линейно независимая
# от противного, допустим она линейно зависимая, тогда какой-то вектор из basis
# является линейной комбинацией других векторов из basis,
# значит этот вектор можно убрать. А это противоречит тому, что basis минимальная

