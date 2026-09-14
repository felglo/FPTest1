import numpy as np


def pauli_x():
    return np.array([[0, 1], [1, 0]])


def pauli_y():
    return np.array([[0, -1j], [1j, 0]])


def pauli_z():
    return np.array([[1, 0], [0, -1]])
