from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

def getStarFromTitle(title):
    star = db.movies.find_one({'title':title})['star']
    return star
    
def upadateTitleFromStar(title):
    stars = getStarFromTitle(title)
    db.movies.update_many({'star':stars},{'$set': {'star':0}})

upadateTitleFromStar('클래식')




#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

