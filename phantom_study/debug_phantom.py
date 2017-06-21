from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
from python.logging.my_log import MyLog

log = MyLog()

if __name__ == '__main__':
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    # 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
    desired_capabilities["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (" \
                                                                "KHTML, like Gecko) Chrome/15.0.87 "
    log.info('设置浏览器User-Agent')
    # 不载入图片，爬页面速度会快很多
    desired_capabilities["phantomjs.page.settings.loadImages"] = False
    log.info('关闭浏览器图片加载')
    br = webdriver.PhantomJS()
    br.start_session(desired_capabilities)
    br.get('http://www.baidu.com')
    br.set_page_load_timeout(5)
    br.set_script_timeout(5)
    log.info('等待爬取内容...')
    print(br.title)
    print(br.get_cookies())
    br.quit()
