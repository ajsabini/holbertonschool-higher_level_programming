#!/usr/bin/python3
""" fetchs a given url - """


import requests

if __name__ == "__main__":

	req = requests.get('https://intranet.hbtn.io/status')
	print('Body response:')
	print('\t- type: {}'.format(type(req.text)))
	print('\t- content: {}'.format(req.text))
