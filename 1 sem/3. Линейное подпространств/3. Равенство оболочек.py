from base import generate, operate_vec
import numpy as np
import random

V = generate.generate_V(5)
L1 = generate.generate_vectors(2, 5)
L2 = generate.generate_vectors(2, 5)

# L1, L2 ⊂ V, L1 != L2
# Ui ∈ L1 не является линейной комбинацией базиса L2 -> Ui не лежит в L2
for i in L1:
    if operate_vec.is_lin_comb(L2, i):
        raise ""
