from urllib import request
import re

if __name__ == '__main__':
    proxy_handler = request.ProxyHandler({'http': 'http://121.193.143.249:80'})
    # proxy_handler = request.ProxyHandler({'http': 'http://61.221.118.213:80'})
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    req = request.Request('http://www.baidu.com')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    try:
        # response = opener.open('http://www.baidu.com', timeout=3)
        response = request.urlopen(req)
    except Exception as e:
        print('failed %s' %e)
    else:
        res = response.read()
        if re.search(r'baidu.com', res.decode('utf-8')):
            print('success!')
