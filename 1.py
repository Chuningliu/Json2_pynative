# 1. Convert the following dictionary into JSON format

# import json
# with open("pynative1.json","w") as f:
#     data = {"key1" : "value1", "key2" : "value2"}
#     json.dump(data,f,indent=4)
    
    
import json
data = {"key1" : "value1", "key2" : "value2"}
b=json.dumps(data)
print(b)