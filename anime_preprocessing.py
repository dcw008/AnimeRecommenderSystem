
# coding: utf-8

# In[84]:


import csv
from collections import defaultdict

toJson = open('anime.json', 'w')
count = 0
toJson.write('[')
with open('anime.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == 'anime_id':
            continue
        
        
        genre_list = row[2].split(',')
        genres = '['
        for g in range(len(genre_list)):
            genre = genre_list[g].replace(" ", "")
            genres += '"'
            genres += genre
            if g != len(genre_list)-1:
                genres += '",'
            else:
                genres += '"]'
                
        rating = row[5]
        if rating == '':
            rating = -1
        
        if (count != 0):
            toJson.write(',\n')
        
        toJson.write('{ "anime_id" : "' + str(row[0]) + '", "name" : "' + str(row[1]) + '", "genre" : '
              + str(genres) + ', "type" : "' + str(row[3]) + '", "episodes" : "'
              + str(row[4]) + '", "rating" : ' + str(rating) + ', "members" : ' + str(row[6]) + '}')
        
        count += 1
    
toJson.write(']')
toJson.close()


# In[129]:


import json

rating = json.load(open('rating_200k.json'))
animedata = json.load(open('anime.json'))


# In[130]:


from collections import defaultdict

watched = defaultdict(set)
rating_by_anime = defaultdict(list)    # list of animes with rating that each user watched

for entry in rating:
    watched[entry['user_id']].add(entry['anime_id'])
    
    anime_dict = {}
    anime_dict['anime_id'] = entry['anime_id']
    anime_dict['rating'] = entry['rating']
    rating_by_anime[entry['user_id']].append(anime_dict)


# In[131]:


genres = set()    # set of all genres
genreCount = defaultdict(int)     # count of each genre

for entry in animedata:
    for genre in entry['genre']:
        genres.add(genre)
        genreCount[genre] += 1


# In[132]:


anime_view_dict = defaultdict(list)     # list of users that watched certain anime

for entry in rating:
    anime_id = entry['anime_id']
    user_id = entry['user_id']
    anime_view_dict[anime_id].append(user_id)


# In[133]:


genre_by_anime = defaultdict(list)      # list of animes corresponding to certain genre

for entry in animedata: 
    for genre in entry['genre']:
        genre_by_anime[genre].append(entry['anime_id'])

