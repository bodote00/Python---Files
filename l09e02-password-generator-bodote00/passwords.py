import itertools
import string

def password_generator(length):
    """Returns an iterator, which generates every possible passwords made out of (low) letters and digits."""
    return itertools.product(string.digits + string.ascii_lowercase, repeat=length)