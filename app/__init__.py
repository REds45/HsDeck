from flask import  Flask

app=Flask(__name__)
app.config['DEBUG']=True


from . import yingdi
from . import box_article