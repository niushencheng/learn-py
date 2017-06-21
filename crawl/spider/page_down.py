from selenium import webdriver

if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get('http://www.baidu.com')
    js='document.body.scrollTop =0'
    br.execute_script(js)
    br.quit()
