import ArticleSpider,DeckSpiders
import DB
import time

deckDb=DB.Deck_DB()
while True:
    deckDb.drop_deck()
    ArticleSpider.run_spider()
    DeckSpiders.run_spider()
    time.sleep(21600)


