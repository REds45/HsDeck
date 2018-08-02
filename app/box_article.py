from . import app
from spiders.box_app_spider import get_article_list,get_article_content
from flask import render_template

@app.route('/box_article')
def box_article():
    news_list=get_article_list()
    return render_template('box_article.html',list=news_list)

@app.route('/box_article/<id>')
def box_article_detail(id):
    news=get_article_content(id)
    return render_template('box_detail.html',news=news)