Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:21:43) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
# Include library urllib.request
import urllib.request
# Read url into variable
request_url = 'http://qainterview.cogniance.com/candidates/6'
request = urllib.request.Request(request_url)
# Delete item from variable
request.get_method = lambda: 'DELETE'
# send the request
urllib.request.urlopen(request)
<http.client.HTTPResponse object at 0x0000000003A34EF0>
