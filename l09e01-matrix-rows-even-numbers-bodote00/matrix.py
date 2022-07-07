import itertools

def rows_even_numbers(matrix, row_mask):
    """Function takes a matrix, and a row_mask, that defines, which lines shuold be ignored, and which not. 
    Returns an iterator, which produces every even number from matrix, that are compatible with row mask."""
    return itertools.filterfalse(lambda x: x % 2 == 1, itertools.chain.from_iterable(itertools.compress(matrix, row_mask)))
    