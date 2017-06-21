
if __name__ == '__main__':
    dic = {'name': 'zhangsan',
           'age': 18,
           'sex': 'female'}
    test = {'hehe':'hehe'}

    for key, value in dic.items():
        test['{}'.format(key)] = value

    print(test)
