from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

movie = db.movies.find_one({'title':'매트릭스'})

print(movie['star'])

star = movie['star']

movies = list(db.movies.find({'star':star}))

for mv in movies:
    print(mv['title'])
