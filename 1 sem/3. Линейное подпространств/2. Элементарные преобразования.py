from base import generate, operate_vec
import numpy as np
import random

# элементарные преобразования:
# 1. Добавление нулевого вектора в набор либо его удаление из набора.
# 2. Перестановка произвольных двух векторов системы.
# 3. Умножение произвольного вектора на ненулевой скаляр.
# 4. Замена любого вектора на его сумму с произвольным другим вектором системы
# элементарное преобразование не меняет оболочку

S = generate.generate_vectors(2, 5)

# 1 добавление нулевого вектора не меняет span
if np.linalg.matrix_rank(np.array([*S, np.zeros(S.shape[1])])) != np.linalg.matrix_rank(S):
    raise ''

# 2 перестановка произвольных двух векторов системы не меняет span
S_swap = np.copy(S)
np.random.shuffle(S_swap)
if np.linalg.matrix_rank(S_swap) != np.linalg.matrix_rank(S):
    raise ''

# 3 умножение произвольного вектора на ненулевой скаляр не меняет span
S[0] *= random.randint(1,10)
if np.linalg.matrix_rank(S) != np.linalg.matrix_rank(S):
    raise ''

# 4. замена любого вектора на его сумму с произвольным другим вектором системы
S[0] = S[0] + S[1]
if np.linalg.matrix_rank(S) != np.linalg.matrix_rank(S):
    raise ''
# мы заменили (aV, bU) -> ((aV + cU), bU)
# тогда мы просто изменим координаты всех линейных комбинаций: b' = b - c
# v = aV + vU = V' + b'U = (aV + cU) + (b - c)U = aV + cU + vU - cU = aV + vU
