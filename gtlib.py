#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
import sys
from gd import detect_lang
import simplejson as json

MAX_TEXT_LENGTH = 680

def translate(text, to='en'):
	to_langs = to.split(' ')
	lang1 = detect_lang(text[:MAX_TEXT_LENGTH])
	results = {}
	for lang in to_langs:
		langpair = '%s|%s'%(lang1,lang)
		base_url = 'http://ajax.googleapis.com/ajax/services/language/translate'
		translation = ''
		params = urlencode((('v',1.0), ('q',text),('langpair',langpair)))
		content = urlopen(base_url, params).read()
		response = json.loads(content)
		if response['responseStatus'] == 200:
			results[lang] = response['responseData']['translatedText']
		else:
			results[lang] = None
	return results

def isBlank(str):
	return len(str.strip()) == 0
	
def main():
	print translate('Hello World', 'ar es ja')

if __name__ == '__main__':
	main()
