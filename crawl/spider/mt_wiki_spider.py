"""
使用webdriver爬取美团wiki文档
"""
from selenium import webdriver
from python.logging.my_log import MyLog


class WikiSpider(object):
    def __init__(self) -> None:
        self.urls = ['https://wiki.sankuai.com/pages/viewpage.action?pageId=777954005']


if __name__ == '__main__':
    log = MyLog()
    desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities[
        'chrome.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4753.400'

    # for key, value in headers.items():
    #     desired_capabilities['chrome.page.customHeaders.{}'.format(key)] = value
    cookie_arr = [
        {
            "domain": ".sankuai.com",
            "expirationDate": 1655141668.849253,
            "hostOnly": False,
            "httpOnly": False,
            "name": "skmtutc",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "1eKKqR6YZ7otMWnl6K7gpK6v6dJhLZin9LiG626SbF7uodrvroBb91bHzb8L6+67XgFJNleaHg2lHKgHlw0t2g==-JT9/y5jS5JbBEHUtFWFHEL3FiF4=",
            "id": 1
        },
        {
            "domain": "wiki.sankuai.com",
            "hostOnly": True,
            "httpOnly": True,
            "name": "JSESSIONID",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": False,
            "session": True,
            "storeId": "0",
            "value": "605DFA7E1E7E307AD94B4CE12C519D45",
            "id": 2
        },
        {
            "domain": "wiki.sankuai.com",
            "hostOnly": True,
            "httpOnly": False,
            "name": "sticky-uuid4",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": False,
            "session": True,
            "storeId": "0",
            "value": "\"61e86daa-28f9-4fa6-864a-7f67df18b356:10.32.115.33\"",
            "id": 3
        }
    ]

    br = webdriver.Chrome()
    # br.get('http://localhost:9090')
    br.set_page_load_timeout(10)
    br.set_script_timeout(5)
    br.implicitly_wait(10)
    br.get('https://wiki.sankuai.com/pages/viewpage.action?pageId=777954005')

    for cookie in cookie_arr:
        br.add_cookie(cookie)

    log.info("已有的cookie：" + str(br.get_cookies()))
    log.info("add cookie success!")
    br.get('https://wiki.sankuai.com/pages/viewpage.action?pageId=777954005')
    print("再次获取时的cookie：%s" % br.get_cookies())
    page_source = br.page_source
    print(page_source)
