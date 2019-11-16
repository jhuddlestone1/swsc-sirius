def api(request):
	time = request.forms.get('time')
	if time:
		timestamp = open('timestamp.txt', 'w')
		timestamp.write(time)
		timestamp.close()
	else:
		abort(400, 'Bad Request')