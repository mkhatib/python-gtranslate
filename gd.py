#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
import sys
import simplejson as json

def detect_lang(text):
  base_url="http://www.google.com/uds/GlangDetect?"
  params=urlencode( (('v',2.0),('q',text)))
  url=base_url+params
  content=urlopen(url).read()
  response = json.loads(content)
  if response['responseStatus'] == 200:
    return response['responseData']['language']
  else:
    return None
  return language  

if __name__ == "__main__":
  if sys.argv[1] == '--file':
    text=open(sys.argv[2]).read()
  else: text = ' '.join(sys.argv[1:])  
  print detect_lang(text)
