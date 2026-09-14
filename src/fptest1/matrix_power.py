import numpy as np

def matrix_power(matrix, power):
    if power < 0:
        raise ValueError("power must be a non-negative integer")
    if power == 0:
        return np.eye(matrix.shape[0], dtype=matrix.dtype)
    result = matrix
    for _ in range(1, power):
        result = result @ matrix
    return result