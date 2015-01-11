>>> import redis
>>> r = redis.StrictRedis(host='localhost', port=6379, db=3)
#create the DB
>>> r.hmset('candidates', {'name': 'Anna', 'position': 'QA'})
True
>>> r.hmset('candidates:1', {'name': 'Bella', 'position': 'QA'})
True
>>> r.hmset('candidates:2', {'name': 'Dmutro', 'position': 'Tester'})
True
>>> r.hmset('candidates:3', {'name': 'Roma', 'position': 'QA'})
True
>>> r.hmset('candidates:4', {'name': 'Victor', 'position': 'Tester'})
True
# verify the DB
>>> r.keys('candidates*')
['candidates:2', 'candidates:4', 'candidates:1', 'candidates', 'candidates:3']
>>> r.hmget('candidates:3', 'name')
['Roma']
>>> r.hmget('candidates:3', 'position')
['QA']
>>> r.hmget('candidates:3', 'position', 'name')
['QA', 'Roma']
>>> r.hgetall('candidates:3')
{'position': 'QA', 'name': 'Roma'}
>>> r.hgetall('candidates:4')
{'position': 'Tester', 'name': 'Victor'}
# delete candidates:4
>>> r.delete('candidates:4')
1
# verify that candidates:4 is absent in DB
>>> r.hgetall('candidates:4')
{}
>>> r.keys('candidates*')
['candidates:2', 'candidates:1', 'candidates', 'candidates:3']
>>> r.dbsize()
4L
# verify that other canditates are in BD
>>> r.hgetall('candidates:2')
{'position': 'Tester', 'name': 'Dmutro'}
>>> r.hgetall('candidates:1')
{'position': 'QA', 'name': 'Bella'}
>>> r.hgetall('candidates')
{'position': 'QA', 'name': 'Anna'}

#Positive testing

>>> r.hmset('candidates:4', {'name': '-1/3', 'position': '0.3333'})
True
>>> r.hgetall('candidates:4')
{'position': '0.3333', 'name': '-1/3'}

>>> r.hmset('candidates:5', {'name': 'object', 'position': {"street": "Address",
"city": "Kyiv", "postalCode": "03067"}})
True
>>> r.hgetall('candidates:5')
{'position': "{'postalCode': '03067', 'city': 'Kyiv', 'street': 'Address'}", 'name': 'object'}

>>> r.hmset('candidates:6', {'name': True, 'position': 'QA'})
True
>>> r.hgetall('candidates:6')
{'position': 'QA', 'name': 'True'}

>>> r.hmset('candidates:7', {'name': None, 'position': None})
True
>>> r.hgetall('candidates:7')
{'position': 'None', 'name': 'None'}

>>> r.hmset('candidates:8', {'name': 'Cyrillic', 'position': 'РђР±СЂР°-РєР°РґР°Р±СЂР° С–'})
True
>>> r.hgetall('candidates:8')
{'position': '\xd0\x90\xd0\xb1\xd1\x80\xd0\xb0-\xd0\xba\xd0\xb0\xd0\xb4\xd0\xb0\xd0\xb1\xd1\x80\xd0\xb0 \xd1\x96', 'name': 'Cyrillic'}

#Negative testing

>>> r.delete('candidates:9')
0
>>> r.delete('candidates:null')
0
>>> r.delete('candidates:none')
0

>>> r.hmset('candidates:9', {'name': 'Tester', 'name': 'QA'})
True
>>> r.hgetall('candidates:9')
{'name': 'QA'}

>>> r.hmset('candidates:10', {'position': 'Tester', 'position': 'QA'})
True
>>> r.hgetall('candidates:10')
{'position': 'QA', 'name': 'QA'}

>>> r.hmset('candidates:11', {'name': 'Tester'})
True
>>> r.hgetall('candidates:11')
{'name': 'Tester'}

>>> r.hmset('candidates:12', {'position': 'Tester'})
True
>>> r.hgetall('candidates:12')
{'position': 'Tester'}

>> r.hmset('candidates:13', {'id':'null','name':'QA','position': 'Tester'})
True
>>> r.hgetall('candidates:13')
{'position': 'Tester', 'id': 'null', 'name': 'QA'}

