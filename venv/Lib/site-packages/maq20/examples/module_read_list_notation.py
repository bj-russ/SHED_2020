"""
This example shows how to read a module using python list notation.

The API supports indexing, iteration, slicing, and negative indexing

One module is required to tun this example.
"""

from maq20 import MAQ20

maq20 = MAQ20()
a_module = maq20[1]  # Module registered at slot 1, same as a_module = maq20.get_module(1)

# indexing
print('Channel 0 : a_module[0] : {}'.format(a_module[0]))

print('')
# iteration
print('for channel in a_module:')
for channel in a_module:
    print(channel)

print('')
print('for i in range(len(a_module)):')
for i in range(len(a_module)):
    print('Channel {} : {}'.format(i, a_module[i]))

print('')  # new line
# slicing
print('Slice from 1 to 4 : a_module[1:5] : {}'.format(a_module[1:5]))
print('All Channels : a_module[:] : {}'.format(a_module[:]))

# negative indexing
print('')  # new line
print('Last Channel : a_module[-1] : {}'.format(a_module[-1]))
