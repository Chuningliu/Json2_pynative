# 3.PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

import json
b= {"key1": "value1", "key2": "value2"}
with open("pynative3.json","w") as f:
    json.dump(b,f,indent=2)

