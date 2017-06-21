import pandas as pd
import numpy as np


class TD(list):
    def __getitem__(self, num):
        print("invoke... %s" % num)


if __name__ == '__main__':
    print(id(123123))
    print(id(123123))
    print(id(123123))
    print(id(123123))
