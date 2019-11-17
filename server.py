#!/usr/bin/python3

import subprocess
from bottle import *
from api import *

local = subprocess.check_output(['hostname', '-I']).decode('utf-8').strip()


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


@route('/fetch', method='POST')
def route_api_fetch():
	return api_fetch(request)
	
@route('/put', method='POST')
def route_api_put():
	return api_put(request)
	
@route('/timestamp', method='POST')
def route_fetch_timestamp():
	return fetch_timestamp()


run(host=local, port=80)