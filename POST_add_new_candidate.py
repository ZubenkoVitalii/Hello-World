Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:21:43) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
import urllib.request
import json
json_dict = {  "name": "Zubenko Vitalii", "position": "QA Engineer" }
# convert json_dict to JSON
json_data = json.dumps(json_dict)
# convert str to bytes (ensure encoding is OK)
post_data = json_data.encode('utf-8')
# we should also say the JSON content type header
headers = {}
headers['Content-Type'] = 'application/json'
# now do the request for a url
req = urllib.request.Request('http://qainterview.cogniance.com/candidates', post_data, headers)

# send the request
res = urllib.request.urlopen(req)
print(res.read().decode("cp1251"))
{
  "candidate": {
    "id": 925, 
    "name": "Zubenko Vitalii", 
    "position": "QA Engineer"
  }
}
>>> 
