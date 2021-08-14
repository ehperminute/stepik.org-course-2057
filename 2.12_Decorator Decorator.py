It's quite annoying to write a trivial wrapper around the inner function each time we write a decorator. Implement a makeDecorator decorator that works like that:

@makeDecorator
def introduce(f, *args, **kwargs):
  print(f.__name__)
  return f(*args, **kwargs)

# introduce is now a decorator

@introduce
def id(*whatever):
  return whatever


print(*(id(40, 2)))

>>> id
40 2

def make_decorator(decorator):
    def decorate(f):
        def inner(*args, **kwargs):
            return decorator(f, *args, **kwargs)
        return inner
    return decorate
