import requests
from bs4 import BeautifulSoup
import json
from DB import Deck_DB

'''
爬取旅法师营地 炉石传说卡族库
'''

#获取套牌列表
def get_deck_list():
    url = 'https://www.iyingdi.cn/hearthstone/set/list/web'
    data = {'token': '',
            'page': '0',
            'size': '8',
            'deck_size': '0',
            'total': '0'
            }
    rep=requests.post(url, data=data).text
    list=json.loads(rep)
    for i in list['sets']:
        id = i['set']['id']
        url = 'https://www.iyingdi.cn/hearthstone/set/{}/decks?size=200'.format(id)
        yield requests.get(url).text

#解析套牌
def parse_deck(deck_list):
    list=json.loads(deck_list)['list']
    for i in list:
        item = {}
        item['imgurl'] = i['deck']['deckImg']
        item['name'] = i['deck']['name']
        item['code'] = i['deck']['code']
        item['form'] = i['deck']['format']
        yield item


def run_spider():
    mongo = Deck_DB()
    #先清空数据库中保存的卡组信息
    mongo.drop_all_item()
    for list in get_deck_list():
        for deck in parse_deck(list):
            mongo.save_deck(deck)



if __name__=='__main__':
    run_spider()