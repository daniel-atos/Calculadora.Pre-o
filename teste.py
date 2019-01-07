import json
import sys

#load the data into an element
data={"test1" {"1" "1.2";'1.3'} , "test2" : "2", "test3" : "3"}

#dumps the json object into an element
json_str = json.dumps(data)

#load the json to a string
resp = json.loads(json_str)

#print the resp
print (resp)
pr = resp['test1']
#extract an element in the response
print (pr)