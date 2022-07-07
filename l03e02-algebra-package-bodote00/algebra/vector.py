def dot_product(vector_1, vector_2):
    """Scalar sum"""
    result = 0
    for number_1, number_2 in zip(vector_1, vector_2):
        result += (number_1 * number_2)
    return result
