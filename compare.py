import json
from collections import Counter 

file1 = "indigenous_full_525.json"
# need to find a better way to automate file selection
with open(file1, 'r') as fp:
    today = json.load(fp)

file2 = "indigenous_full_523.json"
with open(file2, 'r') as fp:
    sun = json.load(fp)

with open('indigenous_hashtag_dic_525.json','r') as fp:
	today_dic = json.load(fp)

'''
Get the number of shared tiktoks between two sessions (intersect) and the set of all tiktoks (union)
May want to put into a function so I can return the jaccard similarity. 
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

print('total tiktoks in common:', total)
#print(len(today))
print('intersect:', intersect)
#print(list_index)
print('union:',union)
print('jaccard:',intersect/union)


# most common hashtags:
# concatenate all lists into one list, user counter
big = []
for key in today_dic:
	big.extend(today_dic[key])

print('most common hashtags:',Counter(big).most_common(15))
#print(list(counts.keys())[0:10])

