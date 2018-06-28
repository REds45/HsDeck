from flask import Flask
from flask import render_template
from DB import Deck_DB,Article_DB
app=Flask(__name__)
app.config['DEBUG']=True

deckdb=Deck_DB()
articledb=Article_DB()

@app.route('/')
def index():
    data={
        'count':deckdb.count_total_decks()
    }
    return render_template('index.html',data=data)

@app.route('/all')
def get_all():
    decks=deckdb.get_all_deck()
    return render_template('deck.html',decks=decks)

@app.route('/article')
def Article():
    articles=articledb.get_all_article()

    return render_template('article.html',articles=articles)
app.run(host='0.0.0.0',port=80,threaded=True)