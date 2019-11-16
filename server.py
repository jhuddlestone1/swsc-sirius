from bottle import *
from api import *

@route('/static/<filename:path>')
def static(filename):
	return static_file(filename, root='static')

@route('/')
@route('/welcome')
def welcome():
	return template('welcome')
	
@route('/explore')
def explore():
	return template('explore')

@route('/api')
def route_api():
	return api(request.query)

run(host='localhost', port=8080)