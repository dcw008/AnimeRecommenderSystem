import json
import csv

def csv_to_json():
    data_list = []
    with open('rating.csv') as f:
        reader = csv.reader(f)
        for line in reader:
            if(line[0] == 'user_id'): continue
            rating_object = {}
            rating_object['user_id'] = line[0]
            rating_object['anime_id'] = line[1]
            rating_object['rating'] = line[2]

            data_list.append(rating_object)

    with open('rating.json', 'w') as outfile:
        json.dump(data_list, outfile)

# csv_to_json()

data = json.load(open('rating.json'))
print(len(data))
