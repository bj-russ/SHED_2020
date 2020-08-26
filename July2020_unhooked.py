#from maq20 import MAQ20
import time
import sys
from time import sleep
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading
from tkinter import ttk
from simple_pid import PID
#from PIL import Image, ImageTk
import xlrd
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pandas import *
import csv
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random
########################################################################################################################
# This code is organized to include the setup, background process, and GUI process. The GUI requires background
# functions to update the text in the GUI. These are refreshed at a rate noted in each function. The actions taken in
# the GUI change values which control using the output values function.
#--------------------------- Setup --------------------------#
exit_case = False   # used to exit multiple threads by using window [x] button
refresh = 100


loc= ("config/config.xlsx")
wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
ip = sheet.cell_value(1, 1)
refresh = int(sheet.cell_value(2,1))
XX = int(sheet.cell_value(3,1))
YY = int(sheet.cell_value(4,1))
ppg = [0]*8
for n in range (0,8):
    ppg[n] = float(sheet.cell_value(6,n+1))     # Update Pulses per gallon according to the Manufactureures Specifications
cal1 = sheet.cell_value(12, 1)                  # Calibration Values for SHED temperature sensors
cal2 = sheet.cell_value(13, 1)
cal3 = sheet.cell_value(14, 1)
cal4 = sheet.cell_value(15, 1)


# Display Settings ####in config file
# XX = 1024
# YY = 600
demo = 1
if demo == 0:
    maq20 = MAQ20(ip_address=ip, port=502)     # Set communication with MAQ20
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
#maq20_initiation()

if demo == 1:
    AI_mod = [0]*8  # Analog input module
    TTC_mod = [0]*8  # Thermocouple input module.
    DIV20_mod = [0]*20  # 20 digital discrete inputs
    DIOL_mod1 = [0]*10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod2 = [0]*10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod3 = [0]*10  # 5 Digital discrete inputs, 5 Digital outputs
    DIOL_mod4 = [0]*10  # 5 Digital discrete inputs, 5 Digital outputs
    AO_mod = [0]*10

    # Read input values from Modules
    DIOL_1 = [0]*10
    DIOL_2 = [0]*10
    DIOL_3 = [0]*10
    DIOL_4 = [0]*10
    T = [0]*8
    AI = [0.1]*8

##########################################################
#              Global Flow Rate Variables                #
##########################################################
if demo == 0:
    ser = serial.Serial(
            port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
)
counter=0
prev_count = [0] * 8
frequency = [0.0]*8
flowrate = [0.0] * 8  # flow rate calculated from pulse count and time
prev_time = time.time()
# ppg = [151.4, 151.4, 75.7, 75.7, 75.7, 151.4, 151.4, 151.4]  # pulses per gallon as per flow meter specs [corrected]


##########################################################
#                   GUI Tab 1 Variables                  #
##########################################################
flow_text1 = [0] *8     # Tab 1
flow_temp_text1 = [0] *8
flow_valve_text1 = [0] *8
shed_temp_text1 = [0] *2
pump_text1 = [0] *8

##########################################################
#                     GUI variables                      #
#  These variables are required to be global as they are #
#  referred to in the background as well as foreground   #
##########################################################
pump_text = [0]*8
header = [None] * 8
header2 = [None] * 8

temp_text2 = [0] * 8    # Tab 2
flow_text2 = [0] * 8    # Tab 2
shed_temp_text = [0] * 2
shed_temp_text2 = [0] * 2
shed_temp_text21 = [0] * 2
flow_rate_text = [0] * 8
flow_rate_text2 = [0] * 8
delta_t_text = [0]*2
shed_temp_value = [0]*2        # Combined average for L and R temperature measures inside of SHED
#valve_text1 = [0]*8
valve_text2 = [0]*2     # Valve position Text
flow_status_gui = [0] * 3   # Flow status as text for each SHED. Cases are further discussed in code
flow_status = [0] *3        # Flow status as a value for each SHED.

SHED1 = False   #SHED1 is off to start
SHED2 = False   #SHED2 is off to start
SHED3 = False   #SHED3 is off to start

##########################################################
#              Variables for Digital Input               #
##########################################################
exhaust_fan_check = 0 #DIOL_4[5]
##########################################################
#                 Variables for smoothing                #
##########################################################
smoothing_size = int(sheet.cell_value(17,1))    # size of list used for smoothing average
smooth_t2 = 0
smooth_t3 = 0
T_shed2 = [20] * smoothing_size      # initiate list as size of smoothing_size
T_shed3 = [20] * smoothing_size

##########################################################
#                  Variables for output                  #
##########################################################
pump_io = [0]*8     # pump status as value [  1 for on, 0 for off ]
pump_error = [0]*8
set_temp = [43,43] # Set temp can be changed in the GUI. Currently only options are 43 and 23 degrees
delta_t = [0]*2 # the difference between measured SHED temperature and set temp
pid_vout = [10] * 2 # Power Voltage to each valve - 10V is open
alarm_status = [False] *3 # Alarm status starts off as false
door_seal = [0] * 2 # not used in current setup (2020)
exhaust_valve = [0] * 2 # exhaust valve on back of
good_to_start = [0] * 3
extractor_fan = 0 # 0 for off, 1 for on
exhaust_damper = 0 # 0 for open, 1 for closed

##########################################################
#                      Analog Out                        #
##########################################################

valve_V = AO_mod[:]
##########################################################
#                     Digital Out                        #
##########################################################

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

pid1 = PID(P1, I1, D1, set_temp[0]) # PID for SHED2
pid1.output_limits = (0, 10)
pid2 = PID(P2, I2, D2, set_temp[1]) # PID for SHED3
pid2.output_limits = (0, 10)

index=0
flash_index = 0

def flash__():
    global flash_index
    flash_index = 1- flash_index


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
            flowrate[n] = frequency[n]/ppg[n] # Flowrate in Gallons/min
            #print("Pump number " + str(n) + "\nFrequency is: " + str(frequency[n]) + " Pulses Per Minute!\nFlowrate is: " + str(flowrate[n]) + " GPM")

        prev_count = current_count
        prev_time = current_time
    except:
        return
    #print(fixed_str)
    #print( fixed_str[1], type(fixed_str[1]))
    #print(current_count, type(current_count))
    #print(fixed_int[1],type(fixed_int[1]))


########################################################################################################################
###########      Plotting Variables                                                                               ######
# @######################################################################################################################

