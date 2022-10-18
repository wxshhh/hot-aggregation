import os

import jieba
import numpy as np
import pandas as pd
import re
import wordcloud
from collections import Counter
import matplotlib.pyplot as plt


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
    data = get_data(['data/Weibo(2022,10,15).csv', 'data/Tieba(2022,10,15).csv', 'data/Zhihu(2022,10,15).csv',
                     'data/Bilibili(2022,10,15).csv'])
    data = process_data(data)
    # counter = Counter(data)
    # top = [word[0] for word in counter.most_common(30)]
    wc = wordcloud.WordCloud(width=1400, height=1400,
                             background_color='white',
                             mode='RGB',
                             font_path=r'C:\Windows\Fonts\simfang.ttf',
                             max_words=500,
                             max_font_size=150,
                             relative_scaling=0.6,  # 设置字体大小与词频的关联程度为0.4
                             random_state=50,
                             scale=2
                             ).generate(" ".join(data))
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭x,y轴
    plt.show()  # 显示
