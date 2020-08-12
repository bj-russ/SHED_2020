"""
This example uses the xlsxwriter library.

This example reads all channels from a module and writes them into a spreadsheet with a timestamp every second.

Improvements that can be made:
    - Log more modules
    - Label the channels
    - Show Units (V, A, R, T, etc)
    - Use a Timer instead of a delay

Potential Change:
    - Use internal File I/O libraries to write a CSV file without using an external library.
"""
from maq20 import MAQ20
import time, xlsxwriter
from datetime import datetime

"""Parameters."""
module_to_use = "JTC"

"""MAQ20 Initialization."""
maq20 = MAQ20(ip_address="192.168.128.100", port=502)
a_module = maq20.find(module_to_use)

"""xlsx file creation and opening."""
workbook = xlsxwriter.Workbook(str(datetime.now()).replace(':', '_').replace('.', '_') + '.xlsx')
worksheet = workbook.add_worksheet()

"""
Write header:
[ Module Name, 'Channel 0', 'Channel 1', ... , 'Channel n']
"""
header = [a_module.get_name()]
for i in range(a_module.get_number_of_channels()):
    header.append('Channel {}'.format(i))

worksheet.write_column(col=0, row=0, data=header)  # Write header of the module used:

for i in range(10):
    worksheet.write_row(col=0, row=i+1, data=[str(datetime.now())])
    worksheet.write_row(col=1, row=i+1, data=a_module.read_data(number_of_channels=a_module.get_number_of_channels()))
    time.sleep(1)
    print(i+1)

workbook.close()
