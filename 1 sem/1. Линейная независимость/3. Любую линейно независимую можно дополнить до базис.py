from base import generate, operate_vec
import numpy as np

# в нашем случае мы рассматриваем линейно независимую систему, но такую, что S != V
# мы хотим доказать, что S можно дополнить до базиса V
V = generate.generate_V(5, ln = 20)
S = operate_vec.weeding(generate.generate_vectors(2, 5))
print('Базис V:')
print(operate_vec.weeding(V))
print('Базис S:')
print(S)

# S != V, S ⊂ М, иначе S - порождающая, следственно S - уже базис
if np.linalg.matrix_rank(V) <= np.linalg.matrix_rank(S):
    raise "miss"

# значит ∃u ∈ V \ span(S)
# S + u - линейно независимая, иначе бы u был линейной комбинацией S
while np.linalg.matrix_rank(V) < np.linalg.matrix_rank(S):
    for i in V:
        if not operate_vec.is_lin_comb(S, i):
            S = np.array([*S, i])

print('Дополненный базис S:')
print(operate_vec.weeding(V))
