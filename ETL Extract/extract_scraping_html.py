import requests
from bs4 import BeautifulSoup
 
url = "https://www.dicoding.com/blog/"
response = requests.get(url)
content = BeautifulSoup(response.content.decode(), 'html.parser')
 
all_content = content.find_all('h1')
 
for cont in all_content:
    print(cont)