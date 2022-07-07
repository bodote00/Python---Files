import time as t

def delay(seconds=1):
    """Add a user defined delay before executing program, or adds default delay, which is set to 1 second."""
    def delay_wrapper(function):
        def wrapper(*args, **kwargs):
            t.sleep(seconds)
            return function(*args, **kwargs)
        return wrapper
    return delay_wrapper 