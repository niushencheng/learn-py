from functools import partial


def func(self, strs):
    print(strs)


class Obj(object):
    def __init__(self):
        self.a = 1


if __name__ == '__main__':
    obj = Obj()
    obj.func = partial(func, obj)
    obj.func('test str')
