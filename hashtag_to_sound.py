from TikTokApi import TikTokApi
import json
#from datetime import datetime

verifyFp = 'verify_kpqf4sp4_SoSmCG3K_JAJv_4zah_8n9j_xl4cG9vZdGDc'
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints = True)

results = 30

#time = datetime.now()
#current = time.strftime("%d%m%Y-%H%M%S")

hashtag = 'nativetiktok'
full_dic = api.by_hashtag(hashtag = hashtag,count = results)

# Get a dictionary of sounds that stem from nativetiktok
sound_list = {}

for tiktok in full_dic:
    key = tiktok['id']
    if key not in sound_dic:
        sound_dic[key] = key['music']['id']
    else:
        sound_dic[key].append(key['music']['id'])

print(sound_dic)

# grab the first sound, see what other tiktoks are using this sound 
first_sound = list(sound_dic.values())[0]

tiktoks = api.bySound(soundId, count=results)

for tiktok in tiktoks:
    print(tiktok)


