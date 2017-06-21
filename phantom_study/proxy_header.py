"""
PhantomJS使用代理上网
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
from bs4 import BeautifulSoup as bs

if __name__ == '__main__':
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    # 设置请求头
    desired_capabilities["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
                                                                 "(KHTML, like Gecko) Chrome/15.0.87")
    # 不加载图片信息
    desired_capabilities["phantomjs.page.settings.loadImages"] = False
    # 利用desired_capabilities设置代理
    proxy = webdriver.Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = '121.193.143.249:80'
    proxy.add_to_capabilities(desired_capabilities)

    br = webdriver.PhantomJS()
    br.start_session(capabilities=desired_capabilities)
    br.get('http://ip.chinaz.com/')
    br.set_page_load_timeout(10)
    br.set_script_timeout(5)
    page_source = br.page_source
    soup = bs(page_source, 'lxml')
    # print(page_source)
    center = soup.find('p', {'class': 'getlist pl10'})
    print(center.get_text())
