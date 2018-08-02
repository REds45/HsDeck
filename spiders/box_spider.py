import re
from DB import Article_DB
import requests
from bs4 import BeautifulSoup
from urllib import parse

'''
爬取炉石盒子PC端卡组推介相关文章
'''


BASE_URL='http://lushi.163.com'


def get_url_list():
    #获前两页文章的链接
    urls=['http://lushi.163.com/gonglue/',
          'http://lushi.163.com/gonglue_2/']
    list = []
    for url in urls:
        result = requests.get(url).text
        soup = BeautifulSoup(result, 'lxml')
        linklist = soup.select('div.sumnews-item-tt a')
        for a in linklist:
            url = parse.urljoin(BASE_URL, a.get('href'))
            list.append(url)
    return list

def save_itrm(item):
    mongo=Article_DB()
    mongo.save_article(item)

def get_article(url):
    print(url)
    html=requests.get(url).text
    decklist=re.findall('<strong>.*(AA.*?)</strong>',html)
    if decklist:
        dict={
            'from':'炉石传说盒子',
            'articleID':url.split('/')[-2],
            'articleNmae':re.search('<h1 class="article-tt">(.*?)</h1>',html).group(1),
            'articleUrl':url,
            'decks':decklist
        }
        save_itrm(dict)


if __name__=='__main__':
    for url in get_url_list():
        get_article(url)