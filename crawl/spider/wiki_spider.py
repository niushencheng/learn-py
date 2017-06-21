from urllib import request, parse
from python.logging.my_log import MyLog
import string

if __name__ == '__main__':
    log = MyLog()
    login_data = parse.urlencode({
        'code': 'a537d66ea8*e45a391601031708aa297',
        'username': '1497492837',
        'password': '84ec9640701f5adc2e6b6864066bf360'
    })
    url = 'http://localhost:8080/api/login'
    try:
        resp = request.urlopen(url, login_data.encode('utf-8'))
    except Exception as e:
        log.info("发生异常... %s" %e)
    else:
        print(resp.read().decode('utf-8'))
