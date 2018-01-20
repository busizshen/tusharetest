import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen
def getBook(book):
    baseUrl="https://www.qu.la/"
    bookUrl="https://www.qu.la/book/%s/"%(book)
    html = urlopen(bookUrl)
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
        # html = urlopen("https://www.qu.la/book"+url.a['href'])
        with  codecs.open("filenameUrl%s.txt"%(book), 'a', "utf-8") as fileObj:
            fileObj.write("%s,%s\n" % (url.a['href'],url.get_text()))
# bsObj=BeautifulSoup(html,"lxml")
# divdd=bsObj.find('div', id_='list')
# # print("----------",divdd)
#
# ulList=divdd.find_all("dd")
# for ul in ulList:
#     print(ul.href)
getBook("16431")