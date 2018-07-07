import requests
import json
from DB import Article_DB

# 获取最新30篇文章的ID
def get_article_list():
    count = 1
    list = []
    starturl = 'https://www.iyingdi.cn/feed/list/seed/v2?web=1&seed=2&system=web'
    rep = requests.get(starturl)
    idlist = json.loads(rep.text)
    for feed in idlist['feeds']:
        list.append(feed['feed']['sourceID'])

    while count < 2:
        count += 1
        lastid = idlist['feeds'][-1]['feed']['id']
        url = 'https://www.iyingdi.cn/feed/list/seed/v2?id={}&web=1&seed=2&system=web'.format(lastid)
        rep = requests.get(url)
        idlist = json.loads(rep.text)
        for feed in idlist['feeds']:
            list.append(feed['feed']['sourceID'])
    return list


# 通过ID访问每篇文章的ID如果其中有套牌信息 则提取
def get_deck_by_api(list):
    for id in list:
        url = 'https://www.iyingdi.cn/article/{}'.format(id)

        response = requests.get(url)
        try:
            article = json.loads(json.loads(response.text)['article']['content'])
            decks = []
            for i in article:
                if (i['type'] == 'deckCode'):
                    item = {}
                    item['name'] = i['deckname']
                    item['code'] = i['code']
                    item['imgurl'] = i['deckIcon']
                    decks.append(item)
            if decks != []:
                dict = {
                    'articleNmae':json.loads(response.text)['article']['title'],
                    'articleID': id,
                    'articleUrl': 'https://www.iyingdi.cn/web/article/hearthstone/{}'.format(id),
                    'decks': decks
                }
                yield dict
        except KeyError:
            print(id, '错误，请确认是否有此文章')


def run_spider():
    mongodb = Article_DB()
    for i in get_deck_by_api(get_article_list()):
        mongodb.save_article(i)

if __name__=='__main__':
    run_spider()





