"""
This example aims to show that when using functions that 'get' instead of 'read' the operation is quicker because
less modbus requests had to be made.
"""
from maq20 import MAQ20
import time

maq20 = MAQ20(ip_address="192.168.128.100", port=502)
module = maq20.get_module(1)  # get module with a registration number of 1. maq20[1] returns the same thing.

if module is None:  # check if module is found
    raise TypeError("Module not found")

read_start_time = time.time()  # record current time
result = module.read_data(start_channel=0, number_of_channels=module.read_input_channels())  #perform modbus request.
read_time = time.time() - read_start_time  # record time taken by subtracting current time with initial time.

# Repeat for 'get' function.
get_start_time = time.time()
result_get = module.read_data(start_channel=0, number_of_channels=module.get_number_of_channels())
get_time = time.time() - get_start_time

# print results (seconds)
print('Read time (seconds): {}'.format(read_time))
print('Get time (seconds):  {}'.format(get_time))
