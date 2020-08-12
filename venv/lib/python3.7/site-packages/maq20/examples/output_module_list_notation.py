"""
Example showing how to write data to a module using list notation.
"""
from maq20 import MAQ20

maq20 = MAQ20()  # Initialize system with default parameters ip_address='192.168.128.100', port=520
output_module = maq20.find("VO")  # get a reference to the output module by finding by name.

if output_module is None:  # check if the module was found.
    raise TypeError('Module not found')

initial_state = output_module[:]  # Read the current state of the channels.
print('Initial state = output_module[:]\n{}'.format(initial_state))  # print its current state

print('\nWriting to all channels at once:')
"""
The following command construct a list by using the built-in len() function and then using a for loop
to write a list that looks like:
[3.3, 3.3, 3.3, ..., 3.3]
"""
output_module[:] = [3.3 for _ in range(len(output_module))]
print('output_module[:] = [3.3 for _ in range(len(output_module))]\n{}'.format(output_module[:]))  # print the state again.

print('\nWrite to one channel:')
output_module[0] = 1.2
print('output_module[0] = 1.2\n{}'.format(output_module[:]))  # print the state again.

print('\nWrite to a subset of channels:')
output_module[2:6] = [5, 5, 5, 5]
print('output_module[2:6] = [5, 5, 5, 5]\n{}'.format(output_module[:]))  # print the state again.

output_module[:] = initial_state  # Write back initial state.
