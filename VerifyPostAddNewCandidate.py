import urllib.request
import json

check_data = {'name': 'Vitalii', 'position': 'QA Engineer'}

# convert data to JSON
json_data = json.dumps(check_data)
# convert str to bytes (ensure encoding is OK)
post_data = json_data.encode('utf-8')
# we should also say the JSON content type header
headers = {'Content-Type': 'application/json'}
# now do the request for a url
req = urllib.request.Request('http://qainterview.cogniance.com/candidates', post_data, headers)
# send the request
res = urllib.request.urlopen(req)

if res.getcode() != 201:
    print('Candidate is not added, wrong http response code, != 201')

json_resp = res.read().decode("cp1251")
cand_resp = json.loads(json_resp)
# Проверяем есть ли ответ от сервера, тип ответа (dict) и он имеет ключ 'candidate' и в маcсиве ключа 'candidate' есть элемент 'id' 
if cand_resp and type(cand_resp) == dict and 'candidate' in cand_resp.keys() and 'id' in cand_resp['candidate'].keys():
    print('Candidate added, check if name and position are correct')
    flag = True
    for k in check_data.keys():
        #проверяем наличие ключей, указанных в check_data, в response from server
        if k not in cand_resp['candidate'].keys() or cand_resp['candidate'][k] != check_data[k]:
            flag = False
            break
    if flag:
        print("Candidate data added correctly")
    else:
        print("Wrong candidate data")
else:
    print('Candidate is not added')
    
Candidate added, check if name and position are correct
Candidate data added correctly
