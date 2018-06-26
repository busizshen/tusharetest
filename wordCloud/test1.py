#coding=utf-8
import jieba.analyse
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt


class wc:
    def __init__(self, txt_file, img_file, font_file):
        self.f = open(txt_file,encoding='utf-8')

        self.txt = self.f.read()
        self.f.close()
        self.tags = jieba.analyse.extract_tags(self.txt, topK=100)
        # topK说白了就是返回几个关键词
        self.text = ' '.join(self.tags)  # 把分词链接起来，加空格因为英文靠空格分词
        self.img = imread(img_file)
        self.wc = WordCloud(font_path=font_file, background_color='white', max_words=100, mask=self.img, max_font_size=50)
        ###直接在这里进行猜###
        # font_path指的是字体文件路径，因为wordcloud自带的字体不支持中文所以我们要指定一个字体文件，否者输出的图片全是框框
        # background_color 默认是黑色　我设置成白色
        # max_words最大显示的词数
        # mask 背景图片
        # max_font_size　最大字体字号
        self.word_cloud = self.wc.generate(self.text)


    def show_wc(self):
        # img_color = ImageColorGenerator(self.img)
        plt.imshow(self.word_cloud)
        # 可以通过 plt.imshow(self.wc.recolor(color_func=img_color))使图片颜色跟字体颜色一样
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
    mywc = wc('test2.txt', 'webImg2.jpg', 'c:\windows\\fonts\simsun.ttc')
    mywc.show_wc()
