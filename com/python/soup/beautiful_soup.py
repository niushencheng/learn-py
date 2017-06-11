from bs4 import BeautifulSoup as bs

soup = bs(open('text.html', 'r', encoding='utf8'), 'lxml')
soup.prettify()
