def arithmetic_progression(begin, step, end=None):
    """Creates an arithmetic progression, which includes "begin" and exludes an "end". Differential is defined by a "step". If "end" is not defined, progression is infinite. """

    while end and begin < end or not end:
        yield begin
        begin += step
