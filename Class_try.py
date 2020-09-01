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
SHED1 = False      # to keep track of SHED status
SHED2 = False
SHED3 = False
SHED_ready = [0,0,0]        # 0 is not requested, 1 is requested but not ready 2 is requested and ready
ref_rate = 100  # refresh rate of value on GUI, might be updated via config file
loc = ("config/config.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
ip = sheet.cell_value(1, 1)
ref_rate = int(sheet.cell_value(2, 1))
XX = int(sheet.cell_value(3, 1))
YY = int(sheet.cell_value(4, 1))
ppg = [0] * 8
for n in range(0, 8):
    ppg[n] = float(        sheet.cell_value(6, n + 1))  # Update Pulses per gallon according to the Manufacturer's Specs

deadhead_protection = sheet.cell_value(22,1)
valve_op_volt = sheet.cell_value(21,1)  # operational valve voltage -> changed to 5 for testing on 5V system .
##########################################################
#                  PID Setup values                      #
##########################################################
pid1 = 0
pid2 = 0
P1 = int(sheet.cell_value(8,1))
I1 = int(sheet.cell_value(9,1))
D1 = int(sheet.cell_value(10,1))
P2 = int(sheet.cell_value(8,2))
I2 = int(sheet.cell_value(9,2))
D2 = int(sheet.cell_value(10,2))

set_temp = [25,25]
pid1 = PID(P1, I1, D1, set_temp[0]) # PID for SHED2
pid1.output_limits = (0, 10)
pid2 = PID(P2, I2, D2, set_temp[1]) # PID for SHED3
pid2.output_limits = (0, 10)

###################################################################################
###                 Temperature Sensor smoothing and calibration                ###
###################################################################################
smoothing_size = int(sheet.cell_value(17,1))    # size of list used for smoothing average
smooth_t2 = 0
smooth_t3 = 0
T_shed2 = [20] * smoothing_size      # initiate list as size of smoothing_size with base
T_shed3 = [20] * smoothing_size


# Calibration Values for SHED temperature sensors
cal1 = sheet.cell_value(12, 1)
cal2 = sheet.cell_value(13, 1)
cal3 = sheet.cell_value(14, 1)
cal4 = sheet.cell_value(15, 1)

#######################################################################################################################
###                                             Important functional                                                ###
#######################################################################################################################
alarm_status = [0,0,0]
#######################################################################################################################
###                                              GUI stuff                                                          ###
#######################################################################################################################
index=0
flash_index = 0

flow_width = 8
pump_width = 5
flow_temp_width = 8
valve_width = 10

flow_status = [0,0,0] # Flow status check for checking if there is backflow: 0 is off, 1 is good to go, 2 is backflow in cold loop, 3 is backflow in hot loop
temp_status = [False] * 8 # Temp Status Check to make sure flow temp is in operation range
flowrate_status = [False] * 8 # Flowrate Checkup
temp_lower_bound = [0] * 8
temp_higher_bound = [0] * 8
flow_lower_bound = [0] * 8
flow_higher_bound = [0] * 8
for i in range(0, len(temp_lower_bound)):
    temp_lower_bound[i] = int(sheet.cell_value(26+i,1))
    temp_higher_bound[i] = int(sheet.cell_value(26+i,2))
    flow_lower_bound[i] = int(sheet.cell_value(36+i,1))
    flow_higher_bound[i] = int(sheet.cell_value(36+i,2))



def flash__(): # flash function for GUI flashing
    global flash_index
    flash_index = 1 - flash_index

#######################################################################################################################
###                                   Input Variable Definition                                                     ###
#######################################################################################################################
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
    AI = [0] * 8
    flowrate_value = [0]*8


def read_serial():
    global frequency, flowrate, prev_count, prev_time
    current_time = time.time()
    sample_time = current_time - prev_time

    # while 1:  # not needed  if function is in while loop
    readchar = ser.readline().decode().rstrip("\n")  # Read Serial, decode, take off '\n' character at end of input
    # print("Decoded Input: " + readchar)
    split_char = readchar.split(',')  # split sting into list by commas
    fixed_str = [i.strip('"\x00#') for i in split_char]  # take off "\x00#" from anywhere in list
    try:  # to prevent " ValueError: invalid literal for int() with base 10: ''"
        current_count = list(map(int, fixed_str))  # change string to integers for purpose of use in calculations
        # print (current_count)
        for n in range(0, 8):
            frequency[n] = (current_count[n] - prev_count[n]) * 60 / sample_time  # pulse per minute
            flowrate.at[n, 'Raw Value'] = frequency[n] / ppg[n]  # Flowrate in Gallons/min
            # print("Pump number " + str(n) + "\nFrequency is: " + str(frequency[n]) + " Pulses Per Minute!\nFlowrate is: " + str(flowrate[n]) + " GPM")

        prev_count = current_count
        prev_time = current_time

        return flowrate
    except:
        return
    # print(fixed_str)
    # print( fixed_str[1], type(fixed_str[1]))
    # print(current_count, type(current_count))
    # print(fixed_int[1],type(fixed_int[1]))
# update functions to be used for demo or non-demo


def update_maq20():# include function if connected to MAQ20
    global DIOL_1,DIOL_2,DIOL_3,DIOL_4, T, AI
    DIOL_1 = (DIOL_mod1.read_data(0, number_of_channels=DIOL_mod1.get_number_of_channels()))
    DIOL_2 = (DIOL_mod2.read_data(0, number_of_channels=DIOL_mod2.get_number_of_channels()))
    DIOL_3 = (DIOL_mod3.read_data_counts(0, number_of_channels=DIOL_mod3.get_number_of_channels()))
    DIOL_4 = (DIOL_mod4.read_data_counts(0, number_of_channels=DIOL_mod4.get_number_of_channels()))
    T = (TTC_mod.read_data(0, number_of_channels=TTC_mod.get_number_of_channels()))
    AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
    read_serial()


def update_unhooked(): # update data with random integers to check functionality
    global DIOL_1, DIOL_2, DIOL_3, DIOL_4, T, AI
    for i in range (0,5):
        DIOL_1[i] = random.randint(0,1)
        DIOL_2[i] = random.randint(0,1)
        DIOL_3[i] = random.randint(0,1)
        DIOL_4[i] = random.randint(0,1)
    for i in range (0,8):
        T[i] = random.uniform(10,65)
        AI[i] = random.uniform(0.5,.6)
        flowrate_value[i] = random.uniform(4.5,5)

# RAW Values for IO to/from maq20
pump_io = [0]*8               # output digital: p1 is 0 in list
valve_pos = [0]*8             # output analog
flow_pulse = [0]*8          # input From Serial Port
flow_temp = T
#SHED_req_to_start = [False]*3   # 0: SHED1, 1:SHED2, 2:SHED3 |  | digital input: 0 for no request, 1 for request
#SHED_good_to_start = [False]*3  # 0: SHED2, 1: SHED2 |  | digital output: 0 for not ready, 1 for ready
door_seal = [0]*2           # 0: SHED2, 1: SHED2 |  | digital output: 0 for open, 1 for seal
exhaustfan_request = 0      # Main Fan |  | digital output: 0 for no request, 1 for request
exhaustfan_feedback = 0     # Main Fan feedback |  | digital input: 0 for off, 1 for on
exhaust_damper = 1          # Main Fan Bypass |  | digital output: 0 for closed, 1 for open (closed for alarms)
SHED_exhaust_valve = [0]*2  # 0:SHED2, 1:SHED3 |  | digital output: 0 for closed, 1 for open


#calculated values:
flowrate_value = [0.0] *8   # Flowrate calculated from read_serial Function
SHED_temp = [0.0]*2         # 0: SHED2, 1: SHED3
SHED_pid = [0]*8            # 0: SHED2, 1: SHED3 calculated pid value

# text values from RAW Values
pump_text = ['']*8          # on, off interpreted from raw value
valve_text = ['']*8         # Valve position as text
flowrate_text = ['']*8
flow_temp_text = ['']*8
SHED_temp_text = ['']*2
SHED_exhaust_valve_text = ['']*2
exhaustfan_request_text = ''
exhaustfan_feedback_text = ''

flowrate_text_tab1 = ['']*8
pump_text_tab1 = ['']*8
flow_temp_text_tab1 = ['']*8
valve_text_tab1 = ['']*8
flow_valve_text_tab1 = ['']*8


def calculated_values_update():
    global SHED_temp, smooth_t2, smooth_t3
    if smooth_t2 == len(T_shed2):
        smooth_t2 = 0
    if smooth_t3 == len(T_shed3):
        smooth_t3 = 0

    # AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
    # read data from 0-3 for analog input 1-4

    sum2 = ((AI[0]) * cal1 + (AI[1]) * cal2) / 2  # Calibration in Config file
    sum3 = ((AI[2]) * cal3 + (AI[3]) * cal4) / 2  # Calibration in config file

    if 1 > AI[0] > 0.15:  # To filter outliers
        instant_t2 = sum2  ## Need to calibrate

        # for design purposes Shed 2 is AI0 and Shed 3 is AI1
        T_shed2[smooth_t2] = instant_t2
        smooth_t2 = smooth_t2 + 1

    if 1 > AI[1] > 0.15:  # To filter outliers
        instant_t3 = sum3  ## Need to calibrate
        T_shed3[smooth_t3] = instant_t3
        smooth_t3 = smooth_t3 + 1
    else:
        None

    ave_T_shed2 = round(sum(T_shed2) / float(len(T_shed2)), 2)
    ave_T_shed3 = round(sum(T_shed3) / float(len(T_shed3)), 2)
    SHED_temp = [ave_T_shed2, ave_T_shed3]




def flow_check(): # Checks Flowrate for Back Flow, Also Checks Exhaust Flow
    global flow_status, temp_status, SHED_good_to_start, flowrate_status
    # ---------- Flow / Temperature Status --------- #
    # temperature Status
    for i in range(0,len(temp_lower_bound)):
        if temp_lower_bound[i] < flow_temp[i] < temp_higher_bound[i]:
            temp_status[i] = True
        else:
            temp_status[i] = False
        if flow_lower_bound[i] < flowrate_value[i] < flow_higher_bound[i]:
            flowrate_status[i] = True
        else:
            flowrate_status[i] = False
    for i in range(0,8):   # Change for test cases
        flowrate_status[i] = True
        temp_status[i] = True
    # SHED 1 Flow Status
    if SHED1 is True:
        if flowrate_value[5] >= flowrate_value[6]:
            flow_status[0] = 1      # Flow Rate Normal
        else:
            flow_status[0] = 2      # Back Flow in Cold Loop

        if (temp_status[5] is True) and (temp_status[6] is True) and (flowrate_status[5] is True) and (flowrate_status[6] is True) and (flow_status[0] == 1):
            SHED_ready[0] = 2 # SHED 1 is ready
        else:
            SHED_ready[0] = 1  # SHED1 is requested, but not ready

    else: # if SHED1 is False:
        flow_status[0] = 0          # SHED off - No Check needed
        SHED_ready[0] = 0 # to reset

    #SHED 2 Flow Status

    if SHED2 is True:
        if (flowrate_value[5] >= flowrate_value[3]) and flowrate_value[4] >= flowrate_value[2]:
            flow_status[0] = 1      # Flow Rate Normal
        else:
            if flowrate_value[5] < flowrate_value[3]:
                flow_status[1] = 2  # Back Flow in cold loop
            elif flowrate_value[4] < flowrate_value[2]:
                flow_status[1] = 3  # Back Flow in Hot loop
            else:
                flow_status[1] = 4  # unknown Error

        if (temp_status[5] is True) and (temp_status[3] is True) and (temp_status[4] is True) and (temp_status[2] is True)\
                and (flowrate_status[5] is True) and (flowrate_status[3] is True) and (flowrate_status[4] is True) and (flowrate_status[2] is True) and (flow_status[1] == 1):
            SHED_ready[1] = 2 # SHED 1 is ready
        else:
            SHED_ready[1] = 1  # SHED1 is requested, but not ready

    else: #if SHED2 is False:
        flow_status[1] = 0          # SHED off - No Check needed
        SHED_ready[1] = 0 # to reset


    # SHED3 Flow Status
    if SHED3 is True:
        if flowrate_value[4] >= flowrate_value[0]:
            flow_status[2] = 1      # Flow Rate Normal
        else:
            flow_status[2] = 2      # Back Flow in Cold Loop

        if (temp_status[4] is True) and (temp_status[0] is True) and (flowrate_status[4] is True) and (flowrate_status[0] is True) and (flow_status[2] == 1):
            SHED_ready[2] = 2 # SHED 1 is ready
        else:
            SHED_ready[2] = 1  # SHED1 is requested, but not ready

    else: #if SHED3 is False:
        flow_status[2] = 0          # SHED off - No Check needed
        SHED_ready[2] = 0 # to reset


def text_update(): #Variable update function. to be used to update variables
    global pump_text, valve_text, flowrate_text, flow_temp_text, SHED_temp_text
    if demo == 1:
        update_unhooked()
    if demo == 0:
        update_maq20()

    for i in range(0,8):
        # pumps
        if pump_io[i] == 0:
            pump_text[i] = 'off'
        elif pump_io[i] == 1:
            pump_text[i] = 'on'
        else:
            pump_text[i] = 'error'
        # valves:
        valve_text[i] = str(round(100*valve_pos[i]/10,2)) +'%'
        flowrate_text[i] = str(round(flowrate_value[i],2)) + ' GPM'
        flow_temp_text[i] = str(round(T[i], 2))+ u' \N{DEGREE SIGN}'+"C"

    for i in range(0,2):
        SHED_temp_text[i] = str(SHED_temp[i])+ u' \N{DEGREE SIGN}'+"C"



text_update()

class SHEDoperation(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.start_btn1 = Button(self, width=25, font =LARGE_FONT)
        self.start_btn2 = Button(self, width=24, font =LARGE_FONT)
        self.start_btn3 = Button(self, width=24, font =LARGE_FONT)
        self.manual_btn = Button(self, width=25, font =LARGE_FONT, text = "Enter Manual Mode")
        
        def SHED_btn1_clicked():
            global SHED1
            SHED1 = True

            if SHED_ready[0] == 2:
                self.start_btn1.configure(text='SHED1: Operational', bg='green', command=SHED_btn1_stop)
            elif SHED_ready[0] == 1:
                self.start_btn1.configure(text='SHED1: Start Request SENT', bg = 'yellow', command = SHED_btn1_stop)
            else:
                pass

        def SHED_btn1_stop():
            global SHED1, SHED_ready
            SHED1 = False
            SHED_ready[0] = 0
            self.start_btn1.configure(text="SHED1: Request to Start", command=SHED_btn1_clicked,
                                 bg="red")

        def SHED_btn2_clicked():
            global SHED2, SHED_ready
            SHED2 = True
            #SHED_ready[1] = 1
            if SHED_ready[1] == 2:
                self.start_btn2.configure(text='SHED2: Operational', bg='green', command=SHED_btn2_stop)
            elif SHED_ready[1] == 1:
                self.start_btn2.configure(text='SHED2: Start Request SENT', bg = 'yellow', command = SHED_btn2_stop)
            else:
                pass

        def SHED_btn2_stop():
            global SHED2, SHED_req_to_start#, start_btn2

            SHED2 = False
            SHED_ready[1] = 0
            self.start_btn2.configure(text="SHED2: Request to Start", command=SHED_btn2_clicked,
                                 bg="red")

        def SHED_btn3_clicked():
            global SHED3, SHED_ready
            SHED3 = True
            if SHED_ready[2] == 2:
                self.start_btn3.configure(text='SHED3: Operational', bg='green', command=SHED_btn3_stop)
            elif SHED_ready[2] == 1:
                self.start_btn3.configure(text='SHED3: Start Request SENT', bg = 'yellow', command = SHED_btn3_stop)
            else:
                pass

        def SHED_btn3_stop():
            global SHED3, SHED_ready
            SHED3 = False
            SHED_ready[2] = 0
            self.start_btn3.configure(text="SHED3: Request to Start", command=SHED_btn3_clicked,
                                 bg="red")



        def SHED_btn_update():
            global SHED_ready
            flow_check()
            if SHED1:
                if SHED_ready[0] == 2:
                    self.start_btn1.configure(text='SHED1: Operational', bg='green', command=SHED_btn1_stop)
                elif SHED_ready[0] == 1:
                    self.start_btn1.configure(text='SHED1: Start Request SENT', bg = 'yellow', command = SHED_btn1_stop)
                else:
                    pass
            else:
                SHED_ready[0] = 0
                self.start_btn1.configure(text="SHED1: Request to Start", command=SHED_btn1_clicked,bg="red")

            if SHED2:
                if SHED_ready[1] == 2:
                    self.start_btn2.configure(text='SHED2: Operational', bg='green', command=SHED_btn2_stop)
                elif SHED_ready[1] == 1:
                    self.start_btn2.configure(text='SHED2: Start Request SENT', bg = 'yellow', command = SHED_btn2_stop)
                else:
                    pass
            else:
                SHED_ready[1] = 0
                self.start_btn2.configure(text="SHED2: Request to Start", command=SHED_btn2_clicked,bg="red")

            if SHED3:
                if SHED_ready[2] == 2:
                    self.start_btn3.configure(text='SHED3: Operational', bg='green', command=SHED_btn3_stop)
                elif SHED_ready[2] == 1:
                    self.start_btn3.configure(text='SHED3: Start Request SENT', bg = 'yellow', command = SHED_btn3_stop)
                else:
                    pass
            else:
                SHED_ready[2] = 0
                self.start_btn3.configure(text="SHED3: Request to Start", command=SHED_btn3_clicked,bg="red")
            self.start_btn2.after(ref_rate, SHED_btn_update)

        self.start_btn1.grid(column=0, row=0)

        self.start_btn2.grid(column=1, row=0)

        self.start_btn3.grid(column=2, row=0)

        self.manual_btn.grid(column=3, row=0)

        SHED_btn_update()


class FlowDisplay(tk.Frame):
    def __init__(self, parent, controller):
        ttk.LabelFrame.__init__(self, parent, text = "Main Loop")
        mainframe = FlowMain(parent, self)
        mainframe.pack()

def flow_calculate(flow_text, n):
    def flow_update():
        txt = ''
        # for n in range(0,8):
        flow_text[n].configure(text="Flowrate \n" + str(round(flowrate_value[n], 2)) + " GPM")
        #print(flowrate[n])
        flow_text[n].after(ref_rate, flow_update)
    flow_update()
def pump_status(pump_text,i):
    def pump_text_update():
        x = 0
        txt = ""

        if pump_io[i] == 0:
            txt = "Pump" + str(i + 1) + "\nOFF"
            pump_text[i].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off


        elif pump_io[i] == 1:
            txt = "Pump" + str(i + 1) + "\nON"
            if pump_error[i] == 0:
                pump_text[i].configure(text=txt, bg="green", fg="black")  # Pump text 1 for ON 0 for Off

            if pump_error[i] == 1:
                bgflash = ("black", "red")
                pump_text[i].configure(bg=bgflash[flash_index])
        else:
            txt = "error"
        pump_text[i].configure(text=txt)  # Pump text 1 for ON 0 for Off
        pump_text[i].after(ref_rate, pump_text_update)

    pump_text_update()

def flow_temp_status(temp_text,n):
    def temp_text_update():
        txt = ""
        txt = "Temp." + str(n + 1) + "\n" +str(round(T[n],2)) + u'\N{DEGREE SIGN}'+"C"
        temp_text[n].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off
        temp_text[n].after(ref_rate, temp_text_update)
    temp_text_update()

def valve_position(valve_text,n):
    def valve_text_update():
        txt=""
        txt="Valve Pos." + str(n+1) + "\n" + str(round(100*valve_pos[n]/10,2)) +"%"
        valve_text[n].configure(text=txt)
        valve_text[n].after(ref_rate, valve_text_update)
    valve_text_update()


def FlowMonitor(app_window, item1, item2):
    hotLabel0 = Label(app_window, text="Hot", font=("Bold", 10), padx=9)
    coldLabel0 = Label(app_window, text="Cold", font=("Bold", 10), padx=9)
    hotLabel0.grid(row=2, column=0)
    coldLabel0.grid(row=3, column=0)
    flowrate_text_tab1[item1] = Label(app_window, padx=10, width=flow_width)
    flowrate_text_tab1[item2] = Label(app_window, padx=10, width=flow_width)
    flowrate_text_tab1[item1].grid(row=2, column=2)
    flowrate_text_tab1[item2].grid(row=3, column=2)
    pump_text_tab1[item1] = Label(app_window, padx=10, width=pump_width)
    pump_text_tab1[item2] = Label(app_window, padx=10, width=pump_width)
    pump_text_tab1[item1].grid(row=2, column=1)
    pump_text_tab1[item2].grid(row=3, column=1)
    flow_temp_text_tab1[item1] = Label(app_window, padx=10, width=flow_temp_width)
    flow_temp_text_tab1[item2] = Label(app_window, padx=10, width=flow_temp_width)
    flow_temp_text_tab1[item1].grid(row=2, column=3)
    flow_temp_text_tab1[item2].grid(row=3, column=3)
    flow_valve_text_tab1[item1] = Label(app_window, padx=10, width=valve_width)
    flow_valve_text_tab1[item2] = Label(app_window, padx=10, width=valve_width)
    flow_valve_text_tab1[item1].grid(row=2, column=4)
    flow_valve_text_tab1[item2].grid(row=3, column=4)

    lower = min(item1,item2)
    larger = max(item1,item2)

    for n in range(lower,larger+1):
        pump_status(pump_text_tab1, n)
        flow_calculate(flowrate_text_tab1, n)
        flow_temp_status(flow_temp_text_tab1, n)
        valve_position(flow_valve_text_tab1, n)

def AlarmMonitor(app_window):
    SHED1alarm_label1 = Label(app_window, text="SHED1: ")
    SHED2alarm_label1 = Label(app_window, text="SHED2: ")
    SHED3alarm_label1 = Label(app_window, text="SHED3: ")
    SHED1alarm_label1.grid(row=1, column=1)
    SHED2alarm_label1.grid(row=2, column=1)
    SHED3alarm_label1.grid(row=3, column=1)
    SHEDalarm_label_status = [Label(app_window, text=''),Label(app_window, text=''),Label(app_window, text='')]
    for i in range(0,3):
        SHEDalarm_label_status[i].grid(row=i + 1, column=2)

        def SHEDalarm_label1_update(label):
            def update():
                for i in range(0, 3):
                    if alarm_status[i] == 0:
                        label[i].configure(text="inactive", fg='black')
                    elif alarm_status[i] == 1:
                        label[i].configure(text="ACTIVE", fg='red')
                    else:
                        label[i].configure(text='CODE ERROR')
                label[0].after(ref_rate, update)

            update()

        SHEDalarm_label1_update(SHEDalarm_label_status)


def AlarmFunction():
    global SHED1, SHED2, SHED3, exhaustfan_request, exhaust_damper, SHED_exhaust_valve

    # NORMAL OPERATION
    if alarm_status[0]+alarm_status[1]+alarm_status[2] == 0:
        exhaustfan_request = 1
        exhaust_damper = 1
        SHED_exhaust_valve = [0,0]
    else:
        exhaustfan_request = 1
        exhaust_damper = 0          # Close exhaust damper to allow for full vacuum

        #SHED 1 ALARM
        if alarm_status[0] == 1:
            SHED1 = False           # set SHED 1 to off
            SHED_ready[0]=0
            #valve_pos[6] = 0        # close valve for cold water flow into External chiller.
        else:
            pass
        #SHED2 ALARM
        if alarm_status[1] == 1:
            SHED_exhaust_valve[0] = 1   # Open Exhaust valve at rear of SHED2
            SHED2 = False
            SHED_ready[1] = 0
        else:
            SHED_exhaust_valve[0] = 0
        #SHED3 ALARM
        if alarm_status[1] ==1:
            SHED_exhaust_valve[1] = 1
            SHED3 = False
            SHED_ready[2] = 0
        else:
            SHED_exhaust_valve[1] = 0


def ExhaustMonitor(app_window):
    damper_label1 = Label(app_window, text="Damper Position: ", font=("Bold", 10), justify=RIGHT)
    damper_label1.grid(row=0, column=0, sticky=E)
    damper_position_label1 = Label(app_window, text="test")
    damper_position_label1.grid(row=0, column=1)

    def damper_label1_update(exhaust_damper_label):
        def update():
            if exhaust_damper == 1:
                exhaust_damper_label.configure(text="CLOSED")
            else:
                exhaust_damper_label.configure(text="OPEN")
            exhaust_damper_label.after(ref_rate, update)
        update()

    damper_label1_update(damper_position_label1)
    exhaustfan_label1 = Label(app_window, text="Exhaust fan: ", font=("Bold", 10))
    exhaustfan_label1.grid(row=1, column=0, sticky=E)
    exhaustfan_io_label1 = Label(app_window, text="test")
    exhaustfan_io_label1.grid(row=1, column=1)
    exhaustfan_feedback_label1 = Label(app_window, text="test2")
    exhaustfan_feedback_label1.grid(row=1, column=2)

    def extractor_status_update(extractor_fan_label, extractor_status_label):
        def update():
            if exhaustfan_request == 1:
                extractor_fan_label.configure(text="Requested", fg='black')
            else:
                extractor_fan_label.configure(text="off", fg="black")
                extractor_status_label.configure(text="Zero Flow", fg="black")
            if exhaustfan_feedback == 1:
                extractor_status_label.configure(text="Confirmed")
                extractor_fan_label.configure(fg="black")
            else:
                fgflash = ("black", "red")
                extractor_status_label.configure(text="Zero Flow", fg=fgflash[flash_index])
            extractor_fan_label.after(ref_rate, update)

        update()

    extractor_status_update(exhaustfan_io_label1, exhaustfan_feedback_label1)
    SHED2_label1 = Label(app_window, text="SHED2 Exhaust: ", font=("Bold", 10), justify=RIGHT)
    SHED2_label1.grid(row=2, column=0, sticky=E)
    SHED2_valve_position_label1 = Label(app_window, text="test")
    SHED2_valve_position_label1.grid(row=2, column=1)
    SHED3_label1 = Label(app_window, text="SHED3 Exhaust: ", font=("Bold", 10), justify=RIGHT)
    SHED3_label1.grid(row=3, column=0, sticky=E)
    SHED3_valve_position_label1 = Label(app_window, text="test")
    SHED3_valve_position_label1.grid(row=3, column=1)

    def SHED_valvetext_update(valve_label2, valve_label3):
        def update():
            if SHED_exhaust_valve[0] == 1:
                valve_label2.configure(text="OPEN")
            elif SHED_exhaust_valve[0] == 0:
                valve_label2.configure(text="CLOSED")
            else:
                valve_label2.configure(text='error')
            if SHED_exhaust_valve[1] == 1:
                valve_label3.configure(text="OPEN")
            elif SHED_exhaust_valve[1] == 0:
                valve_label3.configure(text="CLOSED")
            else:
                valve_label3.configure(text='error')

            valve_label3.after(ref_rate, update)

        update()

    SHED_valvetext_update(SHED2_valve_position_label1, SHED3_valve_position_label1)


class MainApplication(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # Was causing extra frame to pop up

        self.root = tk.Frame()  # create instance of Tk
        self.root.pack()
        self.start_frame = ttk.Frame(self.root)
        self.start_frame.pack(pady = 10)
        self.start_btns = SHEDoperation(self.start_frame,self)
        self.start_btns.pack()
        #self.root.title("SHED Auxiliary Control V2")
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Auxiliary Health')
        self.tabControl.add(self.tab2, text="Automatic SHED control")
        self.tabControl.add(self.tab3, text='Flow Diagram')
        self.tabControl.pack(expand = True, fill = 'both')

        self.frame_tab1 = Tab1(self.tab1, self)
        self.frame_tab1.grid(row = 0, column = 0, sticky = "nsew")

        self.frame_tab2 = Tab2(self.tab2, self)
        self.frame_tab2.grid(row = 0, column = 0, sticky = "nsew")

        self.frame_tab3 = Tab3(self.tab3, self)
        self.frame_tab3.grid(row = 0, column = 0, sticky = "nsew")

        self.geometry("1024x600")
        self.protocol('WM_DELETE_WINDOW', stop_program)
        self.root.mainloop()


def SHED_Status(self):
    shed_frame = ttk.LabelFrame(self, text="SHED status")
    shed_frame.grid(column=0, row=1)
    SHED1_lbl = tk.Label(shed_frame, text='')
    SHED1_lbl.grid(column=0, row=1)

    def update_SHED_lbl(SHED_lbl):
        def update():
            txt = ['', '', '']
            for i in range(0, 3):
                if SHED_ready[i] == 0:
                    txt[i] = "OFF"
                elif SHED_ready[i] == 1:
                    txt[i] = "Req. Sent"
                elif SHED_ready[i] == 2:
                    txt[i] = "SHED" + str(i) + " Ready"
                else:
                    txt[i] = 'error'
            SHED_lbl.configure(text=txt[0] + '\n' + txt[1] + '\n' + txt[2])
            SHED_lbl.after(10, update)

        update()

    update_SHED_lbl(SHED1_lbl)


class Tab1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        flow_frame = ttk.LabelFrame(self, text = "Flow Monitoring")
        flow_frame.grid(column = 0, row = 0, padx = 10, pady = 10,rowspan=25 )
        flow_main_frame = ttk.LabelFrame(flow_frame, text = "Main Flow")
        flow_main_frame.grid(column = 0, row = 0, pady=5)
        FlowMonitor(flow_main_frame,4,5)
        flow_shed1_frame = ttk.LabelFrame(flow_frame, text = "SHED1 Flow")
        flow_shed1_frame.grid(column = 0, row = 1, pady = 5)
        FlowMonitor(flow_shed1_frame,7,6)
        flow_shed2_frame = ttk.LabelFrame(flow_frame, text = "SHED2 Flow")
        flow_shed2_frame.grid(column = 0, row = 2, pady=5)
        FlowMonitor(flow_shed2_frame,2,3)
        flow_shed3_frame = ttk.LabelFrame(flow_frame, text = "SHED3 Flow")
        flow_shed3_frame.grid(column = 0, row = 3, pady=5)
        FlowMonitor(flow_shed3_frame,0,1)
        #mainflow = FlowDisplay(self, flow_frame)
        #mainflow.grid(column = 10, row = 10)
        shed_frame = ttk.LabelFrame(self, text = "SHED status")
        shed_frame.grid(column = 1,row = 0, padx=10, pady=10)
        SHED1_lbl = tk.Label(shed_frame, text = '')
        SHED1_lbl.grid(column = 0, row = 1)

        def update_SHED_lbl(SHED_lbl):
            def update():
                txt = ['','','']
                for i in range(0,3):
                    if SHED_ready[i] == 0:
                        txt[i]  = "OFF"
                    elif SHED_ready[i] == 1:
                        txt[i] = "Req. Sent"
                    elif SHED_ready[i] == 2:
                        txt[i] = "SHED" +str(i) + " Ready"
                    else:
                        txt[i] = 'error'
                SHED_lbl.configure(text = txt[0] +'\n' +txt[1] + '\n' + txt[2])
                SHED_lbl.after(10, update)
            update()
        update_SHED_lbl(SHED1_lbl)

        # ALARM FRAME
        alarm_frame_tab1 = ttk.LabelFrame(self,text="Alarm Status")
        alarm_frame_tab1.grid(column=3,row=0, padx=10, pady=10)
        AlarmMonitor(alarm_frame_tab1)

        # EXHAUST FRAME
        exhaust_frame_tab1 = ttk.LabelFrame(self, text="Exhaust Status")
        exhaust_frame_tab1.grid(column=2, row=0, padx=10, pady=10, rowspan =2)
        ExhaustMonitor(exhaust_frame_tab1)


class Tab2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #start_frame = ttk.Frame(self)
        #start_frame.grid(column=0,row=0, columnspan=1000, sticky = 'EW')
        #start_btns = SHEDoperation(start_frame,self)
        #start_btns.pack()
        lbl2 = tk.Label(self, text="Tab2")
        lbl2.grid(column = 0, row = 0 )

        #lbl1 = tk.Label(self, text="Tab1", font=LARGE_FONT)
        #lbl1.grid(column=1, row=0, sticky='WE')
        SHED_Status(self)


class Tab3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl3 = tk.Label(self, text="Tab3")
        lbl3.grid(column = 0, row = 0)
        #lbl1 = tk.Label(self, text="Tab1", font=LARGE_FONTn)
        #lbl1.grid(column=1, row=0, sticky='WE')
        shed_frame = ttk.LabelFrame(self, text = "SHED status")
        shed_frame.grid(column = 0,row = 1)
        SHED1_lbl = tk.Label(shed_frame, text='')
        SHED1_lbl.grid(column=0, row=1)

        def update_SHED_lbl(SHED_lbl):
            def update():
                txt = ['', '', '']
                for i in range(0, 3):
                    if SHED_ready[i] == 0:
                        txt[i] = "OFF"
                    elif SHED_ready[i] == 1:
                        txt[i] = "Req. Sent"
                    elif SHED_ready[i] == 2:
                        txt[i] = "SHED" + str(i) + " Ready"
                    else:
                        txt[i] = 'error'
                SHED_lbl.configure(text=txt[0] + '\n' + txt[1] + '\n' + txt[2])
                SHED_lbl.after(10, update)

            update()

        update_SHED_lbl(SHED1_lbl)


def Dataset_save():
    start_date_time = datetime.now().strftime("%d-%b-Y_H-%M-%S")
    filename = str(priority) +"_LOGfile_" +str(start_date_time)


def stop_program():
    global exit_case, SHED1,SHED2,SHED3
    # if okay is selected, the program will terminate itself appropriately
    if messagebox.askokcancel("Quit","Do you want to quit?\nThis will terminate everything including data recording"):
        SHED1 = False
        SHED2 = False
        SHED3 = False
        exit_case = True
        sys.exit()
sched = BackgroundScheduler()
sched.start()
sched.add_job(text_update, 'interval', seconds = .5)
app = MainApplication()