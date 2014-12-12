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

Answers:
1) Please, see the code in GET_list_of_candidates.py.
2) Please, see the code in Get_candidates_with_id.py.
3) Please, see the code in POST_add_new_candidate.py.
4) Please, see the code in DELETE_candidate_with_id.py.
5) To verify that data was added to the server succesfully, both codes (GET_list_of_candidates.py, Get_candidates_with_id.py) can be used. Also, I can show the candidate with any id (Get_candidates_with_id.py), which has been added by code in (POST_add_new_candidate.py). Is it correct?
6) Please, see the code in ReturnedResponseCodes.py.
7) a) Please, see the code in VerifyGetListOfCandidate.py for method "GET, http://qainterview.cogniance.com/candidates, gives a list of all candidates". This method works correctly.
  b) Please, see the code in VerifyGetCandidateWithID.py for method "GET, http://qainterview.cogniance.com/candidates/<cand_id>, shows a candidate with id=<cand_id>". This method works incorrectly. At specifying in the request the candidate with any id, we always see in the response the first candidate in list of candidates.
  c) Please, see the code in VerifyPostAddNewCandidate.py for method "POST, http://qainterview.cogniance.com/candidates, adds a new candidate". This method works correctly.
  d) Please, see the code in VerifyDeleteCandidateWithID.py for method "DELETE, http://qainterview.cogniance.com/candidates/<cand_id>, deletes a candidate with id=<cand_id>". This method works correctly.
8) 

Datamining tasks: 
Answers are stored in Datamining.txt.
