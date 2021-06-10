from TikTokApi import TikTokApi
import json

verifyFp = 'verify_kp1smpu7_udw29DoR_RhXe_4p8C_B8Q9_RukzGDZGlesz'
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints = True)

results = 1999

hopi = api.by_hashtag(hashtag = 'hopi',count = results)

hashtag_dic = {}

for tiktok in hopi:
	key = tiktok['id']
	for tag in tiktok['challenges']:
		if key not in hashtag_dic:
			hashtag_dic[key] = [tag['title']]
		else:
			hashtag_dic[key].append(tag['title'])


with open("hopi_challenges_short.json",'w') as outfile:
	json.dump(hashtag_dic, outfile)

'''
that gave me really weird outputs, like byte strings. What if I get the hashtag names from textExtra instead?
Aha!! They're unicode symbols, for when someone uses an emoji or another language (see kpop). Apparently "fyp"+ some kind of sideways smile is popular,
esp with k-pop which is half of what's coming up with hopi. Looks like textExtra and challenges contain the same info, 
so no need to duplicate below. 
'''
# hashtag_dic2 = {} 

# for tiktok in hopi:
# 	key = tiktok['id']
# 	for item in tiktok['textExtra']:
# 		if item['hashtagName']:
# 			if key not in hashtag_dic2:
# 				hashtag_dic2[key] = [item['hashtagName']]
# 			else:
# 				hashtag_dic2[key].append(item['hashtagName'])

# with open("hopi_textExtra_short.json",'w') as outfile:
# 	json.dump(hashtag_dic2, outfile)