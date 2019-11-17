import json


def api_fetch(request):
	time = request.forms.get('time')
	if time:
		return fetch_data(time)
	else:
		abort(400, 'Bad Request')
		
def api_put(request):
	time = request.forms.get('time')
	if time:
		timestamp = open('timestamp.txt', 'w')
		timestamp.write(time)
		timestamp.close()
		return fetch_data(time)
	else:
		abort(400, 'Bad Request')


def fetch_timestamp():
	timestamp = open('timestamp.txt', 'r')
	time = timestamp.read()
	timestamp.close()
	return time
	
def fetch_data(time):
	json_data = open('data/data.json');
	data = json.load(json_data)
	json_data.close()
	return data[time]