
from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
          "host": "172.26.31.201",
          "user": "cisco1",
          "pass": "cisco1"}


net_connect = ConnectHandler(ip=router["host"],
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show run int Gig0")

pprint(interface_cli)


