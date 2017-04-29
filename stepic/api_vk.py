import requests


api_url = r'https://api.vk.com/method/'
method = 'friends.get'
params = {'user_id': 2923}
r = requests.get(api_url+method, params)
j = r.json()
print(j['response'])
#r = requests.get(api_url+'users.get', )
