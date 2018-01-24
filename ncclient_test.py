
from ncclient import manager
from pprint import pprint
import xmltodict

router = {"ip":"10.10.20.48",
          "port":"830",
          "user":"cisco",
          "pass":"cisco_1234!"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""

m = manager.connect(host=router["ip"],
                    port = router["port"],
                    username = router["user"],
                    password = router["pass"],
                    hostkey_verify = False)
interface_netconf = m.get_config("running", netconf_filter)
print()
print(50*"#")
pprint(interface_netconf)
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
print()
print(50*"#")
pprint(interface_python)
print()
print(50*"#")
pprint(interface_python["interfaces"]["interface"]["name"]["#text"])
print()
print(50*"#")