plot_dict = {}
frame_length = 100
plot_interval = 10 # in seconds
def save_for_plot():
    global plot_dict
    entry_time = datetime.now().strftime("%d/%b/%Y_%H:%M")
    Header_list = ["Entry Time", "SHED2 Set Temp", "SHED2 Temp", "PID SHED2", "SHED3 Set Temp", "SHED3 Temp", "PID SHED3",
             "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "T1",
             "T2", "T3", "T4", "T5", "T6", "T7", "T8", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8",
             "Req. for Exhaust Fan", "Exhaust Fan Feedback"]

    saveline = [entry_time, set_temp[0], shed_temp_value[0], pid_vout[0], set_temp[1], shed_temp_value[1],
                pid_vout[1],
                pump_io[0], pump_io[1], pump_io[2], pump_io[3], pump_io[4], pump_io[5], pump_io[6], pump_io[7],
                flowrate[0], flowrate[1], flowrate[2], flowrate[3], flowrate[4], flowrate[5], flowrate[6], flowrate[7],
                T[0], T[1], T[2], T[3], T[4], T[5], T[6], T[7],
                valve_V[0], valve_V[1], valve_V[2], valve_V[3], valve_V[4], valve_V[5], valve_V[6], valve_V[7]]

    saveline_list =[]
    for i in range (0,len(saveline)):
        saveline_list.append([saveline[i]]*frame_length)



    if bool(plot_dict) == False:  # is plot_dict empty? if so create first line
        plot_dict = {key: value for key, value in zip(Header_list, saveline_list)}
        plot_dict = {key: value for key, value in zip(Header_list, saveline_list)}
    else:
        for i in range(0, len(saveline)):
            plot_dict[Header_list[i]].append(saveline[i])
            plot_dict[Header_list[i]] = plot_dict[Header_list[i]][-frame_length:]
            #if len(plot_dict[Header_list[i]])> frame_length :        # if dict reaches max length, delete first value.
            #    plot_dict[Header_list[i]] = plot_dict[Header_list[i]][1:]
    print(plot_dict)

########################################################################################################################
#                               SET UP FOR save_to_csv
priority = "POWERON"                                              # Change priority if you want to record SHED 1 values
start_date_time = datetime.now().strftime("%d-%b-%Y_%H-%M")
print(start_date_time)
#filename = str(priority)+"_datalog_"+str(start_date_time)
########################################################################################################################
def save_to_csv():
    start_date_time = datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    filename = str(priority) + "_datalog_" + str(start_date_time)
    entry_time = datetime.now().strftime("%d/%b/%Y_%H:%M")
    entry = {}
    Header = ["Entry Time", "SHED2 Set Temp.","Shed2 Temp.","PID SHED2", "SHED3 Set Temp.", "SHED3 Temp.", "PID SHED3",
               "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "T1",
               "T2", "T3", "T4", "T5", "T6", "T7", "T8", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8",
               "Req. for Exhaust Fan", "Exhaust Fan Feedback"]
    saveline =    [entry_time, set_temp[0], shed_temp_value[0], pid_vout[0], set_temp[1], shed_temp_value[1], pid_vout[1], pump_io[0],
     pump_io[1], pump_io[2], pump_io[3], pump_io[4], pump_io[5], pump_io[6], pump_io[7], flowrate[0], flowrate[1],
     flowrate[2], flowrate[3], flowrate[4], flowrate[5], flowrate[6], flowrate[7], T[0],T[1],T[2],T[3],T[4],T[5],T[6],T[7],valve_V[0], valve_V[1], valve_V[2],
     valve_V[3], valve_V[4], valve_V[5], valve_V[6], valve_V[7]]
    entry = {key:value for key, value in zip(Header,saveline)}
    fieldnames = Header#Header.to_csv(filename,mode = 'a', header = False)
    with open(filename+'.csv','w', newline='') as csv_file:
#        for head in Header:
#            for i in range(0, len(head)):
#                entry[head] = saveline[i]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(entry)


    def save_time():
        Header = ["Entry Time", "SHED2 Set Temp.", "Shed2 Temp.", "PID SHED2", "SHED3 Set Temp.", "SHED3 Temp.",
                  "PID SHED3",
                  "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "T1",
                  "T2", "T3", "T4", "T5", "T6", "T7", "T8", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8",
                  "Req. for Exhaust Fan", "Exhaust Fan Feedback"]
        saveline = [entry_time, set_temp[0], shed_temp_value[0], pid_vout[0], set_temp[1], shed_temp_value[1],
                    pid_vout[1], pump_io[0],
                    pump_io[1], pump_io[2], pump_io[3], pump_io[4], pump_io[5], pump_io[6], pump_io[7], flowrate[0],
                    flowrate[1],
                    flowrate[2], flowrate[3], flowrate[4], flowrate[5], flowrate[6], flowrate[7], T[0], T[1], T[2],
                    T[3], T[4], T[5], T[6], T[7], valve_V[0], valve_V[1], valve_V[2],
                    valve_V[3], valve_V[4], valve_V[5], valve_V[6], valve_V[7]]
        print('savetime is working')
        entry = {key:value for key, value in zip(Header,saveline)}
        with open(filename+".csv",'a', newline = '') as csv_file:
            fieldnames=Header
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(entry)

        if exit_case == True:
            sched.shutdown()
    sched.add_job(save_time,'interval',seconds = 60)



def flow_check(): # Checks Flowrate for Back Flow, Also Checks Exhaust Flow
    # ---------- Flow / Temperature Status --------- #
    # SHED 1 Flow Status
    if SHED1 is True: #and flowrate[6] > 0 and flowrate[5] > 0:
        if flowrate[5] > flowrate[6]:
            flow_status[0] = 1      # Flow Rate Normal
        else:
            flow_status[0] = 2      # Back Flow in Cold Loop
    elif SHED1 is False:
        flow_status[0] = 0          # SHED off - No Check needed

    #SHED 2 Flow Status
    # This is set up to check both cold and hot flows
    if SHED2 is True:# and flowrate[2] > 0 and flowrate[3] > 0 and flowrate[4] > 0 and flowrate[5] > 0:
        if flowrate[5] > flowrate[3] and flowrate[4] > flowrate[2]:
            flow_status[1] = 1  # Flow rate normal
        else:
            if flowrate[5] < flowrate[3]:
                flow_status[1] = 2  # Back Flow in cold loop
            elif flowrate[4] < flowrate[2]:
                flow_status[1] = 3  # Back Flow in Hot loop
            else:
                flow_status[1] = 4  # unknown Error
    else:
        flow_status[1] = 0  # SHED 2 not on

    # SHED3 Flow Status
    if SHED3 is True:# and flowrate[4] > 0 and flowrate[0] > 0:
        if flowrate[4] > flowrate[0]:
            flow_status[2] = 1  # Flow rate normal
        else:
            flow_status[2] = 3  # Back Flow in Hot Loop
    else:
        flow_status[2] = 0  # SHED 3 not on

    # Exhaust Flow Check
    exhaust_fan_check = DIOL_4[5]
def flow_calculate(flow_text, n):
    def flow_update():
        txt = ''
        # for n in range(0,8):
        flow_text[n].configure(text="Flowrate \n" + str(round(flowrate[n], 2)) + " GPM")
        #print(flowrate[n])
        flow_text[n].after(refresh, flow_update)
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
        pump_text[i].after(refresh, pump_text_update)

    pump_text_update()

def flow_temp_status(temp_text,n):
    def temp_text_update():
        txt = ""
        txt = "Temp." + str(n + 1) + "\n" +str(round(T[n],2)) + u'\N{DEGREE SIGN}'+"C"
        temp_text[n].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off
        temp_text[n].after(refresh, temp_text_update)
    temp_text_update()

