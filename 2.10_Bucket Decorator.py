Make a bucket(<...>) parameterized decorator

The decorator accepts any number of arguments, both positional and keyword, the type does not matter. When the decorated function is called, its result is printed to the standard output along with the decorator arguments in the following format:

(<tuple of positional decorator arguments>, <dictionary of keyword decorator arguments>, <function's returned value>)

 

Expected behaviour:

@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
def id(x):
  return x

>>> id(42)
((1, 2, 3, [1, 2, 3], 'one', 'two', 'three'), {'two': 2, 'one': 1, 'three': 3}, 42)



@bucket()
def id2(x):
  return x

>>> id2(42)
((), {}, 42)

def bucket(*args, **kwargs):
    def wrapper(f):
        def inner(x):
            return (args, kwargs, f(x))
        return inner
    return wrapper
