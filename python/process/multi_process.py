from multiprocessing import Pool
from urllib import request


def getUrl():
    resp = request.urlopen("http://www.baidu.com")
    print(resp.read().decode('utf-8'))


if __name__ == '__main__':
    p = Pool(2)
    p.apply_async(getUrl)
    p.apply_async(getUrl)
    p.close()
    p.join()
