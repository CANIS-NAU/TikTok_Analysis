from TikTokApi import TikTokApi
import json
from datetime import datetime

verifyFp = 'verify_kpqe6rfw_unz5YaMC_N4WS_4WEQ_9xNj_28X1dhIgBRt8'
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints = True)

results = 1999
time = datetime.now()

# Updating naming convention to hopefully give a new file each time
current = time.strftime("%d%m%Y-%H%M%S")
hashtag = 'indigenous'
full_dic = api.by_hashtag(hashtag = hashtag,count = results)
#print(indigenous[0])

# dump entire array returned by api into json:
file_name = hashtag+'_full_'+current
with open(file_name,'w') as outfile:
    json.dump(full_dic, outfile)

# Initial Investigation
# Looks like tags live in something called "challenges". Let's print each
# for tiktok in indigenous:
#   for tag in tiktok['challenges']:
#       if tag['title'] != 'indigenous':
            #print(tag['title'])
        #print()


''' Cool, that gave me what I wanted. I'm seeing nativetiktok, nativeamerican come up a lot!
Have to decide what kind of format we want this in for comparison over time. A dictionary mapping
the tiktok id to all of the hashtags, maybe? Or should I just store the entire array returned in indigenous?
Probably that, so we can do multiple comparisons with the same object. For now, I'll just assemble a dictionary of
ids and hashtags for my own perusal.
'''

hashtag_dic = {}

for tiktok in full_dic:
    key = tiktok['id']
    for tag in tiktok['challenges']:
        if key not in hashtag_dic:
            hashtag_dic[key] = [tag['title']]
        else:
            hashtag_dic[key].append(tag['title'])



'''
Here, doing the json.dump method to put the returned array of dictionaries from this hashtag into a json file, 
will talk with morgan about what to do with that on 5/25.
'''
hashtag_file_name = hashtag+'_hashtag_dic_'+current
with open(hashtag_file_name,'w') as outfile:
    json.dump(hashtag_dic, outfile)







