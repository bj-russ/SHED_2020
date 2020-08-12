from maq20 import MAQ20

maq20 = MAQ20()
module_1 = maq20[1]  # same as maq20.get_module(1)
module_2 = maq20[2]  # same as maq20.get_module(2)

print('System level:')
print('maq20.read_registers(2000, 10) : {}'.format(maq20.read_registers(2000, 10)))
print('maq20.read_registers(4000, 10) : {}'.format(maq20.read_registers(4000, 10)))

print('\nModule level:')
# Show that the result is different.
print('module_1.read_registers(0, 10) : {}'.format(module_1.read_registers(0, 10)))  # this is equivalent to address 2000 to 2010
print('module_2.read_registers(0, 10) : {}'.format(module_2.read_registers(0, 10)))  # this is equivalent to address 4000 to 4010

