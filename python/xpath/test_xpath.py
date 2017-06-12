from scrapy.selector import Selector

with open("/Users/tinker/Workspaces/python/learn-py/xml/super.xml", 'r') as fp:
    body = fp.read()

txt = Selector(text=body).xpath('//birthday').extract()
print(txt)
