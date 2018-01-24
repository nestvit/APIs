
import requests
from pprint import pprint

router = {"ip":"10.10.20.48",
          "port":"443",
          "user":"cisco",
          "pass":"cisco_1234!"}

headers = {"Accept":"application/yang-data+json"}

u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1"
u = u.format(router["ip"], router["port"])

print(u)

r = requests.get(u,
                 headers = headers,
                 auth=(router["user"], router["pass"]),
                 verify=False)

pprint(r.text)

import json
api_data = r.json()
interfacename = api_data["ietf-interfaces:interface"]["name"]

print(interfacename)