>>> r.hmset('candidate:14', {'name': 'Input huge value', 'position': 'In the third week of November, in the year 1895, a dense yellow fog settled down upon London. From the Monday to the Thursday I doubt whether it was ever possible from our windows in Baker Street to see the loom of the opposite houses. The first day Holmes had spent in cross-indexing his huge book of references. The second and third had been patiently occupied upon a subject which he hand recently made his hobby--the music of the Middle Ages. But when, for the fourth time, after pushing back our chairs from breakfast we saw the greasy, heavy brown swirl still drifting past us and condensing in oily drops upon the window- panes, my comrades impatient and active nature could endure this drab existence no longer. He paced restlessly about our sittingd.In was aware that by anything of interest, Holmes meant anything of criminal interest. There was the news of a revolution, of a possible war, and of an impending change of government; but these did not come within the horizon of my companion. I could see nothing recorded in the shape of crime which was not commonplace and futile. Holmes groaned and resumed hs restless meanderings.  The London criminal is certainly a dull fellow,  said he in the querulous voice of the sportsman whose game has failed him.  Look out this window, Watson. See how the figures loom up, are dimly seen, and then blend once more into the cloud-bank. The thief or the murderer could roam London on such a day as the tiger does the jungle, unseen until he pounces, and then evident only to his victim. There have,  said I,  been numerous petty thefts. Holmes snorted his contempt. This great and sombre stage is set for something more worthy than that,  said he.  It is fortunate for this community that I am not a criminal. It is, indeed!  said I heartily. Suppose that I were Brooks or Woodhouse, or any of the fifty men who have good reason for taking my life, how long could I survive against my own pursuit? A summons, a bogus appointment, and all would be over. It is well they dont have days of fog in the Latin countries--the countries of assassination. By Jove! here comes something at last to break our dead monotony. It was the maid with a telegram. Holmes tore it open and burst out laughing. Well, well! What next?  said he.  Brother Mycroft is coming round. Why not?  I asked. Why not? It is as if you met a tram-car coming down a country lane. Mycroft has his rails and he runs on them. His Pall Mall lodgings, the Diogenes Club, Whitehall--that is his cycle. Once, and only once, he has been here. What upheaval can possibly have derailed him? Does he not explain? Holmes handed me his brothers telegram. Must see you over Cadogen West. Coming at once. Mycroft. Cadogen West? I have heard the name. It recalls nothing to my mind. But that Mycroft should break out in this erratic fashion! A planet might as well leave its orbit. By the way, do you know what Mycroft is? I had some vague recollection of an explanation at the time of the Adventure of the Greek Interpreter. You told me that he had some small office under the British government. Holmes chuckled. I did not know you quite so well in those days. One has to be discreet when one talks of high matters of state. You are right in thinking that he under the British government. You would also be right in a sense if you said that occasionally he IS the British government.'})
True
>>> r.hgetall('candidate:14')
{'position': 'In the third week of November, in the year 1895, a dense yellow fog settled down upon London. From the Monday to the Thursday I doubt whether it was ever possible from our windows in Baker Street to see the loom of the opposite houses. The first day Holmes had spent in cross-indexing his huge book of references. The second and third had been patiently occupied upon a subject which he hand recently made his hobby--the music of the Middle Ages. But when, for the fourth time, after pushing back our chairs from breakfast we saw the greasy, heavy brown swirl still drifting past us and condensing in oily drops upon the window- panes, my comrades impatient and active nature could endure this drab existence no longer. He paced restlessly about our sittingd.In was aware that by anything of interest, Holmes meant anything of criminal interest. There was the news of a revolution, of a possible war, and of an impending change of government; but these did not come within the horizon of my companion. I could see nothing recorded in the shape of crime which was not commonplace and futile. Holmes groaned and resumed hs restless meanderings.  The London criminal is certainly a dull fellow,  said he in the querulous voice of the sportsman whose game has failed him.  Look out this window, Watson. See how the figures loom up, are dimly seen, and then blend once more into the cloud-bank. The thief or the murderer could roam London on such a day as the tiger does the jungle, unseen until he pounces, and then evident only to his victim. There have,  said I,  been numerous petty thefts. Holmes snorted his contempt. This great and sombre stage is set for something more worthy than that,  said he.  It is fortunate for this community that I am not a criminal. It is, indeed!  said I heartily. Suppose that I were Brooks or Woodhouse, or any of the fifty men who have good reason for taking my life, how long could I survive against my own pursuit? A summons, a bogus appointment, and all would be over. It is well they dont have days of fog in the Latin countries--the countries of assassination. By Jove! here comes something at last to break our dead monotony. It was the maid with a telegram. Holmes tore it open and burst out laughing. Well, well! What next?  said he.  Brother Mycroft is coming round. Why not?  I asked. Why not? It is as if you met a tram-car coming down a country lane. Mycroft has his rails and he runs on them. His Pall Mall lodgings, the Diogenes Club, Whitehall--that is his cycle. Once, and only once, he has been here. What upheaval can possibly have derailed him? Does he not explain? Holmes handed me his brothers telegram. Must see you over Cadogen West. Coming at once. Mycroft. Cadogen West? I have heard the name. It recalls nothing to my mind. But that Mycroft should break out in this erratic fashion! A planet might as well leave its orbit. By the way, do you know what Mycroft is? I had some vague recollection of an explanation at the time of the Adventure of the Greek Interpreter. You told me that he had some small office under the British government. Holmes chuckled. I did not know you quite so well in those days. One has to be discreet when one talks of high matters of state. You are right in thinking that he under the British government. You would also be right in a sense if you said that occasionally he IS the British government.', 'name': 'Input huge value'}
>>> 
