
import requests
from pprint import pprint

router = {"ip":"10.1.1.1",
          "port":"443",
          "user":"root",
          "pass":"cisco123"}

headers = {"Accept":"application/yang-data+json"}

u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1"
u = u.format(router["ip"], router["port"])

print(u)

r = requests.get(u,
                 headers = headers,
                 auth=(router["user"], router["pass"]),
                 verify=False)

pprint(r.text)



