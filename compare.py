import json
from collections import Counter 

with open("indigenous_full.json", 'r') as fp:
    today = json.load(fp)

with open("indigenous_full_523.json", 'r') as fp:
    sun = json.load(fp)

with open('indigenous_hashtag_dic.json','r') as fp:
	today_dic = json.load(fp)

'''
# Number of tiktoks by id that are the same form 5/23 and 5/25
print(today[0]['id'])
print(sun[0]['id'])
print(today[0]['author']['uniqueId'])
print(sun[0]['author']['uniqueId'])

'''
total = 0
list_index = []
ids = []
for i in range(len(today)):
	for j in range(len(sun)):
		if today[i]['id'] == sun[j]['id']:
			ids.append(today[i]['id'])
			ids.append(today[j]['id'])
			list_index.append(i)
			total += 1
intersect = len(set(list_index))
union = len(set(ids))

print('total:', total)
print(len(today))
print('intersect:', intersect)
#print(list_index)
print('union:',union)
print('jaccard:',intersect/union)


# most common hashtags:
# concatenate all lists into one list, user counter
big = []
for key in today_dic:
	big.extend(today_dic[key])

print(Counter(big).most_common(15))
#print(list(counts.keys())[0:10])

