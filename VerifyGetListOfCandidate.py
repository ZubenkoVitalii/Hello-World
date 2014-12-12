import json
from urllib.request import urlopen


response = urlopen('http://qainterview.cogniance.com/candidates')
if response.getcode() !=200:
    print('Candidates are not exist, wrong http response code != 200')

json_resp = response.read().decode("cp1251")
cand_resp = json.loads(json_resp)

if cand_resp and type(cand_resp) == dict:
    print('Good response from the server with candidates info')
    print('Check if we received correct info for candidates')
else:
    print("Candidates don't exist")

Good response from the server with candidates info
Check if we received correct info for candidates
