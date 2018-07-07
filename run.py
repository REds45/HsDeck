import ArticleSpider,DeckSpiders
import DB
import time
import web

deckDb=DB.Deck_DB()
web.run_app()


while True:
    deckDb.drop_deck()
    ArticleSpider.run_spider()
    DeckSpiders.run_spider()
    time.sleep(21600)


