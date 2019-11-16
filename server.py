#!/usr/bin/python3
from bottle import *
from api import *

@route('/static/<filename:path>')
def route_static(filename):
	return static_file(filename, root='static')

@route('/')
@route('/welcome')
def route_welcome():
	return template('welcome')
	
@route('/explore')
def route_explore():
	return template('explore')

@route('/api', method='POST')
def route_api():
	return api(request)

run(host='localhost', port=8080)