"""
Example showing a loop used to read continuosly from a module until script is interrupted or stopped.
"""
from maq20 import MAQ20
import time

module_to_use = "VDN"  # change this to a module in your system. ("VSN", "VDN", etc)
delay_s = 0.1  # amount in seconds the script waits before reading another sample.


maq20 = MAQ20(ip_address="192.168.128.100", port=502)

a_module = maq20.find(module_to_use)

if a_module is None:  # Check if module was found.
    raise TypeError("Module not found.")

while True:
    print(a_module[:])  # same as: a_module.read_data(0, number_of_channels=a_module.get_number_of_channels())
    time.sleep(delay_s)
