import urllib.request
# now do the request for a url
id = '43'
request_url = ('http://qainterview.cogniance.com/candidates/' + id)
request = urllib.request.Request(request_url)
request.get_method = lambda: 'DELETE'
# send the request
res = urllib.request.urlopen(request)
# analysis of response code
if res.getcode() !=200:
    print('Candidate is not deleted, wrong http response code != 200')

else:
   print("Candidate is successfully deleted")

Candidate is successfully deleted
