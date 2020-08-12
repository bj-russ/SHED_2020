
#!/usr/bin/env python
import serial
import time


ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0
frequency = [0.0]*8
def read_serial():
    global frequency
    rec_in_progress = False
    rec_char = 0
    ndx=0
    start_marker = "#"
    end_marker = "\n'"
    sample_time = 1
    prev_count = [0]*8

    while 1:

        print(ser.readline())
        print (type(ser.readline()))

        readchar = ser.readline().decode().rstrip("\n")     # Read Serial, decode, take off '\n' character at end of input
        print("Decoded Input: " + readchar)
        split_char = readchar.split(',')                    # split sting into list by commas
        fixed_str = [i.strip('"\x00#') for i in split_char] # take off "\x00#" from anywhere in list
        current_count = list(map(int,fixed_str))                #change string to integers for purpose of use in calculations
        for n in range(0,8):
            frequency[n] = (current_count[n] - prev_count[n])/60 #pulse per minute
        prev_count = current_count
        for n in range (0,8):
            print("Frequency is: " +str(frequency[n]) + " Pulses Per Minute!")
        #print(fixed_str)
        #print( fixed_str[1], type(fixed_str[1]))
        print(current_count, type(current_count))
        #print(fixed_int[1],type(fixed_int[1]))


read_serial()
