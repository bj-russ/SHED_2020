"""
Shows how to display a snapshot of all data of all modules in the system.
"""
from maq20.maq20 import MAQ20

# Initiate a maq20 system and communication.
system0 = MAQ20(ip_address="192.168.128.100", port=502)

# Call print system data.
system0.print_system_data()
