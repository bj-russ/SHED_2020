"""
This example shows how to find a module in a system to work with.
Print the module to see information about that module.
"""
from maq20 import MAQ20

module_to_find = "VDN"
maq20 = MAQ20(ip_address="192.168.128.100", port=502)
a_module = maq20.find(module_to_find)
if a_module is None:  # Check if module was not found
    raise ValueError("Module not found")  # if not found, raise error.
print(a_module)  # print module to see information about it.
