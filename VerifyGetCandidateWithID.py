 import json
 from urllib.request import urlopen
 id = '25'
 response = urlopen('http://qainterview.cogniance.com/candidates/' + id)
 if response.getcode() !=200:
	print('Candidate is not exist, wrong http response code != 200')

	
 json_resp = response.read().decode("cp1251")
 cand_resp = json.loads(json_resp)
  # verify that it is not empty response from the server, it is a dictionary, and it has a key 'candidate' and 'candidate' key array has key 'id'
 if cand_resp and type(cand_resp) == dict and 'candidate' in cand_resp.keys() and 'id' in cand_resp['candidate'].keys():
	# Get item (string type) into variable received_id from array with index 'id'
	received_id = cand_resp['candidate']['id'].__str__()
	print('Good response from the server with candidate info')
	print('Check if we received correct info for candidate with id=' + id)
	if received_id == id:
		print('All OK, correct info')
	else:
		print('Received info for candidate with id=' + received_id + ', but not ' + id.__str__())
else:
	print("Candidate doesn't exist")

	
Good response from the server with candidate info
Check if we received correct info for candidate with id=25
Received info for candidate with id=22, but not 25