def valve_position(valve_text,n):
    def valve_text_update():
        txt=""
        txt="Valve Pos." + str(n+1) + "\n" + str(round(100*valve_V[n]/10,2)) +"%"
        valve_text[n].configure(text=txt)
        valve_text[n].after(refresh, valve_text_update)
    valve_text_update()

def valve_pid1(): # PID for SHED2
    global pid_vout
    if SHED2 == True:
        pid1.setpoint = set_temp[0]
        pid_vout[0] = pid1(shed_temp_value[0])
        print("current temp SHED2: " + str(shed_temp_value[0]))
        print( "set point SHED2: " + str(set_temp[0]))
        print ("valve % SHED2: " + str(pid_vout[0] * 10))
        #sleep(1)
    else:
        pid_vout[0] = 10    # set valves open by default


def valve_pid2(): # PID for SHED3
    global pid_vout
    if SHED3 is True:
        pid2.setpoint = set_temp[1]
        pid_vout[1] = pid2(shed_temp_value[1])
        print("current temp SHED3: " +str(shed_temp_value[1])+ " deg C")
        print( "set point SHED3: " + str (set_temp[1]) + " deg C")
        print ("valve % SHED3: " + str(pid_vout[1] * 10))
        #sleep(1)
    else:
        pid_vout[1] = 10     # set valves open by default


def update_pump_text(pump_text,i):

    def pump_text_update():
        txt = " "
        if pump_io[i] == 0:
            txt= "OFF"
        elif pump_io[i] == 1:
            txt = "ON"
        else:
            txt = "error"
        pump_text[i].configure(text=txt)    # Pump text 1 for ON 0 for Off
        pump_text[i].after(refresh, pump_text_update)
    pump_text_update()

def update_pump_text1(pump_text,i): #Update Pump Text for Tab1

    def pump_text_update():
        x=0
        txt = ""

        if pump_io[i] == 0:
            txt= "Pump" + str(i+1) +"\nOFF"
            pump_text[i].configure(text=txt, bg="black", fg="white")  # Pump text 1 for ON 0 for Off


        elif pump_io[i] == 1:
            txt = "Pump" + str(i+1) +"\nON"
            if pump_error == 0:
                pump_text[i].configure(text=txt,bg="green", fg="black")  # Pump text 1 for ON 0 for Off

            if pump_error[i] == 1:
                bgflash=("black","red")
                fgflash=("white","black")
                pump_text[i].configure(bg=bgflash[flash_index], fg = "white")
        else:
            txt = "error"
        pump_text[i].configure(text=txt)    # Pump text 1 for ON 0 for Off


        pump_text[i].after(refresh, pump_text_update)
    pump_text_update()

def read_valve_text(valve_text, i):
    def valve_text_update():
        valve_text[i].configure(text=str(round(pid_vout[i], 2)))
        valve_text[i].after(refresh, valve_text_update)
    valve_text_update()

def valve_text_tab1(valve_text,i):
    def valve_text_update():
        valve_text[i].configure(text=str(round(AO_mod[i], 2)))
        valve_text[i].after(refresh, valve_text_update)
    valve_text_update()

def flow_calculate2(flow_text, n):
    def flow_update():
        # for n in range(0,8):
        flow_text[n].configure(text=round(flowrate[n], 2))
        #print(flowrate[n])
        flow_text[n].after(refresh, flow_update)
    flow_update()

def read_flow_temp(temp_text, i): # used for range i=(0,8) for channel 1-8
    def temp_update():
        # add smoothing function?
        temp_text[i].configure(text=str(round(T[i], 2))) #edits temp_text[i] value
        temp_text[i].after(refresh, temp_update)    # reschedules temp_update function after 100 miliseconds
    temp_update()

def read_flow_temp1(temp_text, i):  #Flow Temperature for Tab1
    def temp_update():
        # add smoothing function?
        temp_text[i].configure(text="Water Temp\n" +str(round(T[i], 2))+ u' \N{DEGREE SIGN}'+"C")  # edits temp_text[i] value
        temp_text[i].after(refresh, temp_update)  # reschedules temp_update function after 100 miliseconds

    temp_update()
    # print(T[0])
    # Thermocouples notation: in list T[n]
    # T0: Shed 3 Hot
    # T1: Shed 3 Cold
    # T2:Shed 2 Hot
    # T3: Shed 2 Cold
    # T4: Main Hot
    # T5: Main Cold
    # T6: Shed1 Cold
    # T7: Shed1 Hot


def read_shed_temp(shed_temp_text, i):  # i to be 0 for SHED2 and 1 for SHED3
    def shed_temp_update():
        global shed_temp_value, smooth_t2, smooth_t3
        if smooth_t2 == len(T_shed2):
            smooth_t2 = 0
        if smooth_t3 == len(T_shed3):
            smooth_t3 = 0

        # AI = (AI_mod.read_data(0, number_of_channels=AI_mod.get_number_of_channels()))
        # read data from 0-3 for analog input 1-4

        sum2 = ((AI[0])*cal1+(AI[1])*cal2)/2   # Calibration in Config file
        sum3 = ((AI[2])*cal3+(AI[3])*cal4)/2   # Calibration in config file

        if 1 > AI[0] > 0.15:                            # To filter outliers
            instant_t2 = sum2  ## Need to calibrate

            # for design purposes Shed 2 is AI0 and Shed 3 is AI1
            T_shed2[smooth_t2] = instant_t2
            smooth_t2 = smooth_t2 + 1

        if 1 > AI[1] > 0.15:                            # To filter outliers
            instant_t3 = sum3  ## Need to calibrate
            T_shed3[smooth_t3] = instant_t3
            smooth_t3 = smooth_t3 + 1
        else:
            None

        ave_T_shed2 = round(sum(T_shed2) / float(len(T_shed2)), 2)
        ave_T_shed3 = round(sum(T_shed3) / float(len(T_shed3)), 2)
        shed_temp_value = [ave_T_shed2, ave_T_shed3]
        shed_temp_text[i].configure(text=str(shed_temp_value[i]))
        shed_temp_text[i].after(refresh, shed_temp_update)

    shed_temp_update()


def calc_delta_t(delta_t_text,h):
    def delta_t_update():
        global delta_t
        delta_t[h] = float(shed_temp_value[h]) - int(set_temp[h])
        delta_t_text[h].configure(text=str(round(delta_t[h], 2)))
        delta_t_text[h].after(refresh,delta_t_update)
    delta_t_update()


def alarm_function():
    global SHED1, SHED2, SHED3, pump_text, extractor_fan, exhaust_valve, exhaust_damper

    if alarm_status[0]+alarm_status[1]+alarm_status[2] == 0 :
        extractor_fan= 1
        exhaust_damper = 1
        exhaust_valve = [0,0]
    else:
        extractor_fan = 1
        exhaust_damper = 0
        if alarm_status[0] == 1:
            SHED1 = False
        else:
            pass
        if alarm_status[1] == 1:  # SHED2 Alarm Activated
            exhaust_valve[0] = 1  # valve open
            SHED2 = False
        else:
            exhaust_valve[0] = 0

        if alarm_status[2] == 1:
            exhaust_valve[1] = 1
            SHED3 = False
        else:
            exhaust_valve[1] = 0

