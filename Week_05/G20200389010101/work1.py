import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
import jieba.analyse
from os import path

dir = path.dirname(__file__)
text = open(path.join(dir, 'bwbj1.txt'),encoding='utf-8').read()
user_dict=r'dict.txt'
jieba.load_userdict(user_dict)

stop_words=r'stop.txt'
jieba.analyse.set_stop_words(stop_words)

tfidf = jieba.analyse.extract_tags(text,
topK=15,
withWeight=False)

print(tfidf)
file = open('bwbj.txt','w')
for i in range(len(tfidf)):
  s = str(tfidf[i]).replace('[','').replace(']','')
  s = s.replace("'",'').replace(',','') +'\n'
  file.write(s)
file.close()
print("����ؼ���")


cizu = open(path.join(dir, 'bwbj.txt'),encoding='GBK').read()
background_Image = np.array(Image.open(path.join(dir, 'shaor.png')))
img_colors = ImageColorGenerator(background_Image)
wc = WordCloud(
  width = 600,      #Ĭ�Ͽ��
  height = 200,     #Ĭ�ϸ߶�
  margin = 2,       #��Ե
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = background_Image,      #����ͼ��,��������ͼƬ���ƣ�����Ҫ����
  color_func = None,
  max_words = 200,  #��ʾ���Ĵʻ���
  stopwords = None, #ֹͣ�����ã���������ͼʱ��Ҫ����
  random_state = None,
  background_color = '#ffffff',#������ɫ���ã�����Ϊ������ɫ�����磺white����16������ֵ��
  font_step = 1,
  font_path='msyh.ttf',
  mode = 'RGB',
  regexp = None,
  collocations = True,
  normalize_plurals = True,
  contour_width = 0,
  colormap = 'viridis',#matplotlibɫͼ�����Ը������ƽ�������������
  contour_color = 'Blues',
  repeat = False,
  scale = 2,
  min_font_size = 10,
  max_font_size = 200)

wc.generate_from_text(cizu)
# ����ͼƬɫ���ñ���ɫ
wc.recolor(color_func = img_colors)
# ��ʾͼ��
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# �洢ͼ��
wc.to_file('love.png')
plt.show()