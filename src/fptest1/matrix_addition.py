import numpy as np


def matrix_sum(matrices):
    if not matrices:
        raise ValueError("matrices must contain at least one matrix")

    if not all(isinstance(matrix, np.ndarray) for matrix in matrices):
        raise TypeError("matrices must contain NumPy arrays")

    result = matrices[0].copy()
    for matrix in matrices[1:]:
        result = result + matrix

    return result
