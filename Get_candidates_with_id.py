Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:21:43) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
from urllib.request import urlopen
res = urlopen("http://qainterview.cogniance.com/candidates/37")
print(res.read().decode("cp1251"))
{
  "candidate": {
    "id": 22, 
    "name": "Dmitrii", 
    "position": "QA_intern"
res.close
<bound method HTTPResponse.close of <http.client.HTTPResponse object at 0x0000000003A99320>>
>>> 
