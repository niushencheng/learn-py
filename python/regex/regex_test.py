import re

if __name__ == '__main__' :
    t = '19:05:30'
    m = re.match(
        r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
        t)
    # print(m.groups())
    s = '11'
    res = re.search(r'^[a-zA-Z0-9][a-zA-Z_0-9]{,6}$', s)
    # print(res.string)

    r = re.match(r'^[\u4e00-\u9fa5]+$','你妈嗨')
    # print(r.string)
    print(re.compile(r'^[\u4e00-\u9fa5]+$').match('你妈嗨').string)
