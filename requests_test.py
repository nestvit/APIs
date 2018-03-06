
import requests
from pprint import pprint

router = {"ip":"172.26.31.201",
          "port":"443",
          "user":"cisco1",
          "pass":"cisco1"}

headers = {"Accept":"application/yang-data+json"}

u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet0"
u = u.format(router["ip"], router["port"])

print(u)

r = requests.get(u,
                 headers = headers,
                 auth=(router["user"], router["pass"]),
                 verify=False)

pprint(r.text)

import json
api_data = r.json()
print()
print(50*"#")
pprint (api_data)
interfacename = api_data["ietf-interfaces:interface"]["name"]


print()
print(50*"#")
print(interfacename)





