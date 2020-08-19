import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading
from simple_pid import PID
import xlrd
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from pandas import *
import pandas as pd
import csv
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random

LARGE_FONT = ("Verdana", 12)
REG_FONT = ("Verdana", 9)

exit_case = False  # when set to true all threads will close properly
ref_rate = 100  # refresh rate of value on GUI, might be updated via config file
loc = ("config/config.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
ip = sheet.cell_value(1, 1)
refresh = int(sheet.cell_value(2, 1))
XX = int(sheet.cell_value(3, 1))
YY = int(sheet.cell_value(4, 1))
ppg = [0] * 8
for n in range(0, 8):
    ppg[n] = float(
        sheet.cell_value(6, n + 1))  # Update Pulses per gallon according to the Manufactureures Specifications
cal1 = sheet.cell_value(12, 1)  # Calibration Values for SHED temperature sensors
cal2 = sheet.cell_value(13, 1)
cal3 = sheet.cell_value(14, 1)
cal4 = sheet.cell_value(15, 1)

demo = 1
if demo == 0:
    from maq20 import MAQ20

    maq20 = MAQ20(ip_address=ip, port=502)  # Set communication with MAQ20
    AI_mod = maq20[1]  # Analog input module
    TTC_mod = maq20[2]  # Thermocouple input module.
    DIV20_mod = maq20[4]  # 20 digital discrete inputs
    DIOL_mod1 = maq20[5]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod2 = maq20[6]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod3 = maq20[7]  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod4 = maq20[8]  # 5 Digital discrete inputs, 5 Digital outputs
    AO_mod = maq20.find("VO")

    # Read input values from Modules
    DIOL_1 = (DIOL_mod1.read_data_counts(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
    DIOL_2 = (DIOL_mod2.read_data_counts(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
    DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
    DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
    T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
    AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))

    ser = serial.Serial(
        port='/dev/ttyS0',  # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
if demo == 1:
    AI_mod = [0] * 8  # Analog input module
    TTC_mod = [0] * 8  # Thermocouple input module.
    DIV20_mod = [0] * 20  # 20 digital discrete inputs
    DIOL_mod1 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod2 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod3 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod4 = [0] * 10  # 5 Digital discrete inputs, 5 Digital outputs
    AO_mod = [0] * 10

    # Read input values from Modules
    DIOL_1 = [0] * 10
    DIOL_2 = [0] * 10
    DIOL_3 = [0] * 10
    DIOL_4 = [0] * 10
    T = [0] * 8
    AI = [0.1] * 8
    def update_maq20():# include function if connected to MAQ20
        global DIOL_1,DIOL_2,DIOL_3,DIOL_4, T, AI
        DIOL_1 = (DIOL_mod1.read_data(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
        DIOL_2 = (DIOL_mod2.read_data(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
        DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
        DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
        T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
        AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
        read_serial()
    def update_unhooked():
        global DIOL_1, DIOL_2, DIOL_3, DIOL_4, T, AI
        for i in range (0,5):
            DIOL_1[i] = random.randint(0,1)
            DIOL_2[i] = random.randint(0,1)
            DIOL_3[i] = random.randint(0,1)
            DIOL_4[i] = random.randint(0,1)
        for i in range (0,8):
            T[i] = random.uniform(10,65)
            AI[i] = random.uniform(0.5,.6)
            flowrate[i] = random.uniform(4.5,5.5)

# Pump Variables
pumps = pd.DataFrame(
    [['Pump1', 0, 0, '', ''], ['Pump2', 0, 0, '', ''], ['Pump3', 0, 0, '', ''], ['Pump4', 0, 0, '', ''],
     ['Pump5', 0, 0, '', ''], ['Pump6', 0, 0, '', ''], ['Pump7', 0, 0, '', ''], ['Pump8', 0, 0, '', '']],
    columns=['Hardware', 'Raw Value', 'Eng Value', 'Text Value', 'Tab1 Text'])
valves = pd.DataFrame(
    [['Valve1', 0, 0, '', ''], ['Valve2', 0, 0, '', ''], ['Valve3', 0, 0, '', ''], ['Valve4', 0, 0, '', ''],
     ['Valve5', 0, 0, '', ''], ['Valve6', 0, 0, '', ''], ['Valve7', 0, 0, '', ''], ['Valve8', 0, 0, '', '']],
    columns=['Hardware', 'Raw Value', 'Eng Value', 'Text Value', 'Tab1 Text'])
flowrate = pd.DataFrame(
    [['Flowrate1', 0, 0, '', ''], ['Flowrate2', 0, 0, '', ''], ['Flowrate3', 0, 0, '', ''], ['Flowrate4', 0, 0, '', ''],
     ['Flowrate5', 0, 0, '', ''], ['Flowrate6', 0, 0, '', ''], ['Flowrate7', 0, 0, '', ''], ['Flowrate8', 0, 0, '', '']],
    columns=['Hardware', 'Raw Value', 'Eng Value', 'Text Value', 'Tab1 Text'])

#valves = pd.DataFrame([['Valve1', 0,0, '', ''], ['Valve2', 0,0, '', ''], ['Valve3', 0, 0,'', ''], ['Valve4', 0,0, '', ''],
#                       ['Valve5', 0,0, '', ''], ['Valve6', 0,0, '', ''], ['Valve7', 0,0, '', ''], ['Valve8', 0,0, '', '']],
#                      columns=['Hardware', 'Raw Value', 'Text Value', 'Tab1 Text'])
print(pumps)


def var_update():
    if demo == 1:
        update_unhooked()
    if demo == 0:
        update_maq20()
    global pumps, flowrate
    pumps['Raw Value'] = pumps['Eng Value'] # Raw Value is sent to maq20
    pumps.loc[pumps['Raw Value'] == 0, 'Text Value'] = 'off'    # if 0, then change to off
    pumps.loc[pumps['Raw Value'] == 1, 'Text Value' ]= 'on'     # if 1 then change to on
    for i in range(0,len(pumps)):       #text update for tab1
         pumps.at[i,'Tab1 Text'] = "Pump" + str(i+1) +'\n' + pumps.at[i,'Text Value'].upper()

    for i in range(0, len(flowrate)):
        flowrate.at[i, 'Raw Value'] =


def read_serial(): # place function in while loop to get continuous reading
    global frequency, flowrate, prev_count, prev_time
    current_time = time.time()
    sample_time = current_time-prev_time

    #while 1:  # not needed  if function is in while loop
    readchar = ser.readline().decode().rstrip("\n")     # Read Serial, decode, take off '\n' character at end of input
    #print("Decoded Input: " + readchar)
    split_char = readchar.split(',')                    # split sting into list by commas
    fixed_str = [i.strip('"\x00#') for i in split_char] # take off "\x00#" from anywhere in list
    try: # to prevent " ValueError: invalid literal for int() with base 10: ''"
        current_count = list(map(int,fixed_str))                #change string to integers for purpose of use in calculations
        #print (current_count)
        for n in range(0,8):
            frequency[n] = (current_count[n] - prev_count[n])*60/sample_time #pulse per minute
            flowrate.at[n, 'Raw Value'] = frequency[n]/ppg[n] # Flowrate in Gallons/min
            #print("Pump number " + str(n) + "\nFrequency is: " + str(frequency[n]) + " Pulses Per Minute!\nFlowrate is: " + str(flowrate[n]) + " GPM")

        prev_count = current_count
        prev_time = current_time
    except:
        return
    #print(fixed_str)
    #print( fixed_str[1], type(fixed_str[1]))
    #print(current_count, type(current_count))
    #print(fixed_int[1],type(fixed_int[1]))

var_update()
print(pumps)
class MainApplication(tk.Tk):

    def __init__(self):
        # tk.Tk.__init__(self)  # Was causing extra frame to pop up

        self.root = tk.Tk()  # create instance of Tk
        self.root.title("SHED Auxiliary Control V2")
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Auxiliary Health')
        self.tabControl.add(self.tab2, text="Automatic SHED control")
        self.tabControl.add(self.tab3, text='Flow Diagram')
        self.tabControl.pack(expand=1, fill='both')

        self.frame_tab1 = Tab1(self.tab1, self)
        self.frame_tab1.pack()

        self.frame_tab2 = Tab2(self.tab2, self)
        self.frame_tab2.pack()

        self.frame_tab3 = Tab3(self.tab3, self)
        self.frame_tab3.pack()

        self.root.geometry("1024x600")
        self.root.mainloop()


class Tab1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl1 = tk.Label(self, text="Tab1")
        lbl1.pack()


class Tab2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl2 = tk.Label(self, text="Tab2")
        lbl2.pack()


class Tab3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl3 = tk.Label(self, text="Tab3")
        lbl3.pack()

sched = BackgroundScheduler()
sched.start()
sched.add_job(background_communication)
app = MainApplication()