def output_control():
    global pump_io, extractor_fan, exhaust_damper, exhaust_valve
    deadhead_protection = sheet.cell_value(22,1)
    valve_op_volt = sheet.cell_value(21,1)  # operational valve voltage -> changed to 5 for testing on 5V system .

    if SHED1 is True:
        #Valve control
        valve_V[6] = 10 * valve_op_volt / 10 # Make sure Cold loop for SHED 1 is open 100%
        valve_V[5] = 5 * valve_op_volt / 10  # adjust Main loop to half open

        if valve_V[6] > deadhead_protection:
            pump_io[6] = 1
        else:
            pump_io[6] = 0
    else: #IF SHED1 is off turn off pump and make sure valve is in default state and main valve is 100% open
        valve_V[5] = 10 * valve_op_volt / 10
        valve_V[6] = 10 * valve_op_volt / 10
        pump_io[6] = 0
        #pump_io[5] = 0

    if SHED2 is True: # FOR TESTING PURPOSES. (SHED 2 is not active)

        valve_V[2] = pid_vout[1] * valve_op_volt / 10
        valve_V[4] = valve_op_volt - pid_vout[1] * valve_op_volt / 10
        #exhaust_valve[0] = 0
        pump_io[3] = 1
        pump_io[2] = 1
    else:
        pump_io[2] = 0 # Hot
        pump_io[3] = 0 # Cold

    if SHED3 is True:
        valve_V[0] = pid_vout[1] * valve_op_volt / 10
        valve_V[4] = valve_op_volt - pid_vout[1] * valve_op_volt / 10
        #exhaust_valve[1] = 0
        if pid_vout[1] * valve_op_volt > deadhead_protection:
            pump_io[0] = 1
        else:
            pump_io[0] = 0

    else:
        #AO_mod[4] = 10 * valve_op_volt / 10     #Valve position open
        #AO_mod[0] = 10 * valve_op_volt / 10     #Valve position open
        pump_io[0] = 0

    # main pumps control
    if pump_io[0] + pump_io[2] + pump_io[7] > 0 or SHED3 is True or SHED2 is True:
        pump_io[4] = 1 # Main Hot on if any of the hot pumps are on
    else:
        pump_io[4] = 0

    if pump_io[1] + pump_io[3] + pump_io[6] > 0 or SHED1 is True or SHED2 is True:
        pump_io[5] = 1 # Main Cold pump on if any Cold pump is on
    else:
        pump_io[5] = 0

    def DIOL_output_function():

        DIOL_mod1[0] = pump_io[0] # SHED3 Hot
        DIOL_mod1[1] = pump_io[1] # SHED3 Cool
        DIOL_mod1[2] = pump_io[2] # SHED2 Hot
        DIOL_mod1[3] = pump_io[3] # SHED2 Cool
        DIOL_mod1[4] = pump_io[4] # MAIN Hot
        DIOL_mod2[0] = pump_io[5] # MAIN Cool
        DIOL_mod2[1] = pump_io[6] # SHED1 Cool
        DIOL_mod2[2] = pump_io[7] # SHED1 Hot
        DIOL_mod2[3] = door_seal[0] # Door Seal SHED2
        DIOL_mod2[4] = exhaust_valve[0]  # Exhaust Valve SHED2
        DIOL_mod3[0] = good_to_start[0] # Ready Signal output for SHED1
        DIOL_mod3[1] = good_to_start[1] # Ready Signal output for SHED2
        DIOL_mod3[2] = good_to_start[2] # Ready Signal output for SHED3
        DIOL_mod3[3] = door_seal[1]     # Door Seal SHED3
        DIOL_mod3[4] = exhaust_valve[1] # Exhaust Valve SHED3
        DIOL_mod4[0] = exhaust_damper   # Exhaust Damper - Located on top of SHED 3. Closed when exhaust is needed.
        DIOL_mod4[1] = extractor_fan
        DIOL_mod4[2] = 0
        DIOL_mod4[3] = 0
        DIOL_mod4[4] = 0
        AO_mod[0] = valve_V[0]
        AO_mod[1] = valve_V[1]
        AO_mod[2] = valve_V[2]
        AO_mod[3] = valve_V[3]
        AO_mod[4] = valve_V[4]
        AO_mod[5] = valve_V[5]
        AO_mod[6] = valve_V[6]
        AO_mod[7] = valve_V[7]
    #DIOL_output_function()

    if SHED1 is True or SHED2 is True or SHED3 is True:
        extractor_fan = 1
        pass
    else:
        extractor_fan = 0



def background_communication():
    global current_in, pulse_count, DIOL_1,DIOL_2,DIOL_3,DIOL_4,T,AI, flowrate,pump_io,  DIOL_mod1

    def pump_error_check():
        global pump_error
        for n in range(0,8):
            if pump_io[n]== 1 and flowrate[n] < 0.5:
                pump_error[n] = 1
            else:
                pump_error[n] = 0

    #while True:
        #sleep(.001)
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
    if demo == 1:
        update_unhooked()
    if demo == 0:
        update_maq20()

    valve_pid1()
    valve_pid2()
    output_control()
    flow_check()
    alarm_function()
    #flash_()
    pump_error_check()
    new_in = [DIOL_1[5], DIOL_1[6], DIOL_1[7], DIOL_1[8], DIOL_1[9], DIOL_2[5], DIOL_2[6],
              DIOL_2[7]]  # used to compare to current_in
    #for n in range(0, 8):
     #   if new_in[n] != current_in[n]:
    #        pulse_count[n] += 1  # should it be .5? .5 for each up or down?
     #       print("Count" + str(n) + ": " + str(pulse_count[n]))
      #      current_in[n] = new_in[n]
       #     flowrate[n] = (((pulse_count[n] - prev_count[n]) / ppg[n]) * 60) / ((time.time() - prev_time[n]))
        #    prev_count[n] = pulse_count[n]
         #   prev_time[n] = time.time()
        #elif new_in[n] == current_in[n] and (time.time()-prev_time[n]) > .5:
         #   flowrate[n] = 0.0
        #else:
         #   pass#print('error')
    if exit_case == True:
        pump_io = [0] * 8
        DIOL_mod1[0] = 0
        DIOL_mod1[1] = 0
        DIOL_mod1[2] = 0
        DIOL_mod1[3] = 0
        DIOL_mod1[4] = 0
        DIOL_mod2[0] = 0
        DIOL_mod2[1] = 0
        DIOL_mod2[2] = 0

        sys.exit()

def record_values_in_csv(priority):
    start_date = datetime.now().strftime("%H_%M_%S")
    print(start_date)

def extractor_status(extractor_fan_label, extractor_status_label):
    def update():
        if extractor_fan == 1:
            extractor_fan_label.configure(text="Exhaust Fan Requested", bg = 'yellow', fg='black')
            if exhaust_fan_check == 0:
                extractor_status_label.configure(text="Exhaust Flow Confirmed",bg="green")
                extractor_fan_label.configure(bg="green")
            else:
                bgflash = ("black", "red")
                extractor_status_label.configure(text = "No Exhaust Flow",bg=bgflash[flash_index], fg="white")
        else:
            extractor_fan_label.configure(
                text="                         Exhaust Fan OFF                          ", bg='black',
                fg='white')
            extractor_status_label.configure(text="Zero Flow", bg="black",fg="white")
        extractor_fan_label.after(refresh, update)
    update()

