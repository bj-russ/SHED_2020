"""
Shows how to use a module that has special functions that other modules normally don't have.

This example uses the IVI (not released) to access its burst mode parameters and functions.
"""
from maq20 import MAQ20
from maq20.modules.diol import DIOL

system0 = MAQ20(ip_address="192.168.128.100", port=502)
module_name = 'DIOL'
diol = system0.find(module_name)

if diol is not None:  # Check if module was found.
    diol = DIOL(maq20_module=diol)
else:
    raise TypeError("Module not found.")

diol.write_special_function_5_frequency_generator(timer=0, frequency=500)  # frequency generator 500 Hz

print(diol.read_special_function_information(timer=0))  # read back the special function settings using timer 0
