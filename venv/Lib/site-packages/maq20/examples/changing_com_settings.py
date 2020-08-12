"""
This module shows how to change some of the MAQ20 COMx's communication settings.

Note: This example does not change any settings because it writes the old values back.
        Also, If you want a setting to stay and be applied, a write to eeprom command needs to be sent and
        COM module needs a power cycle.
"""
from maq20 import MAQ20
from maq20 import COMx


maq20 = MAQ20(ip_address="192.168.128.100", port=502)
com = maq20.get_com()  # type: COMx

"""Save current settings so that we can leave the system as it was before this example."""
ip_address = com.read_ip_address()
ethernet_subnet_mask = com.read_ethernet_subnet_mask()
serial_port_baud = com.read_serial_port_baud()
serial_port_parity = com.read_serial_port_parity()
rs485_type = com.read_rs485_type()

"""IP ADDRESS"""
print('\nip address:')
com.write_ip_address("192.168.128.101")
print(com.read_ip_address())
com.write_ip_address([192, 168, 128, 102])
print(com.read_ip_address())

"""ETHERNET SUBNET MASK"""
print('\nEthernet subnet mask:')
com.write_ethernet_subnet_mask("255.255.0.1")
print(com.read_ethernet_subnet_mask())
com.write_ethernet_subnet_mask([255, 255, 0, 2])
print(com.read_ethernet_subnet_mask())

"""SERIAL PORT BAUD"""
print('\nSerial port baud:')
com.write_serial_port_baud(5)  # 0 to 10
print(com.read_serial_port_baud())
com.write_serial_port_baud(921600)  # see table in register map or function definition.
print(com.read_serial_port_baud())

"""SERIAL PORT PARITY"""
print('\nSerial port parity:')
com.write_serial_port_parity(0)  # 0 to 2
print(com.read_serial_port_parity())
com.write_serial_port_parity('EVEN')  # or any case combination (eVen, even, Even, etc)
print(com.read_serial_port_parity())

"""RS485 TYPE"""
print('\nRS485 type:')
com.write_rs485_type("2-wire")
print(com.read_rs485_type())
com.write_rs485_type(0)
print(com.read_rs485_type())

# Write back defaults for this example.
#
com.write_ip_address(ip_address)
com.write_ethernet_subnet_mask(ethernet_subnet_mask)
com.write_serial_port_baud(serial_port_baud)
com.write_serial_port_parity(serial_port_parity)
com.write_rs485_type(rs485_type)
