#چیراکسی؟

# this is custom Execption
class ExceptionProxy(Exception):
    def __init__(self,message,function):
        self.message = message
        self.function = function
        super().__init__(message)       

# functions for send custom Execption
def g():
    return 1 / 0

def f():
    pass      

# if func excute Exeption proxy return ok else return err 
def transform_exceptions(funcs: list) -> list[ExceptionProxy]:
    result_funcs = []
    for func in funcs: 
        try:
            func()
            result_funcs.append(ExceptionProxy('ok!',func))
        except Exception as err:
            message = str(err)
            result_funcs.append(ExceptionProxy(message,func))
    return result_funcs

exceptions_info = transform_exceptions([g,f])
for item in exceptions_info:
     print(f"function: {item.function}")
     print(f"function name: {item.function.__name__}")
     print(f"message: {item.message}")
     print("-" * 10)