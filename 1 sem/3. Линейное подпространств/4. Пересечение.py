from base import generate, operate_vec
import numpy as np
import random

L1 = generate.generate_vectors(2, 5)
L2 = generate.generate_vectors(2, 5)

# L1 != L2
if not operate_vec.spans_equal(L1, L2):
    raise ""

# V ∈ L1 и V ∈ L2 -> V ∈ L1 ∩ L2
# V ∈ L1 -> линейная комбинация L2 -> V ∈ L1 ∩ L2
intersection = []
for i in L1:
    if operate_vec.is_lin_comb(L2, i):
        intersection.append(i)
intersection = np.array(intersection)

# V', U' ∈ L1 ∩ L2 -> V'+U' ∈ L1 и V
V_new = generate.gen_lin_comb(intersection)
U_new = generate.gen_lin_comb(intersection)
comb = generate.gen_lin_comb(np.array([V_new, U_new]))
if not (operate_vec.is_lin_comb(L1, comb) and operate_vec.is_lin_comb(L2, comb)):
    raise ""
#
