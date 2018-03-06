
from ncclient import manager
from pprint import pprint
import xmltodict

router = {"ip":"172.26.31.201",
          "port":"830",
          "user":"cisco1",
          "pass":"cisco1"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet0</name>
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
pprint(interface_python["interfaces"]["interface"]["ipv4"]["address"]["ip"])
print()
print(50*"#")