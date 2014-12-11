import urllib.request
id = '43'

request_url = ('http://qainterview.cogniance.com/candidates/' + id)
request = urllib.request.Request(request_url)
request.get_method = lambda: 'DELETE'
res = urllib.request.urlopen(request)

if res.getcode() !=200:
    print('Candidate is not deleted, wrong http response code != 200')

else:
   print("Candidate is successfully deleted")

Candidate is successfully deleted
