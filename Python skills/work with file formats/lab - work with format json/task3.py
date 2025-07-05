import json
destfile = "res-file.json"
with open(destfile) as data_file:
 data = json.load(data_file)
from pprint import pprint
#pprint(data)

key1 = data.keys() 
print(list(key1)) 

for subvalue in data["quiz"].items():
    if subvalue[0]=='maths':
       res1=subvalue
       print(res1)
       for subvalue1 in res1:
            print(subvalue1)
            res2=subvalue1
            for subvalue2 in res2:
                print(subvalue2)
                
                
    

        
        


