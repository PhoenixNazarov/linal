from base import generate
import numpy as np

vectors = generate.generate_vectors(3, 3)
span = generate.create_span(vectors)
basis = np.array([])
print('Наше множество векторов: ')
print(span)
print()

# заметим, что S0 ⊆ S1 ⊆ S2 ⊆ S3 ... ⊆ Sm
# !⊂ - принадлежит, но не равно
# если S2 !⊂ Sm, то S1 !⊂ Sm, S2 !⊂ Sm...
# значит вектор vm не является линейной комбинацией для S[:m-1]
#
# пример с конкретным вектором
# если S2 !⊂ S3, то вектор v3 не является линейной комбинацией для S[:2]
# так же уже имеющиеся вектора в базисе линейно независимые с v3
# поэтому это условие дает нам возможность добавить v3 в набор базисных векторов

# пройдем по S[:i-1] и S[i]
for i in range(len(span), 1, -1):
    Sim = span[:i - 1]
    Si = span[:i]
    vi = span[i - 1]

    # S[:i-1] ⊆ S[:i]
    # если S[:i-1] ⊂ S[:i] и не S[:i-1] ⊆ S[:i]
    # то вектор vi не является линейной комбинацией других векторов из S[:i-1] -> добавляем его в базис
    if np.linalg.matrix_rank(Si) > np.linalg.matrix_rank(Sim):
        basis = np.append(basis, vi).reshape(len(basis) + 1, len(vi))

print('Найденный базис:')
print(basis)
