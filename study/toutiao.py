# coding=utf-8

'''
1、抓取索引页内容
2、抓取详情页内容
3、下载图片保存数据库
4、循环及多线程
'''

import requests
from requests.exceptions import RequestException
from json import loads
from bs4 import BeautifulSoup
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent": user_agent}

def get_onepage_index(i, keywords):
    url = "https://so.toutiao.com/search?"
    data = {
        "offset": i,
        "format": "json",
        "keyword": keywords,
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab"
    }
    try:
        response = requests.get(url, params=data)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('something is wrong!')
        return None


def parse_onepage_index(html):
    # json.loads()用于将str类型的数据转成dict。
    data = loads(html)
    print (data.keys())
    if data and 'data' in data.keys():  ##获取所有的key 值
        for item in data.get('data'):  # get() 函数返回指定键的值，如果值不在字典中返回默认值。
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('wrong url:', url)
        return None


def parsepage(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    print(title)


def main():
    for i in range(1, 2):
        i = str(i * 20)
        html = get_onepage_index(i, '街拍')
        for url in parse_onepage_index(html):
            print(url)
            detailhtml = get_page_detail(url)  # 返回网页文本
            if detailhtml == None:
                pass
            else:
                parsepage(detailhtml)  # bs4去解析


if __name__ == '__main__':
      main()
      result = get_page_detail('http://toutiao.com/group/6596305324645286404/')
      print (result)
