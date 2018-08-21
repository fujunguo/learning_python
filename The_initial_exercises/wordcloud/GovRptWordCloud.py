import jieba
import wordcloud
from scipy.misc import imread
mask = imread('chinamap.jpg')

f = open('新时代中国特色社会主义.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(
		# 指定字体为微软雅黑
		font_path = 'MSYH.TTC',
		# 指定词云图片的高度、宽度以及背景色
		width=1000, height=700, background_color='white',
		# 指定最大显示词数和图片样式
		max_words=50, mask=mask
		)
w.generate(txt)
w.to_file('grwordcloud.png')