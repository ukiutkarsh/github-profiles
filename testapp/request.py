"""
import requests
#from django.contrib.auth.models import User


response_user = requests.get('https://api.github.com/users/torvalds')
js = response_user.json()
print(js)
js_username = js['login']
js_followers = js['followers']
js_date = js['updated_at']
js_time = js_date[11:19]
js_date = js_date[0:10]
js_first_name = User.first_name
response_repo = requests.get('https://api.github.com/users/torvalds/repos')
repo = response_repo.json()
js_number = len(repo)
#for i in range(0,len(repo)):
    #final = repo[i]['stargazers_count']
    #print(final)
"""