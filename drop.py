import pymongo
def drop_all_item():
    client = pymongo.MongoClient('localhost')
    db = client['yingdi']
    list = ['hearthstone', 'hsArticle']
    for i in list:
        collection = db[i]
        collection.delete_many({})


