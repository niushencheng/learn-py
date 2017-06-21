from bs4 import BeautifulSoup as bs
from urllib import request

if __name__ =='__main__':

    try:
        resp = request.urlopen('http://www.baidu.com')
        read = resp.read()
    except Exception as e:
        print(e)
    else:
        print(read)
