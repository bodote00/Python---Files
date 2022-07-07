from .vector import dot_product

def new_matrix(shape, fill):
    """Creates new matrix row*column, and fills it with number behind "(row, column)" """
    rows, columns = shape
    result = []
    for _ in range(rows):
      result.append([fill] * columns)  
    return result


def matrix_multiplication(matrix_1, matrix_2):
    """Multiplicates 2 matrixes. Function dot_product from vecotr.py library is applied here."""
    result = []
    for row in matrix_1:
        new_row = []
        for column in zip(*matrix_2):
            new_row.append(dot_product(row, column))
        result.append(new_row)    
    return result


def submatrix(matrix, drop_rows = [], drop_columns = []):
    """Drops user-defined rows and columns"""
    new_matrix = []

    for index_row, row in enumerate(matrix):
        if index_row not in drop_rows:
            my_new_matrix_helper = []
            for index_column, column in enumerate(row) :
                if index_column not in drop_columns:
                    my_new_matrix_helper.append(column)
            if my_new_matrix_helper:
                new_matrix.append(my_new_matrix_helper)
    return new_matrix 
