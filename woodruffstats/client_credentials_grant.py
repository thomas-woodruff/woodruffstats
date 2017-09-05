import requests
import json
import read_credentials

credentials = read_credentials.read_credentials()
client_id = credentials['key']
client_secret = credentials['secret']


post_data  = {
'grant_type': 'client_credentials',
'client_id': client_id,
'client_secret': client_secret
}

post_url = 'https://api.ua.com/v7.1/oauth2/access_token/'

r = requests.post(post_url, data = post_data)

print(r.text)

access_token = r.json()['access_token']	

print(access_token)


activity_type_url = 'https://api.ua.com/v7.1/activity_type/'
response = requests.get(url=activity_type_url, verify=False,
                        headers={
                        'api-key': client_id,
                        'authorization': 'Bearer %s' % access_token})

activity_types = response.json()

print(activity_types['_embedded']['activity_types'][0])