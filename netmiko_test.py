
from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
          "host": "10.10.20.48",
          "user": "cisco",
          "pass": "cisco_1234!"}


net_connect = ConnectHandler(ip=router["host"],
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show run int Gig1")

pprint(interface_cli)


