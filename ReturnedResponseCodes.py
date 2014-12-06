>>> import json
>>> from urllib.request import urlopen
>>> response = urlopen('http://qainterview.cogniance.com/candidates')
>>> html = response.read().decode('utf-8')
>>> candidates = json.loads(html)['candidates']
>>> for item in candidates:
	if item['id'] == 93:
		print(response.getcode())

		
200
>>> res.close
____________________
>>> import urllib.request
>>> import json
>>> json_dict = {  "name": "Zubenko Vitalii", "position": "QA Engineer" }
>>> json_data = json.dumps(json_dict)
>>> post_data = json_data.encode('utf-8')
>>> headers = {}
>>> headers['Content-Type'] = 'application/json'
>>> req = urllib.request.Request('http://qainterview.cogniance.com/candidates', post_data, headers)
>>> res = urllib.request.urlopen(req)
>>> print(res.getcode())
201
>>> res.close

______________________

>>> request_url = 'http://qainterview.cogniance.com/candidates/86'
>>> request = urllib.request.Request(request_url)
>>> request.get_method = lambda: 'DELETE'
>>> res = urllib.request.urlopen(request)
>>> print(res.getcode())
200
>>> res.close

______________________

>>> from urllib.request import urlopen
>>> res = urlopen("http://qainterview.cogniance.com/candidates")
>>> print(res.getcode())
200
>>> res.close
