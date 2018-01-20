import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen


        # print("stdout:%s"%line)
def gettext(url):
    baseUrl="https://www.qu.la%s"%(url)
    print(baseUrl)
    html = urlopen(baseUrl)
    # print(html.read().decode("utf-8"))
    html=html.read().decode("utf-8")
    soup=BeautifulSoup(html,"lxml")
    # print(soup.prettify())
    print(soup.title.string)
    with codecs.open("filename1.txt", 'a', "utf-8") as fileObj:
        fileObj.write("%s\n" % soup.title.string)
    # print(soup.head)
    print(soup.h1.get_text())
    content=soup.find( id='content')
    [x.extract() for x in content.find_all('script')]
    print(content.get_text())
    with codecs.open("filename1.txt", 'a', "utf-8") as fileObj:
        fileObj.write("%s\n" % content.get_text())


with codecs.open("filenameUrl16431.txt",encoding="utf-8") as file:
    for line in file.readlines():
        url=line.split(",")
        if len(url)>1:
            print(url[0])
            gettext(url[0])