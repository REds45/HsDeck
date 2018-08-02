from app import app
from multiprocessing import Process
from spiders import async_spider,DeckSpiders
import time


def article_spider():
    while True:
        async_spider.run_spider()
        time.sleep(21600)


def deck_spider():
    while True:
        DeckSpiders.run_spider()
        time.sleep(86400)


def web():
    app.run(host='0.0.0.0', port=80, threaded=True)



if __name__=='__main__':
    deck_process=Process(target=deck_spider)
    article_process=Process(target=article_spider)
    web_process=Process(target=web)

    deck_process.start()
    article_process.start()
    web_process.start()












