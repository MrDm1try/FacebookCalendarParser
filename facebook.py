import requests

from config import facebook_token

ans = requests.get("https://graph.facebook.com/me?fields=id,name&access_token={}".format(facebook_token))
print(ans.json())
