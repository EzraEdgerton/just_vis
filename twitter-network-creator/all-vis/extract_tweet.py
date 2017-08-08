import os
import sys
import string
import re
import json

print os.listdir('formatted_data')

files = os.listdir('formatted_data')

files = files[1:]
digit = re.compile('[\d]')

post_shoot = open('postshoottweets.txt', 'w')
post_acquit = open('postacquittweets.txt', 'w')

shoot_tweets = ''
acquit_tweets = ''
print digit.match('1')
print digit.match('r')

def check_char(c):
	if c == 'd' or c == 'n':
		return 1
	if c == 'a' or c == 's':
		return 0

for f in files:
	d = digit.match(f[1])
	file_data = open('formatted_data/' + f, 'r' )
	file_json = json.load(file_data)
	file_nodes = file_json['nodes']
	if d:
		writeopt = check_char(f[2])
		if writeopt == 0:
			for tweet in file_nodes:
				for text in tweet['text']:
					s = text.encode('utf-8').strip()
					shoot_tweets = shoot_tweets + ' ' + s.lower().translate(None, string.punctuation)

		else:
			for tweet in file_nodes:
				for text in tweet['text']:
					s = text.encode('utf-8').strip()
					acquit_tweets = shoot_tweets + ' ' + s.lower().translate(None, string.punctuation)

	else:
		print f[1]
		writeopt = check_char(f[1])
		if writeopt == 0:
			for tweet in file_nodes:
				for text in tweet['text']:
					s = text.encode('utf-8').strip()
					shoot_tweets = shoot_tweets + ' ' + s.lower().translate(None, string.punctuation)

		else:
			for tweet in file_nodes:
				for text in tweet['text']:
					s = text.encode('utf-8').strip()
					acquit_tweets = shoot_tweets + ' ' + s.lower().translate(None, string.punctuation)

post_shoot.write(shoot_tweets)
post_acquit.write(acquit_tweets)


