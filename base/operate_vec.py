import numpy as np
from base import generate


def weeding(vectors):
    span = generate.create_span(vectors)
    basis = np.array([])
    for i in range(len(span), 1, -1):
        Sim = span[:i - 1]
        Si = span[:i]
        vi = span[i - 1]
        if np.linalg.matrix_rank(Si) > np.linalg.matrix_rank(Sim):
            basis = np.append(vi, basis).reshape(len(basis) + 1, len(vi))
    return basis


def lin_comb_of_basis(basis, v):
    if not is_lin_comb(basis, v):
        raise 'miss'
    matr_up = np.array([*basis, v]).transpose()
    matr_up = np.array([*matr_up, np.zeros(matr_up.shape[1])])
    matr_new = []
    for i in range(len(matr_up) - 1):
        if not is_lin_comb(matr_up[i + 1:], matr_up[i]):
            matr_new = np.array([*matr_new, matr_up[i]])
    new_v = matr_new.transpose()[-1].copy()
    matr_new = matr_new.transpose()[:-1].transpose()
    return np.linalg.solve(matr_new, new_v)


def is_lin_comb(vectors, v):
    vec_up = np.append(vectors, v).reshape((-1, len(v)))
    return np.linalg.matrix_rank(vectors) == np.linalg.matrix_rank(vec_up)


def is_subset(vec1, vec2):
    for i in vec1:
        if i not in vec2:
            return False
    return True


def spans_equal(span1, span2):
    L1 = weeding(span1)
    L2 = weeding(span2)
    for i in L1:
        if not is_lin_comb(L2, i):
            return False
    return True


def spans_intersection(span1, span2):
    intersection = []
    for i in span1:
        if is_lin_comb(span2, i):
            intersection.append(i)
    return np.array(intersection)


def dim(basis):
    return np.linalg.matrix_rank(basis)

