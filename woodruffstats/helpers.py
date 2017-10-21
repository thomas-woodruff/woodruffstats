from datetime import datetime
import collections

def get_datetime(datetime_str):
	return datetime.strptime(datetime_str[:19], '%Y-%m-%dT%H:%M:%S')


def keys_dict_keys(target_keys, source_dict):
	target_dict = {target_key: source_dict[target_key] for target_key in target_keys}


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + str(k) if parent_key else str(k)
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def convert_metres_to_miles(distance_metres):
	return distance_metres / 1609.34
