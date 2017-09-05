import json

def read_credentials():
	with open('secrets/under-armour.json') as f:
		credentials = json.load(f)
	return credentials