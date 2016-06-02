def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function: ", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper


def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look:", arg1, arg2)
        function_to_decorate(arg1, arg2)
        return
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is ", first_name, last_name)


@document_it
@square_it
def add_ints(a, b):
    return a + b


@makebold
@makeitalic
def say():
    return "hello"


if __name__ == "__main__":
    print(say())
    print("=" * 10)
    add_ints(3, 5)
    print("=" * 10)
    print_full_name("Peter", "Venkman")
