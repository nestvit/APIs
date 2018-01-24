
import json
from pprint import pprint

json_example = open("json_example.json").read()
pprint(json_example)

print()
print (50*"#")

json_python = json.loads(json_example)
int_name = json_python["ietf-interfaces:interface"]["name"]
print("Name interface: " + int_name)

print()
print (50*"#")

print(json.dumps(json_python))
