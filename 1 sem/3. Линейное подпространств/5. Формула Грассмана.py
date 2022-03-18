from base import generate, operate_vec
import numpy as np
import random

dim = operate_vec.dim

# dim(L1 + L2) = dim L1 + dim L2 − dim(L1 ∩ L2)
V = generate.generate_basis(5)
L1 = np.array([V[0], V[1], V[3]])
L2 = np.array([V[0], V[1], V[4]])
# пересечение: (V0, V1)
# сумма: (V0, V1, V3, V4)

# L1 ∩ L2 != 0
L_int = operate_vec.spans_intersection(L1, L2)
if len(L_int) == 0:
    raise ""

# мы можем дополнить базис пересечения до базиса L1 и L2
# тогда dim L1 = w + m, dim L2 = w + n
# L1 ∩ L2 = (W1 .. Wk)
# L1 = (W1 .. Wk; U1 .. Um)
# L2 = (W1 .. Wk; V1 .. Vn)
w = len(L_int)
m = len(L1) - w
n = len(L2) - w

# мы хотим доказать, что dim l1+l2 = dim L3 = w + m + k = dim L1 + dim L2 − dim(L1 ∩ L2)
# то есть: L1 + L2 = L3 = (W1 .. Wk; U1 .. Um; V1 .. Vn)
L3 = operate_vec.weeding(np.array([*L_int, *L1]))
L3 = operate_vec.weeding(np.array([*L3, *L2]))

# докажем, что L3 порождающая
# любой вектор из L1 или L2 представим в L3
# V ∈ L1 -> представим в (W1 .. Wk; U1 .. Um) -> представим в (W1 .. Wk; U1 .. Um; V1 .. Vn)
# V ∈ L2 -> представим в (W1 .. Wk; V1 .. Vn) -> представим в (W1 .. Wk; U1 .. Um; V1 .. Vn)
for i in np.array([*L1, *L2]):
    if not operate_vec.is_lin_comb(L3, i):
        raise ""


# докажем, что L3 линейно независимая
# рассмотрим нулевую линейную комбинацию суммы: aW + bU + cV = 0
W = L_int
U = operate_vec.spans_intersection(L3, L1)
V = operate_vec.spans_intersection(L3, L2)

# aW + bU = -cV
# aW + bU ∈ L1, cV ∈ L2

# L1 ∩ L2 - L'
# значит aW, bU, cV ∈ L1 ∩ L2 -> можем разложить aW, bU по базису (W1 .. Wk)
# aW + bU ∈ (W1 .. Wk) -> a'W + 0U
#   раскладывается только так, потому что aW + bU ∈ L', а L' ⊂ L1,
#   aW + bU ∈ (W1 .. Wk)
#   aW + bU ∈ (W1 .. Wk; U1 .. Um)
#   мы уже можем разложить aW + bU по (W1 .. Wk)
#   значит координаты (W1 .. Wk; U1 .. Um) будут равны (a'1 .. a'k; 01 .. 0m)
#   по теореме о единственности разложения по базису, другого варианта не существует

# получилось: a'W + oU = -cV
# a'W + cV = 0
# a'W + cV ⊂ L2, значит единственное разложение - (01 .. 0k; 01 .. 0n)
# значит aWi + bU + cV = 0
# раскладывается единственным способом = 0Wi + 0U + 0V = 0
# следственно (W1 .. Wk; U1 .. Um; V1 .. Vn) линейно независима

if any(operate_vec.lin_comb_of_basis(L3, np.zeros(L3.shape[1])) != np.zeros(L3.shape[0])):
    raise ""
