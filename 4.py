# 4.Sort JSON keys in and write them into a file
#Sort following JSON data alphabetical order of keys


import json
with open("Meraki4.json","w") as f:
    a={"id" : 1, "name" : "value2", "age" : 29}
    json.dump(a,f,indent=4,sort_keys=True)
    

