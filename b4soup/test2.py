import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen

baseUrl="http://www.qu.la/"
html = urlopen("https://www.qu.la/book/16431/6658470.html")
# print(html.read().decode("utf-8"))
html=html.read().decode("utf-8")
soup=BeautifulSoup(html,"lxml")
# print(soup.prettify())
print(soup.title.string)
# print(soup.head)
print(soup.h1.get_text())
content=soup.find( id='content')
[x.extract() for x in content.find_all('script')]
print(content.get_text())

with  codecs.open("filename1.txt", 'a', "utf-8") as fileObj:
    fileObj.write("%s\n" % soup)
