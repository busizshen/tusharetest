#coding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import jieba.analyse
from PIL import Image
import numpy as np
import chardet
from matplotlib.font_manager import FontProperties

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

text_from_file_with_apath = open('best1.txt','r',encoding='utf-8').read()

abel_mask = np.array(Image.open("6.png"))

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)
##解决乱码的关键在于  font_path='./fonts/simhei.ttf'
my_wordcloud = WordCloud(background_color="white",width=1000,height=1000,max_words=800,max_font_size=80,min_font_size=20,font_path='./fonts/simhei.ttf',mask=abel_mask,stopwords=stopwords, margin=10,
               random_state=1).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.title("Custom colors")
plt.title(u"周婷的自我介绍",fontproperties=font_set)
plt.axis("off")
plt.show()