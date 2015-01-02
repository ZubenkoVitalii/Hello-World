Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:21:43) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> from urllib.request import urlopen
>>> response = urlopen('http://qainterview.cogniance.com/candidates')
>>> html = response.read().decode('utf-8')
>>> candidates = json.loads(html)['candidates']
>>> for item in candidates:
	if item['id'] == 33:
		print(item)

		
{'id': 33, 'name': 'name_test', 'position': 'pos_test'}
>>> response.close
<bound method HTTPResponse.close of <http.client.HTTPResponse object at 0x0000000003A805C0>>
>>> 
