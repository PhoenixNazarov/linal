from base import generate, operate_vec
import numpy as np
import random

# Линейное (аффинное) многообразие - множество {x + x0 | x ∈ L} L - подпространство x0 - некая точка

# линейные многообразия совпадают:
# 1. L1 = L2
# 2. x0-y0 ∈ L1


L1 = generate.partial_generate_basis(5, 2)
L2 = np.array([generate.gen_lin_comb(L1), generate.gen_lin_comb(L1)])
assert operate_vec.spans_equal(L1, L2)

x = generate.gen_lin_comb(L1)
y = generate.gen_lin_comb(L2)
assert operate_vec.is_lin_comb(L1, x-y)

LM1 = L1 + x
LM2 = L2 + y

# L1 + x0 = L2 + y0 -> условия
# v = x + x0 = y + y0
assert operate_vec.spans_equal(LM1, LM2)
# x = 0 -> v = x0 = y + y0 -> x0 - y0 ∈ L2
assert operate_vec.spans_equal(np.array([x]), LM2)
# работает и в обратную сторону, поэтому x0 - y0 ∈ (L1 ∩ L2)
assert operate_vec.spans_equal(np.array([x - y]), operate_vec.spans_intersection(L1, L2))
# x + x0 = y + y0 -> x - y0 + x0 = y ∈ L2
# x0 - y0 ∈ L2, y ∈ L2 -> x ∈ L2

# условия -> LM1 = LM2
# v = x + x0
# v = (x0 - y0) ∈ L2 + x ∈ L1
# x ∈ L2 -> v ∈ L 2
# L2 = {y + y0} = {x + x0}



