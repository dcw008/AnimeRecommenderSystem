
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


# In[5]:


import json

rating = json.load(open('rating_200k.json'))
animedata = json.load(open('anime.json'))


# In[35]:


from collections import defaultdict

watched = defaultdict(set)
rating_by_user = defaultdict(list)    # list of animes with rating that each user watched
rating_by_anime = defaultdict(list)    # list of dictionary with anime as keys, and containing user and ratings


for entry in rating:
    watched[entry['user_id']].add(entry['anime_id'])
    
    anime_dict = {}
    if (entry['rating'] != '-1'):
        anime_dict['anime_id'] = entry['anime_id']
        anime_dict['rating'] = entry['rating']
        rating_by_user[entry['user_id']].append(anime_dict)
    
    user_dict = {}
    if (entry['rating'] != '-1'):
        user_dict['rating'] = entry['rating']
        user_dict['user_id'] = entry['user_id'] 
        rating_by_anime[entry['anime_id']].append(user_dict)
    
    
    
    
    
   


# In[7]:


genres = set()    # set of all genres
genreCount = defaultdict(int)     # count of each genre

for entry in animedata:
    for genre in entry['genre']:
        genres.add(genre)
        genreCount[genre] += 1


# In[8]:


anime_view_dict = defaultdict(list)     # list of users that watched certain anime

for entry in rating:
    anime_id = entry['anime_id']
    user_id = entry['user_id']
    anime_view_dict[anime_id].append(user_id)


# In[9]:


genre_by_anime = defaultdict(list)      # list of animes corresponding to certain genre

for entry in animedata: 
    for genre in entry['genre']:
        genre_by_anime[genre].append(entry['anime_id'])


# In[10]:





# In[87]:


average_rating_byuser = defaultdict(float)

for user in rating_by_user:
    
    animes = rating_by_user[user]
    total = 0
    count = 0
    
    for anime in animes:    
        total += float(anime['rating'])
        count += 1
            
    if count != 0:
        average_rating_by_user[user] = total / count
        
        


# In[89]:


beta_u = defaultdict(float)

total = 0
count = 0
for user in average_rating_by_user:
    total += average_rating_by_user[user]
    count += 1
    
total_average_rating_byuser = total / count

for user in average_rating_by_user:
    beta_u[user] = average_rating_by_user[user] - total_average_rating_byuser


# In[90]:


anime_average_rating = defaultdict(float)      # average rating of each anime

for entry in animedata:
    if (entry['rating'] != -1 and entry['rating'] != 0):
        anime_average_rating[entry['anime_id']] = entry['rating']


# In[91]:


beta_i = defaultdict(float)

total = 0
count = 0
for anime in anime_average_rating:
    total += anime_average_rating[anime]
    count += 1
    
total_average_rating_byanime = total / count

for anime in anime_average_rating:
    beta_i[anime] = anime_average_rating[anime] - total_average_rating_byanime


# In[92]:


alpha = anime_average_rating

