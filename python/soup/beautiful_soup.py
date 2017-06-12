from bs4 import BeautifulSoup as bs

soup = bs(open('text.html', 'r', encoding='utf8'), 'lxml')
soup.prettify()
tag = soup.find('header',{'class':'header'})
print(tag.get_text().strip())
