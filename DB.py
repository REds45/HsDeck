import pymongo
import settings



class DBClient():
    def __init__(self,name):
        '''
        :param name:数据库表的名字
        '''
        self.client=pymongo.MongoClient(settings.DATABASEURI)
        self.db=self.client[settings.DB_NAME]
        self.collection=self.db[name]

    def __del__(self):
        self.client.close()

class Deck_DB(DBClient):
    def __init__(self):
        super().__init__(settings.DECK_COLLECTION_NAME)

    def count_total_decks(self):
        '''
        :return:返回数据库中套牌的总数量
        '''
        return self.collection.count()
    def get_all_deck(self):
        '''
        :return:返回数据库中所有套牌的信息
        '''
        return self.collection.find()

    def save_deck(self,item):
        '''
        ::保存套牌信息到数据库
        '''
        self.collection.save(item)
        print('保存成功',item)

    def drop_deck(self):
        self.collection.delete_many({})


class Article_DB(DBClient):
    def __init__(self):
        super().__init__(settings.ARTICLE_COLLECTION_NAME)
    def get_all_article(self):
        '''
        :return:返回数据库中的文章
        '''
        return self.collection.find()


    def save_article(self,item):
        self.collection.update({'articleID':item['articleID']},{'$set':item},True)
        print (item,'保存成功')
















