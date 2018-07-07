import ArticleSpider,DeckSpiders
import DB


deckDb=DB.Deck_DB()

def open_spider():
    deckDb.drop_deck()
    ArticleSpider.run_spider()
    DeckSpiders.run_spider()









