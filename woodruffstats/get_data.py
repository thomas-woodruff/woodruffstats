import woodruffstats.auth as auth
import woodruffstats.read_credentials as read_credentials
import requests

# credentials = read_credentials.read_credentials()
# client_id = credentials['key']
# client_secret = credentials['secret']
# access_token = auth.get_access_token(credentials)

# auth_headers = auth.construct_auth_headers(client_id, access_token)

def get_user_id(auth_headers):
	url = 'https://api.ua.com/v7.1/user/self/'
	response = requests.get(url=url, headers=auth_headers)

	return response.json()['id']


def get_all_workouts(auth_headers, user_id):
	url_stub = 'https://api.ua.com/'
	workouts_url = url_stub + 'v7.1/workout/?limit=40&user=%s' % user_id
	workouts_response = requests.get(url=workouts_url, headers=auth_headers).json()

	workouts = workouts_response['_embedded']['workouts']
	next_workouts_link = workouts_response['_links'].get('next')
	
	while next_workouts_link:
	    next_workouts_url = url_stub + next_workouts_link[0]['href']
	    next_workouts_response = requests.get(url=next_workouts_url, headers=auth_headers).json()
	    
	    workouts.extend(next_workouts_response['_embedded']['workouts'])
	    
	    next_workouts_link = next_workouts_response['_links'].get('next')

	return workouts


def get_workouts_runs(workouts):
	return [i for i in workouts if i['_links']['activity_type'][0]['id'] == '16' and i['is_verified']]


def get_all_activity_types(auth_headers):
	url = 'https://api.ua.com/v7.1/activity_type/'
	response = requests.get(url=url, headers=auth_headers)
	
	activity_type_items = response.json()['_embedded']['activity_types']
	
	return [{'id': i['_links']['self'][0]['id'], 'name': i['name']} for i in activity_type_items]