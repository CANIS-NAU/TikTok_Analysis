from TikTokApi import TikTokApi
import json
from datetime import datetime

v = 'verify_kq8ugckw_iIUbvyId_SYn0_45ie_BlZf_haGHX8GrPhpd'
api = TikTokApi.get_instance(custom_verifyFp=v, use_test_endpoints = True)
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)

results = 1999
time = datetime.now()
current = time.strftime("%d%m%Y_%H%M%S")


# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=results)
# verify_de3299f562a9f9ed9b52564fc0522962
# verify_de3299f562a9f9ed9b52564fc0522962

# From first meeting with Morgan: verify_kon3g2ik_kTgoMHHt_7KGC_4kss_BQrY_bLRTl6saCDDH
file_name = 'trending_'+current
with open(file_name,'w') as outfile:
    json.dump(trending, outfile)

users = []
for tiktok in trending:
    # Prints the id of the tiktok
    users.append(tiktok['author']['id'])
print(users)


#print(len(trending))