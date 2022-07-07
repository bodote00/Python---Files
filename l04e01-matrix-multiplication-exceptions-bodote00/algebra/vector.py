def dot_product(vector_1, vector_2):
    """Scalar sum"""
    if len(vector_1) != len(vector_2):
        raise ValueError(f"ValueError, vectors are not the same length {vector_1}, {vector_2}")
    result = 0
    for number_1, number_2 in zip(vector_1, vector_2):
        result += (number_1 * number_2)
    return result