def GUI():

    window = tk.Tk()
    window.title('SHED Auxiliary Control')

    #window.iconbitmap('CAicon.ico')
    window.maxsize(XX, YY)
    window.minsize(XX,YY)
    #window.wm_attributes("-transparentcolor", 'gold')   #Set transparent colour - makes screen transparent to desktop
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Auxiliary Health')
    tab_control.add(tab2, text="Automatic SHED control")
    tab_control.add(tab3, text='Flow Diagram')
    tab_control.pack(expand=2, fill='both')

########################################################################################################################

    application_window = tab1
    frame1_tab1 = ttk.LabelFrame(application_window, text="Water Flow Monitoring")
    frame1_tab1.grid(row=0,column=0,padx=10, pady=10)
    frame2_tab1 = ttk.Frame(application_window)
    frame2_tab1.grid(row=0,column=2, rowspan = 5, sticky=N)

########################################################################################################################
    application_window = frame1_tab1
    lf0 = ttk.LabelFrame(application_window, text="Main Loop")  # , width=100,height=100)
    lf0.grid(row=0, column=0, padx=10, pady=10)  # ,rowspan=5, columnspan=4)
    lf1 = ttk.LabelFrame(application_window, text="SHED1 Loop")  # , width=100,height=100)
    lf1.grid(row=1, column=0, padx=10, pady=10)
    lf2 = ttk.LabelFrame(application_window, text="SHED2 Loop")  # , width=100,height=100)
    lf2.grid(row=2, column=0, padx=10, pady=10)
    lf3 = ttk.LabelFrame(application_window, text="SHED3 Loop")  # , width=100,height=100)
    lf3.grid(row=3, column=0, padx=10, pady=10)

    flow_width = 8
    pump_width = 5
    flow_temp_width = 8
    valve_width = 10
    def MAIN_tab1():  # MAIN Loop

        application_window = lf0
        hotLabel0 = Label(application_window, text="Hot", font=("Bold", 10), padx=9)
        coldLabel0 = Label(application_window, text="Cold", font=("Bold", 10), padx=9)
        hotLabel0.grid(row=2, column=0)
        coldLabel0.grid(row=3, column=0)
        flow_text1[4] = Label(application_window, padx=10,width = flow_width)
        flow_text1[5] = Label(application_window, padx=10, width = flow_width)
        flow_text1[4].grid(row=2, column=2)
        flow_text1[5].grid(row=3, column=2)
        pump_text1[4] = Label(application_window, padx=10, width = pump_width)
        pump_text1[5] = Label(application_window, padx=10, width = pump_width)
        pump_text1[4].grid(row=2, column=1)
        pump_text1[5].grid(row=3, column=1)
        flow_temp_text1[4] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[5] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[4].grid(row=2, column=3)
        flow_temp_text1[5].grid(row=3, column=3)
        flow_valve_text1[4] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[5] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[4].grid(row=2, column=4)
        flow_valve_text1[5].grid(row=3, column=4)

        for n in range(4, 6):
            pump_status(pump_text1, n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1, n)
            valve_position(flow_valve_text1, n)

    def SHED3_tab1():
        application_window = lf3
        hotLabel3 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel3 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel3.grid(row=2, column=0)
        coldLabel3.grid(row=3, column=0)
        flow_text1[0] = Label(application_window, padx=10, width= flow_width)
        flow_text1[1] = Label(application_window, padx=10, width = flow_width)
        flow_text1[0].grid(row=2, column=2)
        flow_text1[1].grid(row=3, column=2)
        pump_text1[0] = Label(application_window, padx=10, width = pump_width)
        pump_text1[1] = Label(application_window, padx=10, width = pump_width)
        pump_text1[0].grid(row=2, column=1)
        pump_text1[1].grid(row=3, column=1)
        flow_temp_text1[0] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[1] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[0].grid(row=2, column=3)
        flow_temp_text1[1].grid(row=3, column=3)
        flow_valve_text1[0] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[1] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[0].grid(row=2, column=4)
        flow_valve_text1[1].grid(row=3, column=4)

        for n in range(0, 2):
            pump_status(pump_text1, n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1, n)
            valve_position(flow_valve_text1, n)

    def SHED2_tab1():
        application_window = lf2
        hotLabel2 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel2 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel2.grid(row=2, column=0)
        coldLabel2.grid(row=3, column=0)
        flow_text1[2] = Label(application_window, padx=10, width = flow_width)
        flow_text1[3] = Label(application_window, padx=10, width = flow_width)
        flow_text1[2].grid(row=2, column=2)
        flow_text1[3].grid(row=3, column=2)
        pump_text1[2] = Label(application_window, padx=10,width = pump_width)
        pump_text1[3] = Label(application_window, padx=10,width = pump_width)
        pump_text1[2].grid(row=2, column=1)
        pump_text1[3].grid(row=3, column=1)
        flow_temp_text1[2] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[3] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[2].grid(row=2, column=3)
        flow_temp_text1[3].grid(row=3, column=3)
        flow_valve_text1[2] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[3] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[2].grid(row=2, column=4)
        flow_valve_text1[3].grid(row=3, column=4)

        for n in range(2, 4):
            pump_status(pump_text1, n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1, n)
            valve_position(flow_valve_text1, n)

    def SHED1_tab1():
        application_window = lf1
        hotLabel1 = Label(application_window, text="Hot", font=("Bold", 10), padx=10)
        coldLabel1 = Label(application_window, text="Cold", font=("Bold", 10), padx=10)
        hotLabel1.grid(row=2, column=0)
        coldLabel1.grid(row=3, column=0)

        flow_text1[7] = Label(application_window, padx=10, width = flow_width)
        flow_text1[6] = Label(application_window, padx=10, width = flow_width)
        flow_text1[7].grid(row=2, column=2)
        flow_text1[6].grid(row=3, column=2)
        pump_text1[7] = Label(application_window, padx=10,width = pump_width)
        pump_text1[6] = Label(application_window, padx=10,width = pump_width)
        pump_text1[7].grid(row=2, column=1)
        pump_text1[6].grid(row=3, column=1)
        flow_temp_text1[7] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[6] = Label(application_window, padx=10, width = flow_temp_width)
        flow_temp_text1[7].grid(row=2, column=3)
        flow_temp_text1[6].grid(row=3, column=3)
        flow_valve_text1[7] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[6] = Label(application_window, padx=10, width = valve_width)
        flow_valve_text1[7].grid(row=2, column=4)
        flow_valve_text1[6].grid(row=3, column=4)

        for n in range(6, 8):
            pump_status(pump_text1, n)
            flow_calculate(flow_text1, n)
            flow_temp_status(flow_temp_text1, n)
            valve_position(flow_valve_text1, n)

    MAIN_tab1()
    SHED1_tab1()
    SHED2_tab1()
    SHED3_tab1()

    application_window= frame2_tab1
    datalog_start_button= Button(application_window, text="Data Logger Start",command=save_to_csv, pady = 5)
    datalog_start_button.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady=5)
    lf4 = ttk.LabelFrame(application_window, text="Exhaust")
    lf4.grid(row=1,column=0, pady = 10)
    lf5 = ttk.LabelFrame(application_window, text="Alarms")
    lf5.grid(row=1,column=1, padx = 30)
    plot_frame = ttk.LabelFrame(application_window, text="Shed Temperature History")
    plot_frame.grid(row=2,column=0,padx = 30, pady=3, columnspan = 4, rowspan = 4)

    def Exhaust_tab1():
        def text_update(text_to_update, value_to_update):
            def refresh_val():
                text_to_update.configure(text=str(value_to_update))
                text_to_update.after(10, refresh_val)
            refresh_val()
        application_window = lf4
        damper_label1 = Label(application_window, text = "Damper Position: ",font=("Bold",10), justify = RIGHT)
        damper_label1.grid(row=0, column=0, sticky = E)
        damper_position_label1 = Label(application_window, text = "test")
        damper_position_label1.grid(row= 0, column=1)

        def damper_label1_update(exhaust_damper_label):
            def update():
                if exhaust_damper == 1:
                    exhaust_damper_label.configure(text="CLOSED")
                else:
                    exhaust_damper_label.configure(text="OPEN")
                exhaust_damper_label.after(refresh, update)
            update()
        damper_label1_update(damper_position_label1)
        exhaustfan_label1 = Label(application_window, text ="Exhaust fan: ", font=("Bold",10))
        exhaustfan_label1.grid(row=1,column=0, sticky = E)
        exhaustfan_io_label1 = Label(application_window, text = "test")
        exhaustfan_io_label1.grid(row= 1, column=1)
        exhaustfan_feedback_label1 = Label(application_window, text = "test2")
        exhaustfan_feedback_label1.grid(row= 1, column=2)
        def extractor_status_update(extractor_fan_label, extractor_status_label):
            def update():
                if extractor_fan == 1:
                    extractor_fan_label.configure(text="Requested", fg = 'black')
                else:
                    extractor_fan_label.configure(text="off", fg = "black")
                    extractor_status_label.configure(text="Zero Flow", fg= "black")
                if exhaust_fan_check == 0:
                    extractor_status_label.configure(text="Confirmed")
                    extractor_fan_label.configure(fg="black")
                else:
                    fgflash = ("black", "red")
                    extractor_status_label.configure(text="Zero Flow", fg=fgflash[flash_index])
                extractor_fan_label.after(refresh, update)
            update()
        extractor_status_update(exhaustfan_io_label1,exhaustfan_feedback_label1)
        SHED2_label1 = Label(application_window, text = "SHED2 Exhaust: ", font=("Bold",10), justify = RIGHT)
        SHED2_label1.grid(row=2,column=0, sticky = E)
        SHED2_valve_position_label1 = Label(application_window, text = "test")
        SHED2_valve_position_label1.grid(row= 2, column=1)
        SHED3_label1 = Label(application_window, text="SHED3 Exhaust: ", font=("Bold", 10), justify = RIGHT)
        SHED3_label1.grid(row=3, column=0, sticky = E)
        SHED3_valve_position_label1 = Label(application_window, text = "test")
        SHED3_valve_position_label1.grid(row= 3, column=1)

        def SHED_valvetext_update(valve_label2, valve_label3):
            def update():
                if exhaust_valve[0] == 1:
                    valve_label2.configure(text="OPEN")
                elif exhaust_valve[0] == 0:
                    valve_label2.configure(text="CLOSED")
                else:
                    valve_label2.configure(text = 'error')
                if exhaust_valve[1] == 1:
                    valve_label3.configure(text="OPEN")
                elif exhaust_valve[1] == 0:
                    valve_label3.configure(text="CLOSED")
                else:
                    valve_label3.configure(text = 'error')

                valve_label3.after(refresh, update)
            update()
        SHED_valvetext_update(SHED2_valve_position_label1, SHED3_valve_position_label1)


    def Alarm_tab1():
        application_window =lf5
        SHED1alarm_label1 = Label(application_window, text="SHED1: ")
        SHED2alarm_label1 = Label(application_window, text="SHED2: ")
        SHED3alarm_label1 = Label(application_window, text="SHED2: ")
        SHED1alarm_label1.grid(row=1, column=1)
        SHED2alarm_label1.grid(row=2, column=1)
        SHED3alarm_label1.grid(row=3, column=1)
        SHEDalarm_label_status=[Label(application_window,text =''),Label(application_window,text =''),Label(application_window,text ='')]
        for i in range(0,3):
            SHEDalarm_label_status[i].grid(row = i+1, column = 2)

        def SHEDalarm_label1_update(label):
            def update():
                for i in range(0,3):
                    if alarm_status[i] == 0:
                        label[i].configure(text = "inactive",fg='black')
                    elif alarm_status[i] == 1:
                        label[i].configure(text="ACTIVE", fg='red')
                    else:
                        label[i].configure(text='CODE ERROR')
                label[0].after(refresh,update)
            update()
        SHEDalarm_label1_update(SHEDalarm_label_status)

    Exhaust_tab1()
    Alarm_tab1()

    def plots_tab1():
        application_window = plot_frame
        def plot_try1():
            application_window = plot_frame
            fig_x = 6
            fig_y = 4
            fig_dpi = 80
            x1_val = [] # plot_dict.get("Entry Time")
            y1_val = [] # plot_dict.get("SHED2 Temp")
            yar = []
            xar = []
            y2_val = [] # plot_dict.get("SHED3 Temp")
            fig = plt.figure(figsize=(fig_x, fig_y), dpi=fig_dpi)
            ax1 = fig.add_subplot(1,1,1)
            ax1.set_ylim(0, 100)
            ax1.set_xlim(0, 100)
            line, = ax1.plot(xar, yar, marker='o')
            line1, = ax1.plot(x1_val,y1_val)
            line2, = ax1.plot(x1_val,y2_val)
            ax1.legend(['SHED2', 'SHED3'])

            def animate(i):
                x1_val.append(plot_dict.get("Entry Time"))
                y1_val.append(plot_dict.get("SHED2 Temp"))
                y2_val.append(plot_dict.get("SHED3 Temp"))
                x1_val = x1_val[-frame_length:]
                y1_val = y1_val[-frame_length:]
                y2_val = y2_val[-frame_length:]
                yar.append(99 - i)
                xar.append(i)
                fig.plot(x1_val,y1_val)
                #line.set_data(xar, yar)
                #ax1.set_xlim(0, i + 1)
                #if x1_val != None:
                #    line1.set_data(x1_val, y1_val)
                #    line2.set_data(x1_val, y2_val)
                #    #ax1.set_ylim(min(y1_val)-5,max(y1_val)+5)
                #    ax1.set_xlim(0,len(x1_val))
                print("Plot Should Be updating!")

            plotcanvas = FigureCanvasTkAgg(fig, plot_frame)
            plotcanvas.get_tk_widget().grid(column=1, row=1)
            ani = animation.FuncAnimation(fig, animate, interval=1, blit=False)




            #fig2 = Figure(figsize=(fig_x, fig_y), dpi=fig_dpi)
            #canvas = FigureCanvasTkAgg(fig, application_window)  # A tk.DrawingArea.
            #canvas.draw()
            #canvas.get_tk_widget().pack()#side=tk.TOP, fill=tk.BOTH, expand=1)

            #toolbar = NavigationToolbar2Tk(canvas, application_window)
            #toolbar.update()
            #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def plot1_():
            application_window = plot_frame
            Refresh = Label(application_window, text = 'refresh')
            Refresh.grid(row=10,column=10)
            try:
                plot1 = plt.figure(figsize=(100, 20))
                x_val = plot_dict.get("Entry Time")
                y_val = plot_dict.get("SHED2 Temp")
                if x_val != None:
                    print(x_val, y_val)
                plt.plot(range(len(x_val)),y_val)
                canvas = FigureCanvasTkAgg(plot1, application_window)
                canvas.show()
                canvas.get_tk_widget().pack.grid(row=11,column=10)
            except:
                pass
            Refresh.after(1000,plot1_)

        #plot1_()
        plot_try1()
    #plots_tab1()

