from base import generate, operate_vec
import numpy as np
import random

# подмножество S является подпространством, когда оно замкнуто относительно + и *
V = generate.generate_V(5)
S = generate.generate_vectors(2, 5)

# проверим +: S + S -> S
for i in range(100):
    v = sum([x * random.randint(1, 10) for x in S])
    if not operate_vec.is_lin_comb(S, v):
        # S - не подпространство V
        break
else:
    print('S + S -> S')

# проверим *: K * S -> S
for i in range(100):
    v = generate.gen_lin_comb(S) * i
    if not operate_vec.is_lin_comb(S, v):
        # S - не подпространство V
        break
else:
    print('K * S -> S')


