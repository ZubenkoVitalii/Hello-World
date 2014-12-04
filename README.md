Hello-World
===========

My first repository on GitHub.
Python tasks:
1) GET, http://qainterview.cogniance.com/candidates, gives a list of all candidates. 
2) GET, http://qainterview.cogniance.com/candidates/<cand_id>, shows a candidate with id=<cand_id>. 
3) POST, http://qainterview.cogniance.com/candidates, adds a new candidate. 
4) DELETE, http://qainterview.cogniance.com/candidates/<cand_id>, deletes a candidate with id=<cand_id>. 
5) Code that verifies that data is added to server.
6) Code that verifies correctness of returned response codes.
7) Verify that all methods working as expected.
8) All data is correctly added to server.

Answers and questions:
https://github.com/ZubenkoVitalii/Hello-World/tree/master
1) Please, see the code in GET_list_of_candidates.py.
2) Please, see the code in Get_candidates_with_id.py.
3) Please, see the code in POST_add_new_candidate.py.
4) Please, see the code in DELETE_candidate_with_id.py.
5) As I understood the task, to verify that data was added to the server succesfully, both codes (GET_list_of_candidates.py, Get_candidates_with_id.py) can be used. Also, I can show the candidate with any id (Get_candidates_with_id.py), which has been added by code in (POST_add_new_candidate.py). Is it correct?
6) In this case, does correctness mean that the values "name" and "position" aren't null? 
If, for example, {"id": 806, "name": null, "position": null}, should the code print 'incorrect name and/or position'? Or something else? Could you specify?
7-8) "Try to create positive and negative verifications". - Does it mean that I need add some candidates with correct and incorrect "name" and/or "position" (null, numbers, images, spesial symbols,...or add extra key:value "age":"20",...) and check the candidates availability on server?