########################################################################################################################
    application_window = tab2
########################################################################################################################

    def start_btn1_clicked():
        global SHED1
        start_btn1.configure(text="Stop", command=start_btn1_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        SHED1 = True

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    def start_btn1_stop():
        global SHED1
        SHED1 = False
        start_btn1.configure(text="Start", command=start_btn1_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        # start_btn1.grid(column=1, row=1)

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    def start_btn2_clicked():
        global SHED2
        SHED2 = True
        start_btn2.configure(text="Stop", command=start_btn2_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)


        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))
        # Exhaust Fan ON
        # Check Exhaust Flow
        # Check Flowrate and Temperatures
        # Temp SHED3 Hot > 45 degC, Main Hot >45 degC
        # Delta SHED3 Hot, Main Hot < 5 degC
        # Flowrate SHED3 HOT >____________
        # Flowrate SHED3 HOT < MAIN
        # SHED3 Temperature = Setpoint +/- 3 degC
        # Alarm = False
    def start_btn2_stop():
        global SHED2
        start_btn2.configure(text="Start", command=start_btn2_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        SHED2 = False

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    def start_btn3_clicked():
        global SHED3
        SHED3 = True
        start_btn3.configure(text="Stop", command=start_btn3_stop,
                             bg="red")  # = Button(application_window, text="Start", command=start_btn1_clicked)

        # Main Pump HOT ON, SHED3 Pump hot ON

        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))
        # Exhaust Fan ON
        # Check Exhaust Flow
        # Check Flowrate and Temperatures
        # Temp SHED3 Hot > 45 degC, Main Hot >45 degC
        # Delta SHED3 Hot, Main Hot < 5 degC
        # Flowrate SHED3 HOT >____________
        # Flowrate SHED3 HOT < MAIN
        # SHED3 Temperature = Setpoint +/- 3 degC
        # Alarm = False
    def start_btn3_stop():
        global SHED3
        SHED3 = False
        start_btn3.configure(text="Start", command=start_btn3_clicked,
                             bg="green")  # = Button(application_window, text="Start", command=start_btn1_clicked)
        # start_btn1.grid(column=1, row=1)


        for j in range(0, 8):
            pump_text[j].configure(text=str(pump_io[j]))

    table_label = ["Request to Start",
                   "SHED Temp. Status",
                   "SHED Temp. (deg C)",
                   "SHED set point (deg C)",
                   "Delta T",
                   "Valve (V)",
                   "Flow Temp. Status",
                   "Flow Status",
                   "Request for Exhaust Fan",
                   "Exhaust Damper Position",
                   "LEL Alarm"
                   ]
    Label(application_window, text = "SHED 1").grid(column=1, row=0)
    Label(application_window, text = "SHED 2").grid(column=2, row=0)
    Label(application_window, text = "SHED 3").grid(column=3, row=0)
    Label(application_window, text = "Status").grid(column=0, row=1)
    for j in range(0,len(table_label)):
        Label(application_window, text=table_label[j], padx=5, pady=5).grid(column=0, row=(j+1))

    start_btn1 = Button(application_window, text="Start", command=start_btn1_clicked, bg='green')
    start_btn2 = Button(application_window, text="Start", command=start_btn2_clicked, bg='green')
    start_btn3 = Button(application_window, text="Start", command=start_btn3_clicked, bg='green')
    start_btn1.grid(column=1, row=1)
    start_btn2.grid(column=2, row=1)
    start_btn3.grid(column=3, row=1)

    if alarm_status[1] == 1:
        start_btn2_stop()
    if alarm_status[2] == 1:
        start_btn3_stop()

    pump_label = ["SHED3 Hot",
                  "SHED3 Cold",
                  "SHED2 Hot",
                  "SHED2 Cold",
                  "MAIN Hot",
                  "MAIN Cold",
                  "SHED1 Cold",
                  "SHED1 Hot"
                  ]
    for j in range(0, len(pump_label)):
        Label(application_window, text=pump_label[j], padx=20, pady=5).grid(column=5, row=1+j)
    component_list = ["Pump\nStatus",
                      "Temp.",
                      "Flow\nRate"
                      ]
    for j in range(0, len(component_list)):
        Label(application_window, text = component_list[j], padx=5, pady=10).grid(column= 6+j, row = 0)


    for n in range(0, 8):
        pump_text[n] = Label(application_window, text= str(pump_io[n]), padx=5,pady=5)
        pump_text[n].grid(column=6, row=1+n)
        update_pump_text(pump_text,n)
        temp_text2[n] = Label(application_window)
        temp_text2[n].grid(column=7, row=1+n)
        read_flow_temp(temp_text2, n)
        flow_text2[n] = Label(application_window)
        flow_text2[n].grid(column=8, row=1+n)
        flow_calculate2(flow_text2, n)

    ##SHED TEMPERATURE ###
    for h in range(0, 2):
        shed_temp_text2[h] = Label(application_window)
        shed_temp_text2[h].grid(column=h + 2, row=3)
        read_shed_temp(shed_temp_text2, h)
    def get_set_temp2(event):
        global set_temp
        set_temp[0] = float(temp_set2.get())
    def get_set_temp3(event):
        global set_temp
        set_temp[1] = float(temp_set3.get())
    ## SHED SET POINT ###
    temp_set2 = Combobox(application_window, width = 5, justify = CENTER , state= "readonly", values = [23,43])
    temp_set2.current(1)
    temp_set2.bind("<<ComboboxSelected>>", get_set_temp2)
    temp_set2.grid(column=2,row=4)
    temp_set3 = Combobox(application_window, width = 5, justify = CENTER, state= "readonly", values = [23,25,26,27,28,29,30,35,40,43])
    temp_set3.current(1)
    temp_set3.bind("<<ComboboxSelected>>", get_set_temp3)
    temp_set3.grid(column=3,row=4)

    ## DELTA T ##
    for h in range (0,2):
        delta_t_text[h] = Label(application_window)
        delta_t_text[h].grid(column=h + 2, row=5)
        calc_delta_t(delta_t_text,h)
    ##Valve Voltage ##
    for h in range(0,2):
        valve_text2[h] = Label(application_window)
        valve_text2[h].grid(column= h+2, row = 6)
        read_valve_text(valve_text2,h)


    # Progress bar for SHED2 and SHED3 Temperature
    progress_temp2 = Progressbar(application_window, orient=HORIZONTAL, length=75)#, mode = 'indeterminate')
    progress_temp3 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_temp2.grid(column=2, row=2)
    progress_temp3.grid(column= 3, row =2)

    def bar_temp():
        def refresh_val():
            progress_temp2.configure(value=75 * shed_temp_value[0] / float(temp_set2.get()))
            progress_temp3.configure(value=75 * shed_temp_value[1] / float(temp_set3.get()))
            progress_temp2.after(10, refresh_val)
        refresh_val()
    bar_temp()

    progress_flowtemp1 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp2 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp3 = Progressbar(application_window, orient=HORIZONTAL, length=75)
    progress_flowtemp1.grid(column=1, row=7)
    progress_flowtemp2.grid(column=2, row=7)
    progress_flowtemp3.grid(column= 3, row =7)

    def flow_status_update(flow_status_gui, h):
        def update():
            global flow_status_gui
            if flow_status[h] == 0:
                flow_status_gui[h].configure(text="            SHED"+str(h+1)+ " off          ", bg = "light grey")
            if flow_status[h] == 1:
                flow_status_gui[h].configure(text="     Flow is Good     ")
            if flow_status[h] == 2:
                flow_status_gui[h].configure(text="Back flow in Cool Loop", bg = "red")
            if flow_status[h] == 3:
                flow_status_gui[h].configure(text=" Back flow in Hot Loop", bg= "red")
            if flow_status[h] == 4:
                flow_status_gui[h].configure(text="     Unknown Error    ", bg = "red")
            flow_status_gui[h].after(refresh, update)
        update()
    for h in range (0,3):
        flow_status_gui[h] = Label(application_window)
        flow_status_gui[h].grid(column = h+1, row=8)
        flow_status_update(flow_status_gui,h)


    extractor_fan_label = Label(application_window)
    extractor_fan_label.grid(column = 1, columnspan = 2, row = 9)
    extractor_status_label = Label (application_window)
    extractor_status_label.grid(column=3,columnspan=1,row=9)
    extractor_status(extractor_fan_label, extractor_status_label)

    def exhaust_damper_status(exhaust_damper_label):
        def update():
            if exhaust_damper == 1:
                exhaust_damper_label.configure(
                    text="                      Exhaust Damper CLOSED                       ", bg='green',
                    fg='black')
            else:
                exhaust_damper_label.configure(
                    text="                            Exhaust Damper OPEN                           ", bg='black',
                    fg='white')

            exhaust_damper_label.after(refresh, update)

        update()

    exhaust_damper_label = Label(application_window)
    exhaust_damper_label.grid(column=1, columnspan=3, row=10)
    exhaust_damper_status(exhaust_damper_label)


    def reset_alarm1():
        global alarm_status, exhaust_damper

        alarm_status[0] = 0
        if alarm_status == [0,0,0]:
            exhaust_damper = 0
        LEL_btn1.configure(text="Test Alarm", command=alarm1, bg='green')


    def reset_alarm2():
        global alarm_status, exhaust_damper

        alarm_status[1] = 0
        if alarm_status == [0,0,0]:
            exhaust_damper = 0

        LEL_btn2.configure(text="Test Alarm", command=alarm2, bg='green')

    def reset_alarm3():
        global alarm_status, exhaust_damper

        alarm_status[2] = 0
        if alarm_status == [0,0,0]:
            exhaust_damper = 0
        LEL_btn3.configure(text="Test Alarm", command=alarm3, bg='green')

    def alarm1():
        alarm_status[0] = 1
        start_btn1_stop()
        pump_io[5] = 1
        pump_io[6] = 1
        LEL_btn1.configure(text = "reset Alarm", command = reset_alarm1, bg='red')
        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED1")

    def alarm2():
        alarm_status[1] = 1

        start_btn2_stop()
        LEL_btn2.configure(text="reset Alarm", command=reset_alarm2, bg='red')
        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED2")

    def alarm3():
        alarm_status[2] = 1
        start_btn3_stop()
        LEL_btn3.configure(text="reset Alarm", command=reset_alarm3, bg='red')
        messagebox.showerror("Warning", "Please acknowledge Alarm for SHED3")

    LEL_btn1 = Button(application_window, text="Alarm Test1", command=alarm1, bg='green')
    LEL_btn2 = Button(application_window, text="Alarm Test2", command=alarm2, bg='green')
    LEL_btn3 = Button(application_window, text="Alarm Test3", command=alarm3, bg='green')
    LEL_btn1.grid(column=1, row=11)
    LEL_btn2.grid(column=2, row=11)
    LEL_btn3.grid(column=3, row=11)

