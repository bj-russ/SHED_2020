"""
Example of how to use the utilities module in the MAQ20 API when reading and writing directly to registers.
"""
from maq20 import MAQ20
import maq20.utilities as utils

maq20 = MAQ20(ip_address="192.168.128.100", port=502)

com = maq20.get_com()  # get a reference to the COM module in the MAQ20 system

# The name of a module is stored in the first 15 registers
name_raw = com.read_registers(0, 15)
name = utils.response_to_string(com.read_registers(address=0, number_of_registers=11))
print('Raw name: {}'.format(name_raw))
print('utils.response_to_string(name_raw) : {}'.format(name))

print('')  # new line
# Writing a number bigger than 16 bits: 2^16-1 = 65535
com.write_registers(address=1368, values=utils.int32_to_int16s(987134))
# Reading a number bigger than 16 bits:
read_back = utils.int16_to_int32(com.read_registers(address=1368, number_of_registers=2))
print('Wrote 32 bit number 987134 and we read: {}'.format(read_back))
