#coding:utf-8
import matplotlib,matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba,codecs
with codecs.open(r'D:\PycharmProjects\tusharetest\b4soup\filename1.txt',  encoding='utf-8') as f:
    text_from_file_with_apath =f.read()

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['font.family'] = 'sans-serif'
    # plt.rcParams['axes.unicode_minus'] = False
    # zhfont1 = matplotlib.font_manager.FontProperties(fname='D:\英雄时刻\simsunb.ttf')
    # plt.legend(prop=zhfont1)
    # coding:utf-8
    my_wordcloud = WordCloud(font_path="D:\英雄时刻\msyhbd.ttc").generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()