import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen

baseUrl="http://www.qu.la/"
html = urlopen("http://www.qu.la/book/32645/1752029.html")
# print(html.read().decode("utf-8"))
html=html.read().decode("utf-8")
soup=BeautifulSoup(html,"lxml")
# print(soup.prettify())
print(soup.title.string)
# print(soup.head)
print(soup)
# print(soup.dd.a['href'])
# print(soup.find_all('dd'))
with  codecs.open("filename1.txt", 'a', "utf-8") as fileObj:
    fileObj.write("%s\n" % soup)
# bsObj=BeautifulSoup(html,"lxml")
# divdd=bsObj.find('div', id_='list')
# print("----------",divdd)

# ulList=divdd.findAll("dd")
# for ul in ulList:
#     print(ul.href)