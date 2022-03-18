import numpy as np
from base import operate_vec


def vector_set(count_vector, len_vector):
    return np.random.random((count_vector, len_vector))


def generate_vectors(count_vector, len_vector):
    return np.random.random((count_vector, len_vector))


def gen_lin_comb(vectors):
    v = np.random.random(vectors.shape[0])
    return np.dot(vectors.transpose(), v)


def create_span(vectors, ln=10, zero=True):
    if zero:
        vectors = np.append(np.zeros(vectors.shape[1]), np.array(vectors)).reshape(-1, vectors.shape[1])
    for i in range(ln):
        vectors = np.append(vectors, gen_lin_comb(vectors)).reshape(-1, vectors.shape[1])
    return vectors


def generate_V(size, ln=0):
    vectors = np.array([np.zeros(size)])
    while np.linalg.matrix_rank(vectors) < size:
        new_v = np.random.random(size)
        if not operate_vec.is_lin_comb(vectors, new_v):
            vectors = np.append(vectors, new_v).reshape(-1, size)
    return create_span(vectors, ln)


def generate_basis(size):
    v = generate_V(size)
    return operate_vec.weeding(v)


def partial_generate_basis(size, ln=2):
    vectors = np.array([])
    while len(vectors) < ln:
        new_v = np.random.random(size)
        if not operate_vec.is_lin_comb(vectors, new_v):
            vectors = np.array([*vectors, new_v])
    return vectors

