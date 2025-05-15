# import urllib.request
# import json
 
# url = "https://quote-api.dicoding.dev/list"
# response = urllib.request.urlopen(url)
# result = response.read().decode()
# print(result)

import requests
 
url = "https://quote-api.dicoding.dev/list"
response = requests.get(url)
print(response.json())