import json
from urllib.request import urlopen


response = urlopen('http://qainterview.cogniance.com/candidates')
if response.getcode() !=200:
    print('Candidates are not exist, wrong http response code != 200')

json_resp = response.read().decode("cp1251")
cand_resp = json.loads(json_resp)
# verify that it is not empty response from the server, it is a dictionary, and it has a key 'candidates' and type of 'candidates' key is array
if cand_resp and type(cand_resp) == dict and 'candidates' in cand_resp.keys() and type(cand_resp['candidates']) == list:
    print('Good response from the server with candidates info')
    print('Check if we received correct info for candidates')
else:
    print("Candidates don't exist")

Good response from the server with candidates info
Check if we received correct info for candidates
