from TikTokApi import TikTokApi
api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)

results = 10

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=results, custom_verifyFp='verify_kp1smpu7_udw29DoR_RhXe_4p8C_B8Q9_RukzGDZGlesz')
# From first meeting with Morgan: verify_kon3g2ik_kTgoMHHt_7KGC_4kss_BQrY_bLRTl6saCDDH

for tiktok in trending:
    # Prints the id of the tiktok
    authors = print(tiktok['author']['uniqueId'])

#print(len(trending))