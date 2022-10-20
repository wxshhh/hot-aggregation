import pprint
import re
import time
import os
import sys

import pandas as pd

import requests
from bs4 import BeautifulSoup
from model.topic import *

# 默认图片字段
default_img_url = "https://www.bing.com/images/search?q=%E6%9A%82%E6%97%A0%E5%9B%BE%E7%89%87&FORM=IQFRBA&id=9D8F61B67D0BBB8A38F68E86DC0CA5D1166B381D"
# 默认描述字段
default_desc = "无"


def get_page(url, is_json=False):
    """
    根据传入url，获取对应页面的BeautifulSoup解析结果
    :param url:
    :param is_json: 当该字段为True事，说明求情的url返回的结果为json格式，无需再用BeautifulSoup解析
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
    }
    response = requests.get(url, headers=headers)
    if is_json:
        return response.text
    html = BeautifulSoup(response.text, features="lxml")
    return html


def get_zhihu():
    """
    获取当天的知乎热搜
    id, title, desc, image_url, link, heat
    :return:
    """
    data = []
    url = 'https://www.zhihu.com/billboard'
    soup = get_page(url)
    script_text = soup.find("script", id="js-initialData").get_text()
    rule = r'"hotList":(.*?),"guestFeeds"'
    result = re.findall(rule, script_text)
    temp = result[0].replace("false", "False").replace("true", "True")
    hot_list = eval(temp)
    id = 1
    for topic in hot_list:
        title = topic['target']['titleArea']['text']
        desc = topic['target']['excerptArea']['text']
        if desc in ("", "-"):
            desc = default_desc
        image_url = topic['target']['imageArea']['url']
        if image_url is "":
            image_url = default_img_url
        heat = topic['target']['metricsArea']['text']
        link = topic['target']['link']['url']
        zhihu = Zhihu(id, title, desc, image_url, link, heat)
        id = id + 1
        data.append(zhihu)
    return data


def get_weibo():
    """
    获取当天的微博热搜
    id, title, link
    :return:
    """
    data = []
    url = 'https://weibo.cn/pub/'
    soup = get_page(url)
    topic_list = soup.find_all("div", class_="c")
    id = 1
    for topic in topic_list:
        title = topic.find("a").text[1:-1]
        link = "https://s.weibo.com/weibo?q=%23" + title + "%23"
        weibo = Weibo(id, title, link)
        id = id + 1
        data.append(weibo)
    return data


def get_tieba():
    """
    获取当天的贴吧热搜
    id, title, desc, image_url, link, heat
    :return:
    """
    data = []
    url = 'https://tieba.baidu.com/hottopic/browse/topicList?res_type=1'
    soup = get_page(url)
    topic_list = soup.find_all("li", class_="topic-top-item")
    id = 1
    for topic in topic_list:
        title = topic.find('a', class_='topic-text').text
        desc = topic.find('p', class_='topic-top-item-desc').text
        if desc in ("", "-"):
            desc = default_desc
        image_url = topic.find('img', class_='topic-cover').attrs['src']
        if image_url is "":
            image_url = default_img_url
        heat = topic.find('span', class_='topic-num').text
        link = topic.find('a', class_='topic-text').attrs['href']
        tieba = Tieba(id, title, desc, image_url, link, heat)
        id = id + 1
        data.append(tieba)
    return data


def get_bilibili():
    """
    获取当天的b站热搜
    id, title, describe, image_url, link, author, view, reply, favorite, coin, share
    :return:
    """
    data = []
    url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
    result = get_page(url, is_json=True)
    temp = result.replace("false", "False").replace("true", "True").replace("null", "None")
    topic_list = eval(temp)["data"]["list"]
    id = 1
    for topic in topic_list:
        title = topic["title"]
        desc = topic["desc"]
        if desc in ("", "-"):
            desc = default_desc
        image_url = topic["pic"]
        if image_url is "":
            image_url = default_img_url
        link = topic["short_link"]
        author = topic["owner"]["name"]
        view = topic["stat"]["view"]
        like = topic["stat"]["like"]
        reply = topic["stat"]["reply"]
        favorite = topic["stat"]["favorite"]
        coin = topic["stat"]["coin"]
        share = topic["stat"]["share"]
        bilibili = Bilibili(id, title, desc, image_url, link, author, view, like, reply, favorite, coin
                            , share)
        id = id + 1
        data.append(bilibili)
    return data


def save(data):
    """
    将获取到的data保存为csv文件格式：站点(yyyy,MM,dd).csv
    :param data:
    :return:
    """
    idx = 0
    for item in data[0].__dir__():
        if item.startswith("__"):
            break
        idx = idx + 1
    attrs = data[0].__dir__()[:idx]
    attrs[0] = "rank"
    df = pd.DataFrame(columns=attrs)
    for item in data:
        df.loc[len(df.index)] = item.to_list()
    print(df.head())
    t = time.localtime()
    filename = os.getcwd()[:-7] + type(data[0]).__name__ + "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
    if os.path.exists(filename):
        print("文件已存在！！！")
        return
    df.to_csv(filename)
    print("保存成功！！！")


if __name__ == '__main__':
    weibo = get_weibo()
    zhihu = get_zhihu()
    bilibili = get_bilibili()
    tieba = get_tieba()
    data = [weibo, zhihu, bilibili, tieba]
    for item in data:
        save(item)
    # print()
    pass
