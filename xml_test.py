
import xmltodict
from pprint import pprint

xml_example = open("xml_example.xml").read()
pprint(xml_example)

print()
print (50*"#")

xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
ip_address = xml_dict["interface"]["ipv4"]["address"]["ip"]
print (int_name)
print(ip_address)