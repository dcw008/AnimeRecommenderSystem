
import json
from collections import defaultdict
rating_data = []

#read the rating data from file
with open('rating_100k.json','r') as input:
    rating_data = json.load(input)

#read anime data from file

anime_data = []
with open('anime.json', 'r') as input:
    anime_data = json.load(input)

print(len(anime_data))


#get rating based on types of show
type_count = defaultdict(int)
total_rating_by_type = defaultdict(float)

for anime in anime_data:
    type = anime['type']
    rating = anime['rating']
    if(type != ''):
        type_count[type] += 1
        total_rating_by_type[type] += rating

avg_rating_by_type = {}
for rating in type_count:
    avg = (total_rating_by_type[rating] * 1.0) / type_count[rating]
    avg_rating_by_type[rating] = avg
print(avg_rating_by_type)
# {'Movie': 6.159105621805784, 'TV': 6.660242936361237, 'OVA': 6.31730594986408, 'Special': 6.501056085918853, 'Music': 5.588995901639343, 'ONA': 5.572731411229138}

min_mem = 2 ** 31 - 1
min_anime = ''
max_mem = 0
max_anime = ''

for anime in anime_data:
    if anime['members'] > max_mem:
        max_mem = anime['members']
        max_anime = anime['name']
    if anime['members'] < min_mem:
        min_mem = anime['members']
        min_anime = anime['name']

# print(min_mem)
# print(min_anime)
# print(max_mem)
# print(max_anime)

bucket_range =  int(max_mem / 100)
print(bucket_range)

anime_by_member_count = [ [] for i in range(10)]
for anime in anime_data:
    members = anime['members']
    # want to find which percentile they are in
    percentile = 0.1
    while(members > (percentile * max_mem)):
        percentile += 0.1

    percentile = int(percentile * 10)

    anime_list = anime_by_member_count[percentile-1]
    anime_list.append(anime)


# [{'anime_id': '16498', 'name': 'Shingeki no Kyojin', 'genre': ['Action', 'Drama', 'Fantasy', 'Shounen', 'SuperPower'], 'type': 'TV', 'episodes': '25', 'rating': 8.54, 'members': 896229}, {'anime_id': '11757', 'name': 'Sword Art Online', 'genre': ['Action', 'Adventure', 'Fantasy', 'Game', 'Romance'], 'type': 'TV', 'episodes': '25', 'rating': 7.83, 'members': 893100}]



average_rating_range = []
for i in range(10):
    total_rating = 0
    for anime in anime_by_member_count[i]:
        rating = anime['rating']
        total_rating += rating

    if len(anime_by_member_count[i]) == 0: average_rating_range.append(0)
    else:
        avg = total_rating / len(anime_by_member_count[i])
        average_rating_range.append(avg)

print(average_rating_range)
# [6.2631217021276475, 7.727129909365564, 7.960973451327431, 8.115102040816325, 8.372380952380954, 8.224117647058824, 8.385, 0, 8.184999999999999, 8.71]
