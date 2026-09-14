def matrix_product(matrices):
    if not matrices:
        raise ValueError("matrices must contain at least one matrix")

    result = matrices[0]
    for matrix in matrices[1:]:
        result = result @ matrix
    return result
