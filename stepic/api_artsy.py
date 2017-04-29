import requests
import json
from operator import itemgetter


def get_name_and_year(cipher, headers):
    r = requests.get('https://api.artsy.net/api/artists/' + str(cipher), headers=headers)
    j = json.loads(r.text)
    return j['sortable_name'], j['birthday']


def main():
    client_id = r'62b3a748a6ca6bebb7dc'
    client_secret = r'b6fad7a08fc3a97eb9097e51b3929bc0'

    r = requests.post(r'https://api.artsy.net/api/tokens/xapp_token',
                      data={
                          'client_id': client_id,
                          'client_secret': client_secret
                      })
    j = json.loads(r.text)
    token = j['token']

    headers = {'X-Xapp-Token': token}
    with open('artists.txt', 'rt') as f:
        artists = {}
        for line in f:
            name, year = get_name_and_year(line.rstrip(), headers)
            artists[name] = year
        artists = sorted(artists.items(), key=itemgetter(1, 0))
        [print(artist[0]) for artist in artists]

if __name__ == '__main__':
    main()
