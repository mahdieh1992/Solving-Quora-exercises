#سنجایش
def decorator_builder(validator):
    def decorator_fun(func):
        def wrapper_func(*args, **kwargs):
            if validator(*args,**kwargs):
                return func(*args,**kwargs)
            return 'error'
        return wrapper_func
    return decorator_fun


def non_negative_value(value):
    return value >= 0

@decorator_builder(non_negative_value)
def square_number(number):
    return  number ** 0.5

print(square_number(-4))