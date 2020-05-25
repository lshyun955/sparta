from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

def getStarFromTitle(title):
    star = db.movies.find_one({'title':title})['star']
    return star
    
def getTitleFromStar(star):
    stars = getStarFromTitle(star)
    movies = list(db.movies.find({'star':stars}))
    titles = []
    for title in movies:
        titles.append(title['title'])
    return titles

for title in getTitleFromStar('매트릭스'):
    print(title)



#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

