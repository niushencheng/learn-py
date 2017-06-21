import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            print('text: %s' % text)
            return func(*args, **kw)

        return wrapper

    return decorator


@log('exec')
def now():
    print('now time')


if __name__ == '__main__':
    now()
