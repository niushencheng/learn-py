import itertools

if __name__ == '__main__':
    s = ['a', 'b', 'c']
    for i in itertools.permutations(s, 2):
        print(i)

    print('--------------------------------')
    for i in itertools.combinations(s, 2):
        print(i)

    print('--------------------------------')
    for i in itertools.product(s,repeat = 2):
        print(i)