########################################################################################################################
    application_window = tab3
    canvas = Canvas(application_window, width = XX-50,height=YY-50,bg='grey')
    canvas.pack()
    #image = Image.open("display/Pump.png")
    #image = image.rotate(-90)
    #pump_vert = ImageTk.PhotoImage(image.resize((30,30)))

    #image = image.rotate(180)
    #pump_main_image = ImageTk.PhotoImage(image.resize((30,30)))



    #symb_pump = (img2)

########################################################################################################################


    p1x = 250
    p2x = p1x+50
    p3x = p2x+100
    p4x = p3x+50
    p7x = p4x+100
    p8x = p7x+50
    p5x = 100
    p6x = p5x+50
    p1y = 100
    p5y = 300
    #canvas.create_image(p1x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p2x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p3x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p4x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p5x, p5y, image=pump_main_image, anchor=NW)
    #canvas.create_image(p6x, p5y, image=pump_main_image, anchor=NW)
    #canvas.create_image(p7x, p1y, image=pump_vert, anchor=NW)
    #canvas.create_image(p8x, p1y, image=pump_vert, anchor=NW)

    def stop_program():
        global DIOL_mod1,exit_case,  AO_mod, pump_io, SHED1, SHED2, SHED3
        if messagebox.askokcancel("Quit", "       Do you want to quit?\nThis will terminate everything"):
            SHED1 = False
            SHED2 = False
            SHED3 = False
            exit_case = True
            sys.exit()
    window.protocol('WM_DELETE_WINDOW',stop_program)
    plots_tab1()
    window.mainloop()

if demo ==0:
    if maq20[1] is None:
        raise TypeError("Module Not Found.\n Connect DATAFORTH system and ensure proper IP address!")

sched = BackgroundScheduler()
sched.start()
sched.add_job(flash__,'interval',seconds = 1)
sched.add_job(save_for_plot, 'interval', seconds = plot_interval)
sched.add_job(background_communication,'interval',seconds = .5)
background_thread = threading.Thread(target=background_communication)
GUI_thread = threading.Thread(target=GUI)


#background_thread.start()
#GUI_thread.start()
GUI()

