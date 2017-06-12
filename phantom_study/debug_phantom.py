from selenium import webdriver
from python.logging.my_log import MyLog

log = MyLog()

if __name__ == '__main__':
    br = webdriver.PhantomJS()
    br.get('http://localhost:9090')
    print(br.title)
    username = br.find_element_by_name('username')
    password = br.find_element_by_name('password')
    username.clear()
    password.clear()
    username.send_keys('admin')
    password.send_keys('admin')
    submit_ele = br.find_element_by_name('action')
    submit_ele.click()
    print(br.title)
    br.quit()