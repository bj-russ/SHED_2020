"""
Shows how to setup an output module for writing data to it and shows how to write data.
"""
from maq20 import MAQ20

maq20 = MAQ20(ip_address="192.168.128.100", port=502)  # Initialize
vo = maq20.find("VO")  # get a reference to the module by name

if vo is None:  # check if module was found
    raise TypeError("Module was not found")

initial_value = vo.read_channel_data(3)  # Read initial value
print('Initial output value: {}'.format(initial_value))

vo.write_channel_data(channel=3, data=3.3)  # write using write_data()
print('Output value after writing: {}'.format(vo.read_channel_data(3)))

vo.write_channel_data(channel=3, data=initial_value)  # write back initial value.


