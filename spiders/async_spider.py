import requests
import json
from DB import Article_DB
import asyncio
import aiohttp

'''
DeckSpiders的异步版本
'''
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


async def get(url):
    #使用aiohttpClient进行异步请求
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    await session.close()
    return result


async def save_item(item):
    mongoDb=Article_DB()
    mongoDb.save_article(item)


async def request(id):
    url = 'https://www.iyingdi.cn/article/{}'.format(id)
    response= await get(url)
    try:
        article = json.loads(json.loads(response)['article']['content'])
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
                'articleNmae': json.loads(response)['article']['title'],
                'articleID': id,
                'articleUrl': 'https://www.iyingdi.cn/web/article/hearthstone/{}'.format(id),
                'decks': decks
            }
            await save_item(dict)
    except KeyError:
        print(id, '错误，请确认是否有此文章')


def run_spider():
    list = get_article_list()
    task = [asyncio.ensure_future(request(id)) for id in list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task))


if __name__=='__main__':
    list=get_article_list()
    task = [asyncio.ensure_future(request(id)) for id in list]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task))








