"""
Example of how to log data using csv format.
"""
import csv
from maq20 import MAQ20
import time
from datetime import datetime

"""Parameters."""
module_to_use = "JTC"
filename = str(datetime.now()).replace(':', '_').replace('.', '_') + '.csv'  # uses current time as filename

"""MAQ20 Initialization."""
maq20 = MAQ20(ip_address="192.168.128.100", port=502)
a_module = maq20.find(module_to_use)

with open(filename, 'w', newline='') as csv_file:
    logger = csv.writer(csv_file, delimiter=',')
    logger.writerow([a_module.get_name()])
    header = ['Timestamp']
    for i in range(a_module.get_number_of_channels()):
        header.append('Channel {}'.format(i))
    logger.writerow(header)
    for i in range(5):
        logger.writerow([str(datetime.now())] + a_module[:])
        time.sleep(1)
        print(i + 1)
