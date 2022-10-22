import os
import time

import jieba
import numpy as np
import pandas as pd
import re
import wordcloud
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image


def get_data(files):
    data = []
    for file in files:
        title_list = pd.read_csv(file)['title'].tolist()
        data.extend(title_list)
    return data


def process_data(data):
    data = re.sub('[^\u4e00-\u9fa5]+', '', ' '.join(data))
    with open("stopwords.txt", "r", encoding="utf-8") as f:
        stopwords = f.read().split("\n")
    word_list = jieba.lcut(data)
    data = [word for word in word_list if word not in stopwords and len(word) != 1]
    return data


if __name__ == '__main__':
    t = time.localtime()
    prefix_path = os.getcwd()[:-7].replace("\\", "/") + "data/"
    suffix_path = "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
    websites = ["Bilibili", "Weibo", "Tieba", "Zhihu"]
    filenames = list(map(lambda website: prefix_path + website + suffix_path, websites))
    data = get_data(filenames)
    data = process_data(data)
    mask = np.array(Image.open(os.getcwd()[:-7].replace("\\", "/") + "frontend/public/ji1.png"))
    wc = wordcloud.WordCloud(width=1400, height=1400,
                             background_color='white',
                             mask=mask,
                             mode='RGB',
                             font_path=r'C:\Windows\Fonts\simfang.ttf',
                             max_words=500,
                             max_font_size=150,
                             # relative_scaling=0.6,  # 设置字体大小与词频的关联程度
                             random_state=50,
                             scale=2
                             ).generate(" ".join(data))
    path = os.getcwd()[:-7].replace("\\", "/") + "frontend/src/assets/ciyun.png"
    wc.to_file(path)
    # plt.imshow(wc)  # 显示词云
    # plt.axis('off')  # 关闭x,y轴
    print("词云生产成功")
