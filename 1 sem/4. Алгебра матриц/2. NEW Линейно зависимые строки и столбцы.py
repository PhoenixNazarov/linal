from base import generate, operate_vec
import numpy as np
import random

# Можем вырезать строки из столбцов
A = generate.generate_V(size = 3, ln = 10)[2:]
B = operate_vec.weeding(A)

Stolb = A.transpose()

print(operate_vec.is_lin_comb(Stolb, A[:-4].transpose()))
print(operate_vec.is_lin_comb(Stolb, A[1:-1].transpose()))


# база строк,
print(B)
