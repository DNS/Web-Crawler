import urllib, ssl
import re, sqlite3, time, sys, socket
import http.cookiejar
import socks	# pip install pysocks


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
REQUEST_TIMEOUT = 5
ERROR_RETRY = 99

cj = http.cookiejar.CookieJar()
ssl._create_default_https_context = ssl._create_unverified_context

def http_get (hyperlink):
	#ssl._create_default_https_context = ssl._create_unverified_context
	#ctx = ssl.create_default_context()
	#ctx.check_hostname = False
	#ctx.verify_mode = ssl.CERT_NONE
	for i in range(ERROR_RETRY):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': USER_AGENT}, data=None)
			#response = urllib.request.urlopen(req, context=ctx, timeout=REQUEST_TIMEOUT)
			response = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)).open(req, timeout=REQUEST_TIMEOUT)
			#print(response.geturl())
			return response.read().decode('utf-8')
		except Exception as e:
			#sys.stderr.write(str(e)+'\n')
			raise(str(e))
			time.sleep(2)

# params: {'key1':'val1','key2':'val2'}
def http_post (hyperlink, params):
	#ssl._create_default_https_context = ssl._create_unverified_context
	#ctx = ssl.create_default_context()
	#ctx.check_hostname = False
	#ctx.verify_mode = ssl.CERT_NONE
	for i in range(ERROR_RETRY):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': USER_AGENT}, data=urllib.parse.urlencode(params).encode() )
			#response = urllib.request.urlopen(req, context=ctx, timeout=REQUEST_TIMEOUT)
			response = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)).open(req, timeout=REQUEST_TIMEOUT)
			return response.read().decode('utf-8')
		except Exception as e:
			#sys.stderr.write(str(e)+'\n')
			raise(str(e))
			time.sleep(2)




############
### MAIN ###
############


#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
#socket.socket = socks.socksocket

#data = {
#	'param1':'value1',
#	'param2':'value2',
#}

#text_res = http_post('https://test.com/search.php', data)
#print(text_res)


#text_res = http_get('http://bing.com')
#print(text_res)




############################


text_res = http_get('https://forlap.ristekdikti.go.id/mahasiswa')
m1 = re.findall(r'<input type="hidden" name="captcha_value_1" value="(\d*?)">\r\n\s*?<input type="hidden" name="captcha_value_2" value="(\d*?)">'
		, text_res, re.MULTILINE | re.IGNORECASE | re.DOTALL)
if m1:
	for arr in m1:
		captcha1, captcha2 = int(arr[0]), int(arr[1])
		#print(arr, captcha1 + captcha2)

data = {
	"dummy":"031038+++Universitas+Bina+Nusantara",
	"id_sp":"6C91755E-50E5-4ACF-B454-37A058BA9BCB",
	"id_sms":"CA5901CA-D995-4A47-9D33-B46100A3E129",
	"keyword":"1000881",
	"kode_pengaman":19,
	"captcha_value_1":10,
	"captcha_value_2":9
}

'''
"kode_pengaman":captcha1+captcha2,
"captcha_value_1":captcha1,
"captcha_value_2":captcha2
'''

#text_res2 = http_post('https://forlap.ristekdikti.go.id/mahasiswa/search', data)
text_res = http_post('https://forlap.ristekdikti.go.id/mahasiswa/search', data)
print(text_res)




