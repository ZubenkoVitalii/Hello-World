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
