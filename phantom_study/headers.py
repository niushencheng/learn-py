"""
selenium设置自定义请求头
"""
from selenium import webdriver


def init_phantomjs_driver(*args, **kwargs):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Connection': 'keep-alive'
               }

    desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
    for key, value in headers.items():
        desired_capabilities['phantomjs.page.customHeaders.{}'.format(key)] = value

    desired_capabilities[
        'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

    driver = webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)
    driver.start_session(capabilities=desired_capabilities)
    return driver


def main():
    service_args = [
        '--proxy=127.0.0.1:9999',
        '--proxy-type=http',
        '--ignore-ssl-errors=true'
    ]

    # driver = init_phantomjs_driver(service_args=service_args)
    driver = init_phantomjs_driver()

    driver.get('http://cn.bing.com')
    print(driver.page_source)


if __name__ == '__main__':
    main()
