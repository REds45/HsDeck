import json

import requests

'''
爬取炉石盒子APP中卡组推介相关文章

'''

DECK_API='http://lushi-app.gameyw.netease.com/gzdata/lushicarddata.json'
ARTICLE_API='http://lushi-app.gameyw.netease.com/xiaomei/fetch_news_list/6063__20__%E5%8D%A1%E7%BB%84__1.html'
detail='http://lushi-app.gameyw.netease.com/negs_interface/fetchNews/viewData.j?sid=&data=P8jJEXKkoPpXIrAGdJA%253D&aid={}&render_my=0'


def get_article_list():
    result=requests.get(ARTICLE_API).text
    news_list=json.loads(result)['news_list']
    return news_list

def get_article_content(id):
    url=detail.format(id)
    result=requests.get(url).text
    news=json.loads(result)['news']
    return news



