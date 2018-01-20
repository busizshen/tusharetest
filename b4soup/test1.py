import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen

baseUrl="https://www.qu.la/"
html = urlopen("https://www.qu.la/book/16431/")
# print(html.read().decode("utf-8"))
html=html.read().decode("utf-8")
soup=BeautifulSoup(html,"lxml")
# print(soup.prettify())
print(soup.title.string)
# print(soup.head)
print(soup)
# print(soup.dd.a['href'])
# print(soup.find_all('dd'))
tt = soup.find_all('dd')
for url in tt:
    print(url.a['href'])
    html = urlopen("https://www.qu.la/book"+url.a['href'])
# with  codecs.open("filename.txt", 'a', "utf-8") as fileObj:
#     fileObj.write("%s\n" % soup)
# bsObj=BeautifulSoup(html,"lxml")
# divdd=bsObj.find('div', id_='list')
# # print("----------",divdd)
#
# ulList=divdd.find_all("dd")
# for ul in ulList:
#     print(ul.href)