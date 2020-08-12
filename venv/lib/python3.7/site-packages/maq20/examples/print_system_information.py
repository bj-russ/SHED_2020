"""
Shows MAQ20 initialization and prints information about the system.
"""
from maq20 import MAQ20

system0 = MAQ20(ip_address="192.168.128.100", port=502)
# system0 = MAQ20(virtual_com=True, port="COM24")
print(system0)
