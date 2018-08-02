from flask import  Flask

app=Flask(__name__)
app.config['DEBUG']=True


from . import web
from . import box_article