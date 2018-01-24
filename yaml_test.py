
import yaml
from pprint import pprint

yml_example = open("yaml_example.yaml").read()
pprint(yml_example)

print()
print(50*"#")

yaml_python = yaml.load(yml_example)
int_name = yaml_python['ietf-interfaces:interface']["name"]
print(int_name)