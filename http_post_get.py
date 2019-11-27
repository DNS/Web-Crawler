import urllib.request, ssl
import re, sqlite3, time
import socket
import socks	# pip install pysocks
import sys

def http_get(hyperlink):
	#ssl._create_default_https_context = ssl._create_unverified_context
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	for i in range(999):
		try:
			response = urllib.request.urlopen(hyperlink, context=ctx)
			return response.read().decode('utf-8')
		except urllib.error.HTTPError as e:
			#eprint(e.reason)
			eprint('error: http_get()')
			time.sleep(2)

# params: {'key1':'val1','key2':'val2'}
def http_post(hyperlink, params):
	#ssl._create_default_https_context = ssl._create_unverified_context
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	for i in range(999):
		try:
			req = urllib.request.Request(hyperlink, data=urllib.parse.urlencode(params).encode() )
			response = urllib.request.urlopen(req, context=ctx)
			return response.read().decode('utf-8')
		except urllib.error.HTTPError as e:
			#eprint(e.reason)
			eprint('error: http_post()')
			time.sleep(2)



############
### MAIN ###
############


#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
#socket.socket = socks.socksocket

data = {
	'a':'111',
	'b':'222',
	'c':'333',
}

#text_res = http_post('https://test.com/search.php', data)
#print(text_res)


text_res = http_get('http://bing.com')
print(text_res)




'''






'''




