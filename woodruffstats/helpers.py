from datetime import datetime

def get_datetime(datetime_str):
	return datetime.strptime(datetime_str[:19], '%Y-%m-%dT%H:%M:%S')