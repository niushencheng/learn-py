from multiprocessing import Pool
from urllib import request


def incr_num(url, path):
    print(path)
    resp = request.urlopen(url)
    print(resp.read().decode('utf-8'))


if __name__ == '__main__':
    p = Pool(150)
    for i in range(50):
        p.apply_async(incr_num, args = ('http://localhost:8080/lock', 'path0'))
        p.apply_async(incr_num, args = ('http://localhost:8081/lock', 'path1'))
        # p.apply_async(incr_num, args = ('http://172.18.119.227:8412/lock',))
        # time.sleep(0.1)
    p.close()
    p.join()
