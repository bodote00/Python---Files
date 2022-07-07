def debug(function):
    """Entering arguments and result of function are printed here"""
    def wrappper(*args, **kwargs):
        args_list = []
        kwargs_list = []
        for arg in args:
            args_list.append(repr(arg))
        for key, value in kwargs.items():
            kwargs_list.append(f"{key}={repr(value)}")
        list_of_arguments = ", ".join(args_list + kwargs_list)
        result = function(*args, **kwargs)
        print(f"Calling: {function.__name__}({list_of_arguments})")
        print(f"Result: {result}")
        return result
    return wrappper