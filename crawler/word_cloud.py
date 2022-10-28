import os
import time

import jieba
import numpy as np
import pandas as pd
import re

import snownlp.sentiment
import wordcloud
from crawler.tfidf import TfIdf
from snownlp import SnowNLP
from PIL import Image
import matplotlib.pyplot as plt
import thulac

sentiments = []


def get_data():
    t = time.localtime()
    prefix_path = os.getcwd()[:-7].replace("\\", "/") + "data/"
    suffix_path = "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
    websites = ["Bilibili", "Weibo", "Tieba", "Zhihu"]
    filenames = list(map(lambda website: prefix_path + website + suffix_path, websites))
    data = []
    for file in filenames:
        title_list = pd.read_csv(file)['title'].tolist()
        data.extend(title_list)
    return data


def process_data(data):
    data = re.sub("[^\u4e00-\u9fa5^a-z^A-Z^0-9]", '', ' '.join(data))
    with open("stopwords.txt", "r", encoding="utf-8") as f:
        stopwords = f.read().split("\n")
    # word_list = jieba.cut(data)
    # word_list = SnowNLP(data).words
    cutter = thulac.thulac()
    res = cutter.cut(data)
    word_list = [word[0] for word in res]
    data = [word for word in word_list if word not in stopwords and len(word) != 1]
    tfidf = TfIdf()
    tfidf_values = tfidf.add_corpus(data)
    for dict in tfidf_values:
        for x, y in dict.items():
            # 对wordlist进行过滤，y值越高越严格
            if y <= 3 and x in data:
                data.remove(x)
    return data


def get_senti(data):
    # 收集标题情绪系数并平均得日(周)总体情感系数
    # 0到1之间的浮点数，越靠近1越积极
    senti = [SnowNLP(txt).sentiments for txt in data]
    return senti


if __name__ == '__main__':
    data = get_data()
    data = process_data(data)
    sentiments = get_senti(data)
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
    print("generate wordcloud success!")
