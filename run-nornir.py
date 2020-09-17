#!/usr/bin/env python

from nornir import InitNornir
# from nornir.plugins.tasks.networking import napalm_get
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir.core.inventory import Host
import json

from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command
from nornir.core.filter import F
# from nornir.plugins.tasks import networking
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(config_file="config.yaml")
# print(json.dumps(Host.schema(), indent=4)) # print schema

print( nr.inventory.hosts)
print( nr.inventory.groups)
print( nr.inventory.hosts["spine1"])

result = nr.run(napalm_get, getters=['get_facts'])
# print_result(result)

# result = nr.run(netmiko_send_command, command_string="show versions")
# print_result(result)

Junos_devices = nr.filter(F(platform="junos"))
# for dev in Junos_devices.inventory.hosts:
    # psss

result = Junos_devices.run(task=napalm_cli, commands=["show bgp summary"])
# print(type(result))
# print(dir(result))
print_result(result)
for k in result:
    # print(type(result[k]))
    print("#### " + k )
    print_result(result[k])
    # print(result[k]["show bgp summary"]) # this does not work
    # for m in result[k]:
    #     print(type(m))
    #     print_result(m